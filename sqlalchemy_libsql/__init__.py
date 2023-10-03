from sqlalchemy.dialects import registry as _registry

from sqlalchemy_libsql.libsql import dialect
from sqlalchemy_libsql.libsql import SQLiteDialect_libsql
from sqlalchemy_libsql.libsql_async import SQLiteDialect_libsql_async

__version__ = "0.1.0-pre"

_registry.register(
    "sqlite.libsql", "sqlalchemy_libsql", "SQLiteDialect_libsql"
)

_registry.register(
    "sqlite.libsql_async", "sqlalchemy_libsql", "SQLiteDialect_libsql_async"
)

__all__ = ("SQLiteDialect_libsql", "SQLiteDialect_libsql_async", "dialect")
