import pytest
from sqlalchemy.dialects import registry
from sqlalchemy.testing.plugin.pytestplugin import *  # noqa: F401,F403,E402

registry.register("sqlite.libsql", "sqlalchemy_libsql", "SQLiteDialect_libsql")

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")
