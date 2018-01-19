# Pony Database Facade

Пакет pony-database-facade инкапсулирует имена параметров, используемых в низкоуровневых модулях.  

## Установка

```bash
pip install pony-database-facade
```

## Использование

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