"""Characters that participate in multiple combats.

Essentially a view over Combatants, this provides a way for users to start
looking at how a character's performance changes over time.
"""

from sqlalchemy import select, func, Index
from sqlalchemy.orm import relationship
from .combatant import Combatant
from .view import create_mat_view, MaterializedView

__all__ = ('Character', '__author__', '__copyright__', '__license__',
           '__version__')
__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


class Character(MaterializedView):
    """The Character view of Combatant data.

    Represents a single character, participating in many Encounters.
    """

    __table__ = create_mat_view(
        "character_mview",
        select([
            Combatant.name.label('name'),
            func.min(Combatant.starttime).label('firstSeen'),
            func.max(Combatant.endtime).label('lastSeen'),
            func.sum(Combatant.duration).label('seenTime'),
            func.sum(Combatant.damage).label('damage'),
            func.sum(Combatant.healed).label('healed'),
            func.sum(Combatant.damagetaken).label('damageTaken'),
            func.sum(Combatant.kills).label('kills')
        ]).group_by(Combatant.name).order_by(Combatant.name)
    )

    combatants = relationship(
        'Combatant',
        backref='character',
        primaryjoin='Character.name==Combatant.name',
        foreign_keys='Combatant.name'
        )

    attackUsages = relationship(
        'AttackType',
        backref='attackerCharacter',
        primaryjoin='Character.name==AttackType.attackerName',
        foreign_keys='AttackType.attackerName'
        )

    hitSummaries = relationship(
        'AttackType',
        backref='victimCharacter',
        primaryjoin='Character.name==AttackType.victimName',
        foreign_keys='AttackType.victimName'
        )

    outSwings = relationship('Swing',
                             backref='attackerChar',
                             primaryjoin="Swing.attackerName==Character.name",
                             foreign_keys='Swing.attackerName')

    inSwings = relationship('Swing',
                            backref='victimChar',
                            primaryjoin="Swing.victimName==Character.name",
                            foreign_keys='Swing.victimName')

    def __repr__(self):
        return "<Character {!r}>".format(self.name)


Index('idx_character_name', Character.name, unique=True)
