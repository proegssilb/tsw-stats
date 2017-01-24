"""A module for handling really generic queries.

Things like "Get an arbitrary window of data from an table I tell you."
"""

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


def getDataTable(dataRequest, dbSession):
    """Return a dictionary representing a data table.

    Takes a parsed DataRequest object, and the class to query, and returns the
    data requested.
    """
    modelClass = dataRequest.table
    baseQuery = dbSession.query(modelClass)
    totalObjects = baseQuery.count()
    # TODO: Searching.
    filteredQuery = baseQuery.order_by(*dataRequest.ordering)
    filteredObjects = filteredQuery.count()
    objsList = filteredQuery.offset(dataRequest.offset).limit(
        dataRequest.limit).all()
    return {
        'draw': dataRequest.draw,
        'recordsFiltered': filteredObjects,
        'recordsTotal': totalObjects,
        'data': objsList
    }
