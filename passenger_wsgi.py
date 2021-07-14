# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1270192/data/www/robocode.uz/robocode')
sys.path.insert(1, '/var/www/u1270192/data/robovenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'robocode.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 