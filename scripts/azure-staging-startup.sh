#!/bin/bash

# apt-get update
# apt-get install -y sl gdal-bin python3-gdal libcairo2 python-gobject-2 libpango-1.0-0 libpangocairo-1.0-0 postgresql-client
# /antenv/bin/python /home/site/wwwroot/api/app/manage.py collectstatic

gunicorn --workers 2 --threads 2 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8001 \
     --chdir=/home/site/wwwroot/api/app signals.wsgi
