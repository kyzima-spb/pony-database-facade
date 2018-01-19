Pony Database Facade
====================

Реализует шаблон Facade для объекта ``Database`` PonyORM.
Этот пакет инкапсулирует имена параметров, используемых в низкоуровневых модулях.


Установка
---------

::

  pip install pony-database-facade


Конструктор
-----------

Конструктор ``DatabaseFacade`` и метод ``bind`` принимают следующие аргументы:

provider
  Имя используемой базы данных.
  Одно из списка: ``sqlite``, ``mysql``, ``postgres`` or ``oracle``.
  По-умолчанию ``sqlite``.

dbname
  Имя базы данных.
  Если вы используете SQLite, имя файла, в котором SQLite будет хранить данные и по умолчанию ``:memory:``.

host
  Имя хоста для подключения.
  По-умолчанию ``localhost``.

port
  TCP-порт сервера базы данных.
  По умолчанию используется стандартный порт для выбранной СУБД.

user
  Имя пользователя.
  По-умолчанию ``None``.

password
  Пароль.
  По-умолчанию ``None``.

charset (только для MySQL)
  По-умолчанию ``utf8``.

create_db (только для SQLite)
  Пробует создать базу данных, если такой файл не существует.
  По-умолчанию ``True``.

\*args
  параметры, необходимые для драйвера базы данных.

\*\*kwargs
  параметры, необходимые для драйвера базы данных.

.. code:: python

    # SQLite in memory
    db = DatabaseFacade()

    # MySQL, localhost, no user, no password, used database blog
    db = DatabaseFacade('mysql', dbname='blog')
    db = DatabaseFacade(provider='mysql', dbname='blog')

    # PostgreSQL
    db = DatabaseFacade()
    db.bind('postgres',
            host='my.vps.com',
            user='anyone',
            password='anykey',
            dbname='blog')


Соединение
----------

Чтобы подключиться к базе данных, используйте метод ``connect``.
Этот метод принимает те же аргументы, что и `generate_mapping`_, но значение по умолчанию для ``create_tables`` равно ``True``.
Этот метод также вызывает метод ``bind``.

.. code:: python

    db = DatabaseFacade()
    db.connect()


Полный пример
-------------

.. code:: python

    from pony.orm import Required, db_session, show
    from pony_database_facade import DatabaseFacade


    db = DatabaseFacade()


    class Person(db.Entity):
        username = Required(str, 50)


    db.connect()

    with db_session:
        person_1 = Person(username='Linus')

    show(person_1)


.. _generate_mapping: https://docs.ponyorm.com/api_reference.html#Database.generate_mapping
