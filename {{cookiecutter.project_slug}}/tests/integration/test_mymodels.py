import pytest

from {{ cookiecutter.project_slug }} import models


@pytest.mark.parametrize('type', [
    models.MyModel.types.TYPE1,
    models.MyModel.types.TYPE2,
])
def test_mymodel_create(testapp, db_transaction, type):
    resp = testapp.post('/mymodels/', dict(type=str(type).lower()), status=201)
    guid = resp.json['mymodel']['id']
    with db_transaction() as session:
        mymodel = session.query(models.MyModel).get(guid)
    assert mymodel.type == type


def test_mymodel_get(testapp, db_transaction):
    with db_transaction() as session:
        mymodel = models.MyModel.create(
            type=models.MyModel.types.TYPE1,
        )
        session.add(mymodel)
    resp = testapp.get(
        '/mymodels/{}'.format(mymodel.guid),
    )
    assert resp.json['mymodel']['id'] == mymodel.guid
    assert resp.json['mymodel']['type'] == 'type1'
    assert resp.json['mymodel']['updated_at'] == mymodel.updated_at.isoformat()
    assert resp.json['mymodel']['created_at'] == mymodel.created_at.isoformat()
