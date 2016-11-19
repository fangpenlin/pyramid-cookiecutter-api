import os

from setuptools import find_packages
from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction>=1.6,<1.7',
    'zope.sqlalchemy',
    'waitress',
    'base58',
    'pytz',
    'requests',
    'click',
    'ipython',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    'psycopg2',
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.0.0',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'tests': tests_require,
    },
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = {{ cookiecutter.project_slug }}:main
    [console_scripts]
    {{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.scripts.__main__:main

    """,
)
