sqlalchemy-libsql
=================

A `libSQL <https://libsql.org/>`_ dialect for `SQLAlchemy <https://www.sqlalchemy.org/>`_.


Pre-requisites
--------------

You must have a running instance of `sqld <https://github.com/libsql/sqld>`_,
which is the libSQL server mode. There are several supported options:

- `Build and run an instance
  <https://github.com/libsql/sqld/blob/main/docs/BUILD-RUN.md>`_ on your local
  machine.
- Use an instance managed by `Turso <https://turso.tech/>`_.
- Use the `libSQL test server <https://github.com/libsql/hrana-test-server>`_
  implemented in python

Co-requisites
-------------

This dialect requires the python packages `SQLAlchemy
<https://pypi.org/project/SQLAlchemy/>`__ (version 2.0 or later) and
`libsql_client <https://pypi.org/project/libsql-client/>`_. They are specified
as requirements so ``pip`` will install them if they are not already in place.
To install, just::

    pip install sqlalchemy-libsql

Getting Started
---------------

You must construct a special URL that SQLAlchemy can use to locate your
database. This will be different than the usual HTTP or websocket URLs that you
normally use with the libSQL client SDKs.

If you are running an instance of sqld on your own machine, normally listening
at 127.0.0.1 port 8080, the SQLAlchemy URL looks like this::

    sqlite+libsql://127.0.0.1:8080

If your sqld instance is configured to use SSL with some hostname, and requires
authentication with a database token (including Turso databases), you must
provide two additional configurations in the query string of the URL::

    sqlite+libsql://your-database-hostname/?authToken=your-auth-token&secure=true

``your-database-hostname`` and ``your-auth-token`` above are unique to your
database. ``secure=true`` specifies the use of SSL.

You can then pass this URL to SQLAlchemy::

    from sqlalchemy import create_engine
    engine = create_engine(url)

Development
-----------

This project uses `poetry <https://python-poetry.org/>`_, can be tested with
`pytest <https://pytest.org/>`_ and should be checked with
`pre-commit <https://pre-commit.com/>`_. A
`pure-python <https://github.com/libsql/hrana-test-server>`_ test server is used
as a submodule::

    git clone https://github.com/libsql/sqlalchemy-libsql.git
    cd sqlalchemy-libsql
    git submodule init && git submodule update  # hrana-test-server

    pre-commit install         # install git-hooks
    poetry install --with dev  # pytest

    pre-commit run -a          # check all files in the project, runs pytest

    poetry run pytest
    poetry run pytest --log-debug=libsql_client  # debug libsql_client usage
    # run against WSS server:
    poetry run pytest --dburi "sqlite+libsql://server.com?secure=true&authToken=JWT_HERE"


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
