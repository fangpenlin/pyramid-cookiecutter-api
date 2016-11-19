from {{ cookiecutter.project_slug }} import models


def test_create_mymodel(db_transaction):
    with db_transaction() as session:
        mymodel = models.MyModel.create(type=models.MyModel.types.TYPE1)
        session.add(mymodel)
    assert mymodel.guid.startswith('MD')
    assert mymodel.type == models.MyModel.types.TYPE1
