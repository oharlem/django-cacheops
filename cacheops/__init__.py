__version__ = '3.2.1'
VERSION = tuple(__version__.split('.'))


from django.apps import AppConfig

from .simple import *
from .query import *
from .invalidation import *
from .templatetags.cacheops import *
from .transaction import install_cacheops_transaction_support


class CacheopsConfig(AppConfig):
    name = 'cacheops'

    def ready(self):
        install_cacheops()
        install_cacheops_transaction_support()

default_app_config = 'cacheops.CacheopsConfig'
