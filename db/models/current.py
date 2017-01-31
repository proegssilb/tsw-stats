"""A module for the obscure 'current_table' table."""

from .sacommon import OrmBase
from sqlalchemy import Column, BigInteger, String, CHAR, Integer
from sqlalchemy import Index, NUMERIC
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TIMESTAMP

__all__ = ('Current', '__author__', '__copyright__', '__license__',
           '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"

class Current(OrmBase):
    """Advanced Combat Tracker uses this table. tsw-stats doesn't."""
    __tablename__ = 'current_table'

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
    dps = Column(NUMERIC)
    encdps = Column(NUMERIC)
    enchps = Column(NUMERIC)
    hits = Column(Integer)
    crithits = Column(Integer)
    blocked = Column(Integer)
    misses = Column(Integer)
    swings = Column(Integer)
    healstaken = Column(BigInteger)
    damagetaken = Column(BigInteger)
    deaths = Column(Integer)
    tohit = Column(DOUBLE_PRECISION(53))
    critdamperc = Column(String(8))
    crithealperc = Column(String(8))
    aegisdmg = Column(Integer)
    currentid = Column(BigInteger, primary_key=True)
