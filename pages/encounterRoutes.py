"""All encounter-related routes.

If the user wants to browse/search encounters, or look at the overview for a
particular encounter, they'll probably want one of these routes.
"""

from bottle import route, template, request, HTTPError
from db import Encounter, Combatant, Swing, DataRequest, getDataTable
from datetime import datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.dialects import postgresql

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.1"
__all__ = ('listEncounters', 'encounterInfo', 'encounterCombatantPerformance',
           'encounterDamageTypeInfo', 'encounterAttackTypeInfo',
           'queryEncounterTable')


@route('/encounter')
def listEncounters(dbSession):
    """List all the encounters, possibly providing search functionality."""
    # This query only matters for people without JavaScript.
    recentEncounters = dbSession.query(Encounter) \
        .filter(Encounter.endtime > (datetime.now() - timedelta(days=33))) \
        .order_by(Encounter.endtime.desc()).limit(25).all()
    return template('encounterList', encounters=recentEncounters)


@route('/encounter/<encounterId>')
@route('/encounter/<encounterId>/')
def encounterInfo(encounterId, dbSession):
    """Provide an overview of a given encounter."""
    if (not encounterId.isalnum()):
        raise HTTPError(404)
    try:
        enc = dbSession.query(Encounter).filter(
            Encounter.encid == encounterId
            ).one()
    except NoResultFound:
        raise HTTPError(404)
    except MultipleResultsFound:
        raise HTTPError(404)
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
        Swing.attackerName.in_(a.name for a in allies)
    ).order_by(Swing.damage.desc()).limit(10)
    print(
        str(topAlliedAttacks.statement.compile(dialect=postgresql.dialect()))
        )
    topAlliedAttacks = topAlliedAttacks.all()
    topAlliedHeals = dbSession.query(Swing).filter(
        Swing.encid == encounterId,
        Swing.swingtype == 3,
        Swing.attackerName.in_(a.name for a in allies)
    ).order_by(Swing.damage.desc()).limit(10).all()
    topEnemyAttacks = dbSession.query(Swing).filter(
        Swing.encid == encounterId,
        Swing.swingtype == 1,
        Swing.attackerName.in_(a.name for a in foes)
    ).order_by(Swing.damage.desc()).limit(10).all()
    topEnemyHeals = dbSession.query(Swing).filter(
        Swing.encid == encounterId,
        Swing.swingtype == 3,
        Swing.attackerName.in_(a.name for a in foes)
    ).order_by(Swing.damage.desc()).limit(10).all()
    return template('encounterDetail', encounter=enc, allies=allies, foes=foes,
                    alliedHits=topAlliedAttacks, alliedHeals=topAlliedHeals,
                    foeHits=topEnemyAttacks, foeHeals=topEnemyHeals)


@route('/encounter/<encounterId>/c/<combatantName>')
def encounterCombatantPerformance(encounterId, combatantName, dbSession):
    """For a given encounter, how did a particular character do in detail."""
    return template('encounterCombatant')


@route('/encounter/<encounterId>/d/<damageTypeId>')
def encounterDamageTypeInfo(encounterId, damageTypeId, dbSession):
    """For a given encounter, look at a particular group of abilities."""
    pass


@route('/encounter/<encounterId>/a/<attackTypeId>')
def encounterAttackTypeInfo(encounterId, attackTypeId, dbSession):
    """For an encounter, look at how a particular ability performed."""
    return template('encounterAttackType')


@route('/data/encounter')
@route('/data/encounter', method="POST")
def queryEncounterTable(dbSession):
    """Return JSON describing the results of an arbitrary query/search."""
    dataReq = DataRequest(Encounter, request.json)
    return getDataTable(dataReq, dbSession)


def debugQuery(q):
    """Quickly print a compiled query for debugging."""
    print(q.compile(dialect=postgresql.dialect()))


@route('/encounter/<encounterId>/graph')
def encounterGraph(encounterId, dbSession):
    # WARNING: VALIDATION PREVENTING A SQL INJECTION
    if not encounterId.isalnum():
        raise HTTPError(404)
    allied = request.params['allied'] in (True, 'True', 'true', 't', 1, 'T')
    attackTypeId = int(request.params['attackTypeId'])
    allied = 'T' if allied else 'F'
    # END VALIDATION

    combatants = dbSession.query(Combatant.name).filter(
        Combatant.encid == encounterId,
        Combatant.ally == allied
        ).group_by(
            Combatant.name
        ).order_by(Combatant.name)
    combatantNameList = tuple(n for (n,) in combatants.all())

    # WARNING: SQL INJECTION RISK FOLLOWS
    # The alternative is roundabout, slow, ugly, and broken.
    qRaw = """SELECT *
    FROM crosstab('SELECT sw.stime, sw.attacker, SUM(sw.damage)
                    FROM swing_table sw
                        JOIN combatant_table cm
                            ON sw.attacker = cm.name
                                AND sw.encid = cm.encid
                    WHERE sw.encid =''{0}''
                        AND sw.swingtype = {1}
                        AND cm.ally = ''{3}''
                    GROUP BY sw.stime, sw.attacker
                    ORDER BY sw.stime ASC, sw.attacker ASC',
                 'SELECT sw.attacker
                  FROM swing_table sw
                      JOIN combatant_table cm
                          ON sw.attacker = cm.name
                              AND sw.encid = cm.encid
                  WHERE sw.encid=''{0}''
                    AND sw.swingtype={1}
                    AND cm.ally = ''{3}''
                  GROUP BY sw.attacker
                  ORDER BY sw.attacker ASC')
      AS (
            stime timestamp,
            {2}
        )"""
    asList = ',\n'.join(('"{}" bigint'.format(c) for c in combatantNameList))
    timelineQuery = qRaw.format(encounterId, attackTypeId, asList, allied)
    yield 'Swing Time,' + ','.join(combatantNameList) + '\n'
    yield from (','.join(str('NaN' if v is None else v) for (k, v) in
                         row.items())
                + '\n' for row in dbSession.execute(timelineQuery))
