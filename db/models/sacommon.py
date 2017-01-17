"""A module for centralizing some common SqlAlchemy code for the models.

The common code includes, of course, the Declarative Base, but we should also
define any automatic conventions here as well.
"""

from sqlalchemy.ext.declarative import declarative_base

__all__ = ('OrmBase', '__author__', '__copyright__', '__license__',
           '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


OrmBase = declarative_base()
