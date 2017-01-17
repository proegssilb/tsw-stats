"""A module for the Encounter class."""

from .sacommon import OrmBase
from sqlalchemy import Column, BigInteger, String, CHAR, TIMESTAMP, Integer
from sqlalchemy import Numeric
from sqlalchemy.orm import relationship

__all__ = ('Encounter', '__author__', '__copyright__', '__license__',
           '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


class Encounter(OrmBase):
    """A period of time and location where Combatants combatted.

    An Encounter is a container for both Combatants, the characters, and
    Swings, what the Combatants did. The main data it provides is where and
    when, but there is some overview info available as well.
    """

    __tablename__ = 'encounter_table'

    # Columns
    encid = Column(CHAR(8))
    title = Column(String(64))
    starttime = Column(TIMESTAMP)
    endtime = Column(TIMESTAMP)
    duration = Column(Integer)
    damage = Column(BigInteger)
    encdps = Column(Numeric)
    zone = Column(String(64))
    kills = Column(Integer)
    deaths = Column(Integer)
    aegisdmg = Column(Integer)
    encounterid = Column(BigInteger, primary_key=True)

    # Relationships
    combatants = relationship('Combatant',
                              backref='encounter',
                              primaryjoin="Combatant.encid==Encounter.encid",
                              foreign_keys='Combatant.encid')

    attackTypes = relationship('AttackType',
                               backref='encounter',
                               primaryjoin="AttackType.encid==Encounter.encid",
                               foreign_keys='AttackType.encid')

    damageTypes = relationship('DamageType',
                               backref='encounter',
                               primaryjoin="DamageType.encid==Encounter.encid",
                               foreign_keys='DamageType.encid')

    swings = relationship('Swing',
                          backref='encounter',
                          primaryjoin="Swing.encid==Encounter.encid",
                          foreign_keys='Swing.encid')

    # Methods
    def __repr__(self):
        return "<Encounter {!r} {!r}>".format(self.title, str(self.starttime))
