"""All encounter-related routes.

If the user wants to browse/search encounters, or look at the overview for a
particular encounter, they'll probably want one of these routes.
"""

from bottle import route, template, request
from db import Encounter, Combatant, Swing
from datetime import datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.dialects import postgresql
from sqlalchemy.inspection import inspect

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


@route('/encounter')
def listEncounters(dbSession):
    """List all the encounters, possibly providing search functionality."""
    # TODO: custom date range.
    recentEncounters = dbSession.query(Encounter) \
        .filter(Encounter.endtime > (datetime.now() - timedelta(days=33))) \
        .order_by(Encounter.endtime.desc()).limit(25).all()
    # TODO: Move below to template, e.g. objectList.tpl & encounterList.tpl
    colConfig = [
        {'attr': 'zone', 'name': 'Zone', 'class': 'all'},
        {'attr': 'title', 'name': 'Encounter', 'class': 'all'},
        {'attr': 'starttime', 'name': 'Start Time', 'class': 'all'},
        {'attr': 'duration', 'name': 'Duration (s)', 'class': 'min-md'},
        {'attr': 'damage', 'name': 'Total Damage',
         'formatter': '{:,.2f}'.format, 'class': 'min-sm'},
        {'attr': 'encdps', 'name': 'Encounter DPS',
         'formatter': '{:,.2f}'.format, 'class': 'all'},
        {'attr': 'kills', 'name': 'Kills', 'formatter': '{:,.0f}'.format,
         'class': 'min-md'},
        {'attr': 'deaths', 'name': 'Deaths', 'class': 'min-md'},
        {'attr': 'aegisdmg', 'name': 'AEGIS Damage',
         'formatter': '{:,.0f}'.format, 'class': 'min-lg'}
    ]
    return template('objectList', objects=recentEncounters, columns=colConfig,
                    urlgen=(lambda obj: '/encounter/{}'.format(obj.encid)),
                    urlcol='title', ajaxurl='/data/encounter')


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
    # TODO: Move JSON parsing into generic route
    # TODO: Move DB-specific stuff into db module
    jsonD = request.json
    draw = int(jsonD['draw'])
    limit = int(jsonD['length'])
    if limit > 500:
        return {'draw': draw, 'error': 'Too many records requested.'}
    offset = int(jsonD['start'])

    # TODO: Figure out how to sort-of do search.
    searchVal = jsonD['search']['value']  #noqa
    searchIsRegex = jsonD['search']['regex']  #noqa

    # Sorting
    colList = [c['data'] for c in jsonD['columns']]
    orderData = jsonD['order']
    orderData = [(colList[o['column']], o['dir']) for o in orderData]
    cols = inspect(Encounter).c
    orderData = [cols[col].desc() if direct == 'desc'
                 else cols[col] for (col, direct) in orderData]
    # orderData now looks like [(attrName, direction), ...]
    # TODO: Searching, as above.
    objs = dbSession.query(Encounter).order_by(*orderData)
    return {
        'draw': draw,
        'recordsFiltered': objs.count(),
        'data': [{
            col: inspect(o).attrs[col].value
            for col in colList} for o in objs.offset(offset)
                .limit(limit).all()],
        'recordsTotal': dbSession.query(Encounter).count(),
        }
