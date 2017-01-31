"""A module for the AttackType class."""

from .sacommon import OrmBase
from sqlalchemy import Column, BigInteger, String, CHAR, Integer, SMALLINT
from sqlalchemy import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

__all__ = ('AttackType', '__author__', '__copyright__', '__license__',
           '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


class AttackType(OrmBase):
    """A grouping of Swings based off of the ability used. SqlAlchemy class.

    Each time a Swing is performed, it uses a particular ability. Each ability
    could be used multiple times in the same Encounter, generating multiple
    Swings of the same ability. AttackType collects those Swings together to
    allow comparing them against each other, finding crit rate, and so on.
    """

    __tablename__ = 'attacktype_table'

    # Columns
    encid = Column(CHAR(8), index=True)
    attackerName = Column('attacker', String(64))
    victimName = Column('victim', String(64))
    swingtype = Column(SMALLINT)
    attacktype = Column('type', String(64))
    starttime = Column(TIMESTAMP, index=True)
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
    resist = Column(String(64))
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
    attackTypeId = Column('attacktypeid', BigInteger, primary_key=True)

    # Relationships
    __swingJoinCond = " & ".join(
        ["(AttackType.encid == Swing.encid)",
         " | ".join([
             "(AttackType.attackerName == Swing.attackerName)",
             "(AttackType.victimName == Swing.victimName)"
             ]),
         "(Swing.attacktype == AttackType.attacktype)"
         ])
    attacks = relationship('Swing',
                          backref='attackSummary',
                          primaryjoin=__swingJoinCond,
                          foreign_keys='Swing.encid, Swing.attackerName, ' +
                          'Swing.victimName, Swing.attacktype')

    # Methods
    def __repr__(self):
        return "<AttackType {!r} - {!r} - {!r}>".format(self.encounter,
                                                        self.attackerName,
                                                        self.attacktype)
