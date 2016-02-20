"""
WSGI config for home_work project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#
# import os
# import os.path
# import sys
#
# ROOT_DIR = os.path.abspath(os.path.dirname(__name__))
# CFG_DIR = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, ROOT_DIR)
# sys.path.insert(0, CFG_DIR)
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
#
# from django.core.handlers.wsgi import WSGIHandler
# application = WSGIHandler()

