"""
This module centralizes all of the DB-related code.

DB-related code includes models describing the DB, custom types for making
the DB easier to work with, and procedures for common queries needed in
multiple places.

One-off queries only needed in one place are welcome to use the import the
models and query them directly, rather than going through query functions.

Any function retrieving data in this module should return a query, not a list
of results. Returning a query allows for further refining of the dataset
before sending the query to SQL.
"""

from db.models import AttackType, Combatant, Encounter, DamageType, Swing
from db.models import OrmBase
from db.dataRequest import DataRequest
from db.genericQuery import getDataTable

__all__ = ('AttackType', 'Combatant', 'Encounter', 'DamageType', 'Swing',
           'OrmBase', '__author__', '__copyright__', '__license__',
           '__version__', 'DataRequest', 'getDataTable', 'Character')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"
