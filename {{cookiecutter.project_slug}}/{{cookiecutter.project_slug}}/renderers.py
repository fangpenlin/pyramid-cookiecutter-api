import datetime
import sys

import venusian
from pyramid.interfaces import IJSONAdapter
from pyramid.renderers import JSON
from pyramid.settings import asbool
from zope.interface import providedBy

from . import models

JSONIFY_CATEGORY = 'jsonify_renderer'


def jsonify(object_type):
    def decorator(func):
        def callback(scanner, name, ob):
            scanner.adapters.append((object_type, func))
        venusian.attach(func, callback, category=JSONIFY_CATEGORY)
        return func
    return decorator


def enum_symbol(enum_value):
    if enum_value is None:
        return enum_value
    return str(enum_value).lower()


@jsonify(datetime.datetime)
def datetime_adapter(dt, request):
    return dt.isoformat()


@jsonify(models.MyModel)
def mymodel_adapter(mymodel, request):
    return dict(
        id=mymodel.guid,
        type=enum_symbol(mymodel.type),
        updated_at=mymodel.updated_at,
        created_at=mymodel.created_at,
    )


class JSONRenderer(JSON):

    def __init__(self, pretty_print=True):
        current_module = sys.modules[__name__]
        scanner = venusian.Scanner(adapters=[])
        scanner.scan(current_module, categories=(JSONIFY_CATEGORY,))
        kwargs = dict(adapters=scanner.adapters)
        if pretty_print:
            kwargs.update(dict(
                sort_keys=True,
                indent=4,
                separators=(',', ': ')),
            )
        super().__init__(**kwargs)

    def jsonify(self, obj, request=None):
        """Return a dict for jsonify object

        """
        if hasattr(obj, '__json__'):
            return obj.__json__(request)
        not_found = object()
        obj_iface = providedBy(obj)
        result = self.components.adapters.lookup(
            (obj_iface, ),
            IJSONAdapter,
            default=not_found,
        )
        if result is not_found:
            raise TypeError('{} is not JSON serializable'.format(obj))
        return result(obj, request)


def includeme(config):
    settings = config.registry.settings
    cfg_key = 'api.json.pretty_print'
    pretty_print = asbool(settings.get(cfg_key, True))
    renderer = JSONRenderer(pretty_print)
    config.add_renderer('json', renderer)
