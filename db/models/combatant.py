from .sacommon import Base
from sqlalchemy import Column, BigInteger, String, CHAR, Integer, SMALLINT
from sqlalchemy import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

__all__ = ['Combatant']


class Combatant(Base):
    __tablename__ = 'combatant_table'

    # Columns
    encid = Column(CHAR(8))
    ally = Column(CHAR(1))
    name = Column(String(64))
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
    healstaken = Column(BigInteger)
    damagetaken = Column(BigInteger)
    deaths = Column(Integer)
    tohit = Column(DOUBLE_PRECISION)
    critdamperc = Column(String(8))
    crithealperc = Column(String(8))
    aegisdmg = Column(Integer)
    combatantid = Column(BigInteger, primary_key=True)

    def __repr__(self):
        return "<Combatant {!r} - {!r} -  Ally: {!r}>" \
            .format(self.encounter, self.name, self.ally)
