from sqlalchemy import exc
from sqlalchemy.testing.exclusions import closed
from sqlalchemy.testing.exclusions import only_on
from sqlalchemy.testing.requirements import SuiteRequirements


# this is based on sqlalchemy/test/requirements.py
class Requirements(SuiteRequirements):
    def _sqlite_json(self, config):
        with config.db.connect() as conn:
            try:
                return (
                    conn.exec_driver_sql(
                        """select json_extract('{"foo": "bar"}', """
                        """'$."foo"')"""
                    ).scalar()
                    == "bar"
                )
            except exc.DBAPIError:
                return False

    @property
    def json_type(self):
        return only_on([self._sqlite_json])

    @property
    def reflects_json_type(self):
        return only_on(["sqlite >= 3.9"])

    def _sqlite_partial_idx(self, config):
        with config.db.connect() as conn:
            connection = conn.connection
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM pragma_index_info('idx52')")
            except:
                return False
            else:
                return (
                    cursor.description is not None
                    and len(cursor.description) >= 3
                )
            finally:
                cursor.close()

    @property
    def sqlite_partial_indexes(self):
        return only_on(self._sqlite_partial_idx)

    def _sqlite_attach(self, config):
        with config.db.connect() as conn:
            connection = conn.connection
            cursor = connection.cursor()
            try:
                cursor.execute("ATTACH ':memory:' AS test_schema")
                cursor.execute("DETACH test_schema")
                return True
            except:
                return False
            finally:
                cursor.close()

    @property
    def sqlite_attach(self):
        return only_on(self._sqlite_attach)

    @property
    def sqlite_savepoint(self):
        # TODO: sqld should send "autocommit" state so we know
        # we're inside a transaction or not. Meanwhile libsql_client
        # tries to figure out and is lost with savepoints
        return closed()
