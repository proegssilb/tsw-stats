from .sacommon import Base
from sqlalchemy import Column, BigInteger, String, CHAR, Integer, SMALLINT
from sqlalchemy import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

__all__ = ['DamageType']


class DamageType(Base):
    __tablename__ = 'damagetype_table'

    # Columns
    encid = Column(CHAR(8))
    combatant = Column(String(64))
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
    #attackTypeJoinCond = "and_({})".format(", ".join(
    #    "AttackType.encid==DamageType.encid",
    #    "or_(DamageType.combatant==AttackType.attacker," + \
    #        "DamageType.combatant==AttackType.victim)",
    #    # TODO: DamageType.grouping contains AttackType.swingtype
    #    ))
    #attackTypes = relationship('AttackType',
    #                           backref='damageCategory',
    #                           primaryjoin=attackTypeJoinCond,
    #                           foreign_keys='AttackType.encid')
    

    # Methods
    def __repr__(self):
        return "<DamageType {!r} - {!r} - {!r}>".format(self.encounter,
                                                        self.combatant,
                                                        self.typeName)
