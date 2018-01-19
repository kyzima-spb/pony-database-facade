Pony Database Facade
====================

|PyPI| `Русская документация`_

PonyORM Database object Facade. The package encapsulates the names of the parameters used in the low-level modules.


Installation
------------

::

  pip install pony-database-facade


Parameter names
---------------

provider
  The name of the database provider.
  One of the list: ``sqlite``, ``mysql``, ``postgres`` or ``oracle``.
  By default is ``sqlite``.

Usage
-----

.. code:: python

  # model.py

  from pony.orm import Required
  from pony_database_facade import DatabaseFacade


  db = DatabaseFacade()


  class Person(db.Entity):
      username = Required(str, 50)


.. code:: python

  # main.py

  from pony.orm import db_session

  import model


  model.db.connect()


  with db_session:
      person_1 = model.Person(username='Linus')


.. |PyPI| image:: https://img.shields.io/pypi/v/pony-database-facade.svg
    :target: https://pypi.python.org/pypi/pony-database-facade/
    :alt: Latest Version

.. _Русская документация: docs/RU.md
