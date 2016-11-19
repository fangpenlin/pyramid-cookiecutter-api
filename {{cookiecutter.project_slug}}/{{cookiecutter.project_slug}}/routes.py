def includeme(config):
    config.add_route('mymodels.create', '/mymodels/')
    config.add_route('mymodels.view', '/mymodels/{guid}')
