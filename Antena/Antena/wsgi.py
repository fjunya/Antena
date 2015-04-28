# -*- coding: utf-8 -*-

import os,sys

sys.path.append('/home/fjunya/django/Antena/Antena')
os.environ["DJANGO_SETTINGS_MODULE"] = "Antena.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()