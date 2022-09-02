#!/var/www/u997259/data/flaskenv/bin/python3
# -*- coding: utf-8 -*-

import sys, os

# Add a custom Python path.
sys.path.insert(0, "/var/www/u997259/data/www/test.hand-made-tlt.ru/")

# Switch to the directory of your project. (Optional.)
os.chdir("/var/www/u997259/data/www/test.hand-made-tlt.ru/")

from wsgiref.handlers import CGIHandler
#from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    CGIHandler().run(app)
    #WSGIServer(app).run()