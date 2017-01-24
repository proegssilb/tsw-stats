"""The main entrypoint for this project."""

import db
import pages #noqa ; This import is done for the side effects.
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from bottle.ext import sqlalchemy as bsa
from bottle import install, run, JSONPlugin
from jsonEncoder import TswStatsEncoder
import os
import argh
import json

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.1"


def initEnv(envFile):
    """Set environment variables based on a config file."""
    if envFile != '' and envFile is not None:
        with open(envFile) as envVars:
            for line in envVars:
                var, val = line.split('=', 1)
                var = var.strip()
                val = val.strip()
                os.environ[var] = val


def initDb():
    """Initialize SQL access."""
    dbConnectionString = os.environ['DBCONNECTION']
    return create_engine(dbConnectionString)


def getSession(engine=None):
    """Return a session for the given engine."""
    if engine is None:
        engine = initDb()
    Session = sessionmaker(bind=engine)
    return Session()


def replaceJsonPlugin():
    """Patch bottle's default JSON handling to support our custom object."""
    install(JSONPlugin(
        json_dumps=lambda body: json.dumps(body, cls=TswStatsEncoder)
        ))


@argh.arg('--envFile', help="A file containing environment variable settings.")
def main(envFile=''):
    """Run the tsw-stats server.

    tsw-stats does not support much configuration, so it is configured via
    environment variables:
      - $PORT to set the listening port
      - $DBCONNECTION to set the SQL Connection String (contains a password!)
      - $HOST to control which IP Address to listen on
    """
    initEnv(envFile)
    port = os.environ['PORT']
    host = os.environ['HOST']
    engine = initDb()
    plugin = bsa.Plugin(
        engine,
        db.OrmBase.metadata,
        keyword='dbSession'  # Argument name to views
    )

    install(plugin)
    replaceJsonPlugin()
    run(host=host, port=port, debug=True)


parser = argh.ArghParser()
argh.set_default_command(parser, main)

if __name__ == '__main__':
    parser.dispatch()
