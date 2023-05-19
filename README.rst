sqlalchemy-libsql
=================

A `LibSQL<https://libsql.org/>`_ dialect for SQLAlchemy.

This dialect requires SQLAlchemy 2.0 or later.


Pre-requisites
--------------

- Running instance of https://github.com/libsql/sqld. You can easily get one at https://turso.tech/
- Alternatively a https://github.com/libsql/hrana-test-server, a pure-python implementation

Co-requisites
-------------

This dialect requires SQLAlchemy and libsql_client. They are specified as requirements so ``pip``
will install them if they are not already in place. To install, just::

    pip install sqlalchemy-libsql

Getting Started
---------------

Create an URL that points to your libsql database.
Then, in your Python app, you can connect to the database via::

    from sqlalchemy import create_engine
    engine = create_engine("sqlite+libsql://your-db.your-server.com?authToken=JWT_HERE&secure=true")

Note that ``secure=true`` query/search parameter will force the usage of
secure WebSockets (``wss://``) to connect to the remote server.


The SQLAlchemy Project
======================

SQLAlchemy-libsql is part of the `SQLAlchemy Project <https://www.sqlalchemy.org>`_ and
adheres to the same standards and conventions as the core project.

Development / Bug reporting / Pull requests
-------------------------------------------

Please refer to the
`SQLAlchemy Community Guide <https://www.sqlalchemy.org/develop.html>`_ for
guidelines on coding and participating in this project.

Code of Conduct
_______________

Above all, SQLAlchemy places great emphasis on polite, thoughtful, and
constructive communication between users and developers.
Please see our current Code of Conduct at
`Code of Conduct <https://www.sqlalchemy.org/codeofconduct.html>`_.


Credits
=======

This project structure is based on
https://github.com/gordthompson/sqlalchemy-access, a project cited at
`README.dialects.rst
<https://github.com/sqlalchemy/sqlalchemy/blob/main/README.dialects.rst>`_.


License
=======

SQLAlchemy-libsql is distributed under the `MIT license
<https://opensource.org/licenses/MIT>`_.
