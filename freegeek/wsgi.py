"""
WSGI config for freegeek project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import site

# adding site-packages of desired virtualenv (in this case, py3.5)
site.addsitedir('/mnt/freegeek/lib/python3.5/site-packages')

# adding app's directory to the PYTHONPATH
sys.path.append('/mnt/free-geek')
sys.path.append('/mnt/free-geek/freegeek')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freegeek.settings")

# activate virtualenv
activate_env = os.path.expanduser("/mnt/freegeek/bin/activate_this.py")
exec(open(activate_env).read())

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freegeek.settings")

application = get_wsgi_application()
