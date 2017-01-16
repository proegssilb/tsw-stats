from .sacommon import Base
from sqlalchemy import Column, BigInteger, String, CHAR, Integer, SMALLINT
from sqlalchemy import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

__all__ = ['AttackType', '__author__', '__copyright__', '__license__',
           '__version__']
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


class AttackType(Base):
    __tablename__ = 'attacktype_table'

    # Columns
    encid = Column(CHAR(8))
    attacker = Column(String(64))
    victim = Column(String(64))
    swingtype = Column(SMALLINT)
    attacktype = Column('type', String(64))
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
             "(AttackType.attacker == Swing.attackerName)",
             "(AttackType.victim == Swing.victimName)"
             ]),
         "(Swing.attacktype == AttackType.attacktype)"
         ])
    swings = relationship('Swing',
                          backref='attackSummary',
                          primaryjoin=__swingJoinCond,
                          foreign_keys='Swing.encid, Swing.attackerName, ' +
                          'Swing.victimName, Swing.attacktype')

    # Methods
    def __repr__(self):
        return "<AttackType {!r} - {!r} - {!r}>".format(self.encounter,
                                                        self.attacker,
                                                        self.attacktype)
