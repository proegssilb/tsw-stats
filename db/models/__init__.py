"""
This module collects all the classes representing the model of the DB.

The model is based on SqlAlchemy's ORM library, and so the DB is modeled
via classes.
"""

from db.models.attacktype import AttackType
from db.models.combatant import Combatant
from db.models.encounter import Encounter
from db.models.damagetype import DamageType
from db.models.swing import Swing

__all__ = ('AttackType', 'Combatant', 'Encounter', 'DamageType', 'Swing',
           '__author__', '__copyright__', '__license__', '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"
