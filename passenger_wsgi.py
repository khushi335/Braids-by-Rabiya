import sys
import os

# Add your project directory to the Python path
project_home = '/home/hightech/project01.rominalimousineservice.com/braid'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtual environment
venv = '/home/hightech/virtualenv/project01.rominalimousineservice.com/braid/3.10'
activate_this = os.path.join(venv, 'bin', 'activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), {'__file__': activate_this})

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'braid.settings')

# Load Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()