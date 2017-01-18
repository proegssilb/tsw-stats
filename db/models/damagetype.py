"""A module for the DamageType class."""

from .sacommon import OrmBase
from sqlalchemy import Column, BigInteger, String, CHAR, Integer
from sqlalchemy import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
# from sqlalchemy.orm import relationship # We'll be needing this soon.

__all__ = ('DamageType', '__author__', '__copyright__', '__license__',
           '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


class DamageType(OrmBase):
    """A class representing the DamageType table from ACT.

    Damage Types collect Swings into broad categorizations, such as
    "Outgoing damage". This is in contrast to Attack Types, which group Swings
    into much narrower categorizations based on the actual ability used.
    """

    __tablename__ = 'damagetype_table'

    # Columns
    encid = Column(CHAR(8))
    combatantName = Column('combatant', String(64))
    grouping = Column(String(92))
    typeName = Column('type', String(64))
    starttime = Column(TIMESTAMP)
    endtime = Column(TIMESTAMP)
    duration = Column(Integer)
    damage = Column(BigInteger)
    encdps = Column(Numeric)
    chardps = Column(Numeric)
    dps = Column(Numeric)
    average = Column(Numeric)
    median = Column(BigInteger)
    minhit = Column(BigInteger)
    maxhit = Column(BigInteger)
    hits = Column(Integer)
    crithits = Column(Integer)
    blocked = Column(Integer)
    misses = Column(Integer)
    swings = Column(Integer)
    tohit = Column(DOUBLE_PRECISION)
    averagedelay = Column(DOUBLE_PRECISION)
    critperc = Column(String(8))
    glancehits = Column(Integer)
    glanceperc = Column(String(32))
    penetrationhits = Column(Integer)
    penetrationperc = Column(String(32))
    blockedhits = Column(Integer)
    blockedperc = Column(String(32))
    aegishits = Column(Integer)
    aegisdmg = Column(Integer)
    aegismismatch = Column(Integer)
    aegismismatchperc = Column(String(32))
    damagetypeid = Column(BigInteger, primary_key=True)

    # Relationships
    # attackTypeJoinCond = "and_({})".format(", ".join(
    #    "AttackType.encid==DamageType.encid",
    #    "or_(DamageType.combatantName==AttackType.attacker," + \
    #        "DamageType.combatantName==AttackType.victim)",
    #    # TODO: DamageType.grouping contains AttackType.swingtype
    #    ))
    # attackTypes = relationship('AttackType',
    #                           backref='damageCategory',
    #                           primaryjoin=attackTypeJoinCond,
    #                           foreign_keys='AttackType.encid')

    # Methods
    def __repr__(self):
        return "<DamageType {!r} - {!r} - {!r}>".format(self.encounter,
                                                        self.combatantName,
                                                        self.typeName)
