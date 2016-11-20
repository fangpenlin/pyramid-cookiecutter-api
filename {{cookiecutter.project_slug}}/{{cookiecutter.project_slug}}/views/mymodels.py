from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from .. import models


@view_config(
    route_name='mymodels.create',
    request_method='POST',
    renderer='json',
)
def create(request):
    type = models.MyModel.types.from_string(request.params['type'].upper())
    mymodel = models.MyModel.create(type=type)
    request.dbsession.add(mymodel)
    request.dbsession.flush()
    request.response.status = '201 Created'
    return dict(mymodel=mymodel)


@view_config(route_name='mymodels.view', renderer='json')
def view(request):
    guid = request.matchdict['guid']
    mymodel = request.dbsession.query(models.MyModel).get(guid)
    if mymodel is None:
        return HTTPNotFound()
    return dict(mymodel=mymodel)
