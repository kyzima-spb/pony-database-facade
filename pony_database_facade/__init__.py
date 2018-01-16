# coding: utf-8
#
# Copyright 2017 Kirill Vercetti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from pony.orm import Database

from .loader import Loader


class DatabaseFacade(object):
    """PonyORM Database object Facade"""

    def __init__(self, **config):
        self.__db = Database()
        self.set_config(config)

    def __init_defaults(self):
        """Initializes the default connection settings."""

        config = self.__config
        config.setdefault('provider', 'sqlite')

        provider = config.get('provider')

        if provider == 'sqlite':
            config.setdefault('dbname', ':memory:')
        elif provider == 'mysql':
            config.setdefault('port', 3306)
        elif provider == 'postgres':
            config.setdefault('port', 5432)
        elif provider == 'oracle':
            config.setdefault('port', 1521)
        else:
            raise ValueError('Unsupported provider "{}"'.format(provider))

        config.setdefault('host', 'localhost')
        config.setdefault('user', None)
        config.setdefault('password', None)
        config.setdefault('dbname', None)
        config.setdefault('charset', 'utf8')

    def bind(self):
        config = self.__config
        provider = config.get('provider')
        args = [provider]
        kwargs = {}

        if provider == 'sqlite':
            filename = config.get('dbname')

            if filename != ':memory:' and not os.path.dirname(filename):
                filename = os.path.join(os.getcwd(), filename)

            kwargs.update({
                'filename': filename,
                'create_db': True
            })
        elif provider == 'mysql':
            kwargs.update({
                'host': config.get('host'),
                'port': config.get('port'),
                'user': config.get('user'),
                'passwd': config.get('password'),
                'db': config.get('dbname'),
                'charset': config.get('charset')
            })
        elif provider == 'postgres':
            kwargs.update({
                'host': config.get('host'),
                'port': config.get('port'),
                'user': config.get('user'),
                'password': config.get('password'),
                'database': config.get('dbname')
            })
        elif provider == 'oracle':
            args.append('{user}/{password}@{host}:{port}/{dbname}'.format(user=config.get('user'),
                                                                          password=config.get('password'),
                                                                          host=config.get('host'),
                                                                          port=config.get('port'),
                                                                          dbname=config.get('dbname')
                                                                          ))

        self.original.bind(*args, **kwargs)

    def connect(self):
        self.bind()
        self.original.generate_mapping(create_tables=True)

    @property
    def original(self):
        return self.__db

    @property
    def Entity(self):
        return self.original.Entity

    def set_config(self, config):
        self.__config = config
        self.__init_defaults()

    @staticmethod
    def load_module_with_entities(name):
        assert isinstance(name, str)
        return Loader().load_and_registry(name)
