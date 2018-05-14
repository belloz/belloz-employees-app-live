import sys, os

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/employees_project')

INTERP = os.path.expanduser("~/.virtualenvs/employees_project/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'$HOME/.virtualenvs/employees_project/bin')
sys.path.insert(0,'$HOME/.virtualenvs/employees_project/lib/python3.5/site-packages/django')
sys.path.insert(0,'$HOME/.virtualenvs/employees_project/lib/python3.5/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Employees_Project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
