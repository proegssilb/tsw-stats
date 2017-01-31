"""A module for the Combatant class."""

from .sacommon import OrmBase
from sqlalchemy import Column, BigInteger, String, CHAR, Integer
from sqlalchemy import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

__all__ = ('Combatant', '__author__', '__copyright__', '__license__',
           '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


class Combatant(OrmBase):
    """Describes a participant in an Encounter.

    Combatants can be either friend or foe, can be hit by a Swing, and can
    attack other combatants, causing a Swing.
    """

    __tablename__ = 'combatant_table'

    # Columns
    encid = Column(CHAR(8), index=True)
    ally = Column(CHAR(1))
    name = Column(String(64), index=True)
    starttime = Column(TIMESTAMP)
    endtime = Column(TIMESTAMP)
    duration = Column(Integer)
    damage = Column(BigInteger)
    damageperc = Column(String(4))
    kills = Column(Integer)
    healed = Column(BigInteger)
    healedperc = Column(String(4))
    critheals = Column(Integer)
    heals = Column(Integer)
    dps = Column(Numeric)
    encdps = Column(Numeric)
    enchps = Column(Numeric)
    hits = Column(Integer)
    crithits = Column(Integer)
    blocked = Column(Integer)
    misses = Column(Integer)
    swings = Column(Integer)
    healstaken = Column(BigInteger)
    damagetaken = Column(BigInteger)
    deaths = Column(Integer)
    tohit = Column(DOUBLE_PRECISION)
    critdamperc = Column(String(8))
    crithealperc = Column(String(8))
    aegisdmg = Column(Integer)
    combatantid = Column(BigInteger, primary_key=True)

    # Relationships
    attackSummaries = relationship(
        'AttackType',
        backref='attacker',
        primaryjoin="and_({})".format(', '.join([
            'Combatant.encid==AttackType.encid',
            'Combatant.name==AttackType.attackerName'
            ])),
        foreign_keys='AttackType.encid, AttackType.attackerName'
        )

    hitSummaries = relationship(
        'AttackType',
        backref='victim',
        primaryjoin="and_({})".format(', '.join([
            'Combatant.encid==AttackType.encid',
            'Combatant.name==AttackType.victimName'
            ])),
        foreign_keys='AttackType.encid, AttackType.victimName'
        )

    outSwings = relationship('Swing',
                             backref='attacker',
                             primaryjoin="and_(Swing.encid==Combatant.encid," +
                             " Swing.attackerName==Combatant.name)",
                             foreign_keys='Swing.encid, Swing.attackerName')

    inSwings = relationship('Swing',
                            backref='victim',
                            primaryjoin="and_(Swing.encid==Combatant.encid, " +
                            "Swing.victimName==Combatant.name)",
                            foreign_keys='Swing.encid, Swing.victimName')

    swingCategories = relationship(
        'DamageType',
        backref='combatant',
        primaryjoin="and_({})".format(', '.join([
            'Combatant.encid==DamageType.encid',
            'Combatant.name==DamageType.combatantName'
            ])),
        foreign_keys='DamageType.encid, DamageType.combatantName'
    )

    def __repr__(self):
        return "<Combatant {!r} - {!r} -  Ally: {!r}>" \
            .format(self.encounter, self.name, self.ally)
