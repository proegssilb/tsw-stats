"""
This module contains all the page-generating functions/classes/etc.

Think of this module as the Controller in MVC, where the "db" module is the
Model, and the Templates are the Controller.
"""

from pages.simple import index, static, fonts
from pages.encounterRoutes import listEncounters, encounterInfo
from pages.encounterRoutes import encounterAttackTypeInfo
from pages.encounterRoutes import encounterDamageTypeInfo, queryEncounterTable
from pages.characterRoutes import queryCharacterTable, listCharacters
from pages.characterRoutes import characterOverview

__all__ = (index, listEncounters, encounterInfo, encounterAttackTypeInfo,
           encounterDamageTypeInfo, queryEncounterTable, static, fonts,
           queryCharacterTable, listCharacters, characterOverview)

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"
