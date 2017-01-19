"""All encounter-related routes.

If the user wants to browse/search encounters, or look at the overview for a
particular encounter, they'll probably want one of these routes.
"""

from bottle import route, template
from db import Encounter, Combatant, Swing
from datetime import datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


@route('/encounter')
def listEncounters(dbSession):
    """List all the encounters, possibly providing search functionality."""
    # TODO: Pagination, sorting, custom date range.
    recentEncounters = dbSession.query(Encounter) \
        .filter(Encounter.endtime > (datetime.now() - timedelta(days=33))) \
        .order_by(Encounter.endtime.desc()).limit(15).all()
    return template('encounterList', encounters=recentEncounters)


@route('/encounter/<encounterId>')
def encounterInfo(encounterId, dbSession):
    """Provide an overview of a given encounter."""
    try:
        enc = dbSession.query(Encounter).filter(
            Encounter.encid == encounterId
            ).one()
    except NoResultFound:
        return "No result found for that encounter. Hit the back button."
    except MultipleResultsFound:
        return "Given encounter ID is not unique. Data cannot be viewed."
    allies = dbSession.query(Combatant).filter(
        Combatant.encid == encounterId,
        Combatant.ally == 'T'
    ).all()
    foes = dbSession.query(Combatant).filter(
        Combatant.encid == encounterId,
        Combatant.ally == 'F'
    ).all()
    topAlliedAttacks = dbSession.query(Swing).filter(
        Swing.encid == encounterId,
        Swing.swingtype == 1,
        Swing.attackerName in (a.name for a in allies)
    ).order_by(Swing.damage.desc()).limit(10)
    topAlliedHeals = dbSession.query(Swing).filter(
        Swing.encid == encounterId,
        Swing.swingtype == 3,
        Swing.attackerName in (a.name for a in allies)
    ).order_by(Swing.damage.desc()).limit(10)
    topEnemyAttacks = dbSession.query(Swing).filter(
        Swing.encid == encounterId,
        Swing.swingtype == 1,
        Swing.attackerName in (a.name for a in foes)
    ).order_by(Swing.damage.desc()).limit(10)
    topEnemyHeals = dbSession.query(Swing).filter(
        Swing.encid == encounterId,
        Swing.swingtype == 3,
        Swing.attackerName in (a.name for a in foes)
    ).order_by(Swing.damage.desc()).limit(10)
    return template('encounterDetail', encounter=enc, allies=allies, foes=foes,
                    alliedHits=topAlliedAttacks, alliedHeals=topAlliedHeals,
                    foeHits=topEnemyAttacks, foeHeals=topEnemyHeals)


@route('/encounter/<encounterId>/d/<damageTypeId>')
def encounterDamageTypeInfo(encounterId, damageTypeId, dbSession):
    """For a given encounter, look at a particular group of abilities."""
    pass


@route('/encounter/<encounterId>/a/<attackTypeId>')
def encounterAttackTypeInfo(encounterId, attackTypeId, dbSession):
    """For an encounter, look at how a particular ability performed."""
    pass


@route('/data/encounter')
def queryEncounterTable(dbSession):
    """Return JSON describing the results of an arbitrary query/search."""
    pass
