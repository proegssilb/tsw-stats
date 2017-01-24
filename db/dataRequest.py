"""DataRequest class.

Represents a request from DataTables for a particular set of data.
"""

import logging as logger
from sqlalchemy.inspection import inspect

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"
__all__ = ('DataRequest', '__author__', '__copyright__', '__license__',
           '__version__')


def validateBool(**kws):
    for argName, value in kws.items():
        if value not in (True, False, 'true', 'false', '1', '0'):
            logger.warn(
                'Found invalid boolean in %s: "%s". Coercing to False.',
                argName, value
                )
            return False
        else:
            return value in [True, 'true', '1']


class DataRequest:
    """Represents the parse results of a DataTables AJAX request."""

    draw = 1
    limit = 25
    offset = 0
    globalSearchTerm = None
    globalSearchIsRegex = False
    columns = dict()
    columnSearch = dict()
    table = None
    ordering = ()

    def __init__(self, table, json):
        """
        Initialize a DataRequest.

        Takes a SqlAlchemy table and a DataTables JSON request.
        """
        self.table = table
        self.draw = int(json['draw'])
        self.limit = int(json['length'])
        if self.limit > 500:
            raise ValueError('Asked for too many records.')
        self.offset = int(json['start'])
        self.globalSearchTerm = json['search']['value']
        self.globalSearchIsRegex = validateBool(
            globalSearchIsRegex=json['search']['regex']
            )
        self.columns = {}
        self.columnSearch = {}
        for colSpec in json['columns']:
            columnName = colSpec['data']
            if not columnName.isalpha():
                raise ValueError('Found invalid column name: "{}"'.format(
                    columnName
                    ))
            isSearchable = validateBool(isSearchable=colSpec['searchable'])
            isOrderable = validateBool(isOrderable=colSpec['orderable'])
            self.columns[columnName] = {'orderable': isOrderable,
                                        'searchable': isSearchable
                                        }
            colSearch = colSpec['search']['value']
            colRegex = validateBool(colRegex=colSpec['search']['regex'])
            self.columnSearch[columnName] = {
                'term': colSearch,
                'regex': colRegex
            }

        colList = [c['data'] for c in json['columns']]
        self.ordering = ((colList[o['column']], o['dir']) for o in
                         json['order'])
        cols = inspect(self.table).c
        self.ordering = tuple(cols[col].desc() if direct == 'desc' else
                              cols[col] for (col, direct) in self.ordering)
