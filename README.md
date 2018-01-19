# Pony Database Facade

The pony-database-facade package encapsulates the names of the parameters used in the low-level modules.  

[RU](docs/ru/README.md)

## Installation

```bash
pip install pony-database-facade
```

## Usage

```python
# model.py

from pony.orm import Required
from pony_database_facade import DatabaseFacade


db = DatabaseFacade()


class Person(db.Entity):
    username = Required(str, 50)

```

```python
# main.py

from pony.orm import db_session

import model


model.db.connect()


with db_session:
    person_1 = model.Person(username='Linus')

```