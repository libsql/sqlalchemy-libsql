from sqlalchemy.dialects import registry as _registry
from sqlalchemy_libsql.libsql import SQLiteDialect_libsql

__version__ = "0.1.0-pre"

_registry.register(
    "sqlite.libsql", "sqlalchemy_libsql", "SQLiteDialect_libsql"
)
