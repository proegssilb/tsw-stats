
"""
A listing of all the 'simple' pages that don't require their own module.

This may include pages that return the results of a query, allowing a template
to do formatting, or it may include error pages, or other pages that don't
need their own module.
"""

from bottle import route, template, static_file
from db import Encounter
from datetime import datetime, timedelta

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


@route('/')
def index(dbSession):
    """The index route."""
    recentEncounters = dbSession.query(Encounter) \
        .filter(Encounter.endtime > (datetime.now() - timedelta(days=1))) \
        .order_by(Encounter.endtime.desc()).limit(15).all()

    topDamageEncounters = dbSession.query(Encounter) \
        .filter(Encounter.endtime > (datetime.now() - timedelta(days=33))) \
        .order_by(Encounter.encdps.desc()).limit(15).all()

    hardestEncounters = dbSession.query(Encounter) \
        .filter(Encounter.endtime > (datetime.now() - timedelta(days=33))) \
        .order_by(Encounter.deaths.desc()).limit(15).all()

    return template('index', recent=recentEncounters, dmg=topDamageEncounters,
                    hard=hardestEncounters)


@route('/static/<filename>')
def static(filename):
    """Serve static files."""
    return static_file(filename, root='./static')
