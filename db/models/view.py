"""A module for supporting Materialized Views in SQLAlchemy.

Based on https://github.com/jeffwidman/sqlalchemy-postgresql-materialized-views
"""
# pylama:skip=1

# materialized_view_factory.py
# example for use with Flask-SQLAlchemy

# Accompanying blog post:
# http://www.jeffwidman.com/blog/847/

# Many thanks to Mike Bayer (@zzzeek) for his help.

from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement, PrimaryKeyConstraint
from sqlalchemy import MetaData, Table, Column, event, inspect, DDL
from .sacommon import OrmBase


class CreateMaterializedView(DDLElement):
    def __init__(self, name, selectable):
        self.name = name
        self.selectable = selectable


@compiler.compiles(CreateMaterializedView)
def compile(element, compiler, **kw):
    # Could use "CREATE OR REPLACE MATERIALIZED VIEW..."
    # but I'd rather have noisy errors
    return 'CREATE MATERIALIZED VIEW %s AS %s' % (
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
        )


def create_mat_view(name, selectable, metadata=OrmBase.metadata):
    _mt = MetaData()  # temp metadata just for initial Table object creation
    t = Table(name, _mt)  # the actual mat view class is bound to db.metadata
    for c in selectable.c:
        t.append_column(Column(c.name, c.type, primary_key=c.primary_key))

    if not (any([c.primary_key for c in selectable.c])):
        t.append_constraint(PrimaryKeyConstraint(*[c.name for c in selectable.c]))

    event.listen(
        metadata, 'after_create',
        CreateMaterializedView(name, selectable)
        )

    @event.listens_for(metadata, 'after_create')
    def create_indexes(target, connection, **kw):
        for idx in t.indexes:
            idx.create(connection)

    event.listen(
        metadata, 'before_drop',
        DDL('DROP MATERIALIZED VIEW IF EXISTS ' + name)
        )
    return t


def refresh_mat_view(name, session, concurrently):
    # since session.execute() bypasses autoflush, must manually flush in order
    # to include newly-created/modified objects in the refresh
    session.flush()
    _con = 'CONCURRENTLY ' if concurrently else ''
    session.execute('REFRESH MATERIALIZED VIEW ' + _con + name)


def refresh_all_mat_views(concurrently=True):
    '''Refreshes all materialized views. Currently, views are refreshed in
    non-deterministic order, so view definitions can't depend on each other.'''
    mat_views = inspect(db.engine).get_view_names(include='materialized')
    for v in mat_views:
        refresh_mat_view(v, concurrently)


class MaterializedView(OrmBase):
    __abstract__ = True

    @classmethod
    def refresh(cls, dbSession, concurrently=True):
        '''Refreshes the current materialized view'''
        refresh_mat_view(cls.__table__.fullname, dbSession, concurrently)
