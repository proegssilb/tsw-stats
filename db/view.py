"""A module for supporting Materialized Views in SQLAlchemy.

Based on https://github.com/jeffwidman/sqlalchemy-postgresql-materialized-views
"""

# Accompanying blog post:
# http://www.jeffwidman.com/blog/847/

# Many thanks to Mike Bayer (@zzzeek) for his help.
# pylama:skip=1

from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement, PrimaryKeyConstraint
import sqlalchemy as db


class CreateMaterializedView(DDLElement):
    def __init__(self, name, selectable):
        self.name = name
        self.selectable = selectable


@compiler.compiles(CreateMaterializedView)
def compile(element, compiler, **kw):
    # Could use "CREATE OR REPLACE MATERIALIZED VIEW..."
    # but I'd rather have noisy errors
    return "CREATE MATERIALIZED VIEW %s AS %s" % (
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


def create_mat_view(metadata, name, selectable):
    _mt = db.MetaData()  # temp metadata just for initial Table object creation
    t = db.Table(name, _mt)  # the actual mat view class is bound to db.metadata
    for c in selectable.c:
        t.append_column(db.Column(c.name, c.type, primary_key=c.primary_key))

    if not (any([c.primary_key for c in selectable.c])):
        t.append_constraint(PrimaryKeyConstraint(*[c.name for c in selectable.c]))

    db.event.listen(
        metadata, "after_create",
        CreateMaterializedView(name, selectable)
    )

    @db.event.listens_for(metadata, "after_create")
    def create_indexes(target, connection, **kw):
        for idx in t.indexes:
            idx.create(connection)

    db.event.listen(
        metadata, "before_drop",
        db.DDL('DROP MATERIALIZED VIEW IF EXISTS ' + name)
    )
    return t
