import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from getpass import getpass

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
