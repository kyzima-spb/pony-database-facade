# coding: utf-8

import json
from datetime import datetime

from pony.orm import db_session, show

from model import db, Task


# Load config from file
with open('config.json') as f:
    config = json.load(f)


# Update connection options
db.bind(**config)

# Make a connection
db.connect()


with db_session:
    task = Task(title='Изучить pony-database-facade',
                description='Пригодится для flask-pony',
                planned=datetime.now())

show(task)
