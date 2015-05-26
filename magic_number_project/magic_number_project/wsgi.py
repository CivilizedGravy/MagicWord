"""
WSGI config for magic_number_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
activate_this = '/home/Civilizedgravy/magic_word_env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

path = '/home/Civilizedgravy/magic_word_project'

if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magic_number_project.settings")
import django
django.setup()

application = get_wsgi_application()
