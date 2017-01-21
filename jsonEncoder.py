"""A custom JSON encoder with support for Decimal and SqlAlchemy models."""

import json
import decimal as d
from db import OrmBase
from sqlalchemy.inspection import inspect
from datetime import datetime


class TswStatsEncoder(json.JSONEncoder):
    """A custom JSON encoder with support for Decimal and SqlAlchemy models."""

    def default(self, obj):
        """Per JSONEncoder, do JSON encoding."""
        if isinstance(obj, d.Decimal):
            return self.encodeDecimal(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, OrmBase):
            return self.encodeModel(obj)
        return json.JSONEncoder.default(self, obj)

    def encodeDecimal(self, obj):
        """Do the work of encoding a Decimal."""
        if int(obj) == obj:
            return int(obj)
        else:
            return '{:.2f}'.format(obj)

    def encodeModel(self, obj):
        """Do the work of encoding a SqlAlchemy Model."""
        inspct = inspect(obj)
        rv = {'__class__': type(obj).__name__}
        for colName in inspct.mapper.column_attrs.keys():
            val = inspct.attrs[colName].value
            rv[colName] = val
        return rv
