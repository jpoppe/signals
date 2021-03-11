#!/bin/bash

apt-get update
apt-get install -y sl gdal-bin python3-gdal libcairo2 python-gobject-2 libpango-1.0-0 libpangocairo-1.0-0 postgresql-client

gunicorn --workers 8 --threads 4 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000 \
     --chdir=/home/site/wwwroot/api/app signals.wsgi
