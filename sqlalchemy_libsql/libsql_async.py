r"""
.. dialect:: sqlite+libsql_async
    :name: libsql_async
    :dbapi: libsql_client.dbapi2
    :connectstring: sqlite+libsql_async://your-db.your-server.com?authToken=JWT_HERE&secure=true
    :url: https://github.com/libsql/libsql-client-py/

    Note that this driver is based on the standard SQLAlchemy ``pysqlite``
    dialect, the only change is how to connect, accepting remote URL in
    addition to the file dialects

    Disclaimer: While this dialect allows for async_engine compatibility with
    libsql, the dbapi remains synchronous

Driver
------

The ``libsql_client.dbapi2`` offers compatibility with standard library's
``sqlite3.dbapi2``. For local files or ``:memory:``, the standard library
connection is used. Whenever a host is provided, then the connection
will use LibSQL network protocol via ``ws`` (WebSocket) or ``wss``
(secure WebSocket), the decision depends on the presence of ``secure=true``
query parameter.

Connect Strings
---------------

In addition to `Pysqlite
<https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#connect-strings>`_,
this driver accepts URL with user, password, hostname and port.

These will use the LibSQL network protocol on top of WebSockets. The selection
between ``ws://`` and ``wss://` (secure) is defined by the query/search
parameter ``secure=true``. It defaults to  ``secure=false``.

If the given URL provides a hostname, then it will default to ``uri=true``.

"""  # noqa: E501

from sqlalchemy_libsql.libsql import SQLiteDialect_libsql


class SQLiteDialect_libsql_async(SQLiteDialect_libsql):
    driver = "libsql"
    # need to be set explicitly
    supports_statement_cache = SQLiteDialect_libsql.supports_statement_cache
    is_async = True


dialect = SQLiteDialect_libsql_async
