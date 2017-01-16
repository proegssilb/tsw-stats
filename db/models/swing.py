from .sacommon import Base
from sqlalchemy import Column, BigInteger, String, CHAR, Integer, SMALLINT
from sqlalchemy import TIMESTAMP, Numeric

__all__ = ['Swing']


class Swing(Base):
    __tablename__ = 'swing_table'

    # Columns
    encid = Column(CHAR(8))
    stime = Column(TIMESTAMP)
    attackerName = Column('attacker', String(64))
    swingtype = Column(SMALLINT)
    attacktype = Column(String(64))
    damagetype = Column(String(64))
    victimName = Column('victim', String(64))
    damage = Column(BigInteger)
    damagestring = Column(String(128))
    critical = Column(CHAR(1))
    special = Column(String(64))
    swingid = Column(BigInteger, primary_key=True)

    # Methods

    def __repr__(self):
        return "<Swing {!r} - {!r} - {!r} - {!r}".format(self.encounter,
                                                         self.attacker,
                                                         self.victim,
                                                         self.damage)
