# coding: utf-8

from pony.orm import Required, db_session, show
from pony_database_facade import DatabaseFacade


db = DatabaseFacade()


class Person(db.Entity):
    username = Required(str, 50)


db.connect()

with db_session:
    person_1 = Person(username='Linus')

show(person_1)
