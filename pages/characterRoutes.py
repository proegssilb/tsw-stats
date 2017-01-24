"""All character-related routes.

If the user wants to browse/search characters, or look at how a character has
improved over time, they'll likely want something from here.
"""

from datetime import datetime, timedelta
from bottle import route, request, template, HTTPResponse
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from db import Character, DataRequest, getDataTable


@route('/character')
def listCharacters(dbSession):
    """List all the characters, possibly providing search functionality."""
    # This query only matters for people without JavaScript.
    recentCharacters = dbSession.query(Character) \
        .filter(Character.lastSeen > (datetime.now() - timedelta(days=33))) \
        .order_by(Character.lastSeen.desc()).limit(25).all()
    return template('characterList', characters=recentCharacters)


@route('/character/<charName>')
def characterOverview(charName, dbSession):
    """Provide an overview of how a character has been doing."""
    print(charName)
    if not charName.isalnum():
        raise HTTPResponse(status=404)
    character = None
    try:
        character = dbSession.query(Character).filter(
            Character.name == charName).one()
    except NoResultFound:
        raise HTTPResponse(status=404)
    except MultipleResultsFound:
        raise HTTPResponse(status=500)
    else:
        return template('characterOverview', character=character)


@route('/data/character')
@route('/data/character', method="POST")
def queryCharacterTable(dbSession):
    """Return JSON describing the results of an arbitrary query/search."""
    dataReq = DataRequest(Character, request.json)
    return getDataTable(dataReq, dbSession)
