from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from .. import models


@view_config(route_name='mymodels.view', renderer='json')
def view(request):
    guid = request.matchdict['guid']
    mymodel = request.dbsession.query(models.MyModel).get(guid)
    if mymodel is None:
        return HTTPNotFound()
    return dict(mymodel=mymodel)
