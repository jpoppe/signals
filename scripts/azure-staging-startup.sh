#!/bin/bash

apt-get update
apt-get install -y sl gdal-bin python3-gdal libcairo2 python-gobject-2 libpango-1.0-0 libpangocairo-1.0-0 postgresql-client

python /home/site/wwwroot/api/app/manage.py collectstatic

echo "🦄 starting gunicorn 🦄"

gunicorn --workers 2 --threads 2 --timeout 60 --bind=0.0.0.0:8000 \
  --access-logfile=/var/log/gunicorn-access.log \
  --error-logfile=/var/log/gunicorn-error.log \
  --capture-output=true \
  --chdir=/home/site/wwwroot/api/app signals.wsgi
