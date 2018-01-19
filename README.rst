Pony Database Facade
====================

|PyPI|

The pony-database-facade package encapsulates the names of the parameters used in the low-level modules.  


Check out this `relative link`_.

.. _relative link: docs/RU.md

[Русская документация](docs/RU.md)


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

.. |PyPI| image:: https://img.shields.io/pypi/v/pony-database-facade.svg
    :target: https://pypi.python.org/pypi/pony-database-facade/
    :alt: Latest Version
