from __future__ import with_statement

from logging.config import fileConfig
from os import getenv

import sqlalchemy
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def get_url():
    db_user = getenv("DB_USER")
    db_pass = getenv("DB_PASS")
    db_name = getenv("DB_NAME")
    db_type = getenv('DB_TYPE', 'mysql+pymysql')
    cloud_sql_instance_name = getenv("CLOUD_SQL_INSTANCE_NAME")
    if db_type == 'sqlite':
        return sqlalchemy.create_engine('sqlite:///test.db')
    else:
        return sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername=db_type,
                username=db_user,
                password=db_pass,
                database=db_name,
                query={
                    'unix_socket': '/cloudsql/{}'.format(
                        cloud_sql_instance_name)
                }
            ),
            pool_size=5,
            max_overflow=2,
            pool_timeout=30,  # 30 seconds
            pool_recycle=1800)


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = get_url()

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
