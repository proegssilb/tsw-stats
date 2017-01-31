from __future__ import with_statement
import os
from alembic import context
from sqlalchemy import create_engine, pool
from logging.config import fileConfig
from db import OrmBase

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

fileConfig(config.config_file_name)
target_metadata = OrmBase.metadata


def initEnv(envFile):
    """Set environment variables based on a config file."""
    if envFile != '' and envFile is not None:
        with open(envFile) as envVars:
            for line in envVars:
                var, val = line.split('=', 1)
                var = var.strip()
                val = val.strip()
                os.environ[var] = val

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    initEnv('envfile.txt')
    url = os.environ['DBMIGRATECONN']
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    initEnv('envfile.txt')
    url = os.environ['DBMIGRATECONN']
    connectable = create_engine(url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
