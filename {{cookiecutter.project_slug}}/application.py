from paste.deploy.config import PrefixMiddleware

import {{ cookiecutter.project_slug }}

application = {{ cookiecutter.project_slug }}.main({})

# handle proxing headers
application = PrefixMiddleware(application)
