# coding: utf-8

from datetime import datetime

from pony.orm import Required, Optional, Set
from pony_database_facade import DatabaseFacade


db = DatabaseFacade()


class Task(db.Entity):
    title = Required(str, 50)
    planned = Required(datetime)
    description = Required(str)
    done = Optional(bool, default=False)
    # created = Optional(datetime)
