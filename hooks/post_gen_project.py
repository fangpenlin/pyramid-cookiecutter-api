import subprocess
import sys
import venv


venv.create('.env', with_pip=True)
proc = subprocess.Popen(
    ['.env/bin/pip', 'install', '--upgrade', 'pip', 'setuptools'],
    shell=sys.platform.startswith('win'),
    cwd='.',
)
proc.wait()
proc = subprocess.Popen(
    ['.env/bin/pip', 'install', '-e', '.[tests]'],
    shell=sys.platform.startswith('win'),
    cwd='.',
)
proc.wait()


print('Creating role: {{ cookiecutter.project_slug }}')
proc = subprocess.Popen(
    ['psql', '-c', "CREATE USER {{ cookiecutter.project_slug }} WITH PASSWORD '{{ cookiecutter.project_slug }}';"],
    shell=sys.platform.startswith('win'),
    cwd='.',
)
proc.wait()

print('Creating database: {{ cookiecutter.project_slug }}')
proc = subprocess.Popen(
    ['psql', '-c', 'CREATE DATABASE {{ cookiecutter.project_slug }} OWNER {{ cookiecutter.project_slug }}'],
    shell=sys.platform.startswith('win'),
    cwd='.',
)
proc.wait()

print('Creating database: {{ cookiecutter.project_slug }}_test')
proc = subprocess.Popen(
    ['psql', '-c', 'CREATE DATABASE {{ cookiecutter.project_slug }}_test OWNER {{ cookiecutter.project_slug }}'],
    shell=sys.platform.startswith('win'),
    cwd='.',
)
proc.wait()
