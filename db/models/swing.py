from .sacommon import Base
from sqlalchemy import Column, BigInteger, String, CHAR, SMALLINT, TIMESTAMP

__all__ = ['Swing', '__author__', '__copyright__', '__license__',
           '__version__']
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


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
