from .sacommon import Base
from sqlalchemy import Column, BigInteger, String, CHAR, Integer, SMALLINT
from sqlalchemy import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import relationship

__all__ = ['Encounter']


class Encounter(Base):
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
