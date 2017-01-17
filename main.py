"""The main entrypoint for this project."""

import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from getpass import getpass
import sys

__author__ = "David Bliss"
__copyright__ = "Copyright (C) 2017 David Bliss"
__license__ = "Apache-2.0"
__version__ = "1.0"


print(sys.version)
print(sys.version_info)

engine = create_engine(
    'postgresql://postgres:{}@localhost/ACT'.format(getpass())
    )
Session = sessionmaker(bind=engine)
sess = Session()
print(repr(sess.query(db.Encounter).first()))
print(repr(sess.query(db.Combatant).first()))
print(repr(sess.query(db.AttackType).first()))
print(repr(sess.query(db.DamageType).first()))
print(repr(sess.query(db.Swing).first()))
