#!/bin/bash

# PGPASSWORD=insecure psql --host=basis-db.postgres.database.azure.com --port=5432 --username=signals@basis-db --dbname=signals

apt-get update
apt-get install -y sl gdal-bin python3-gdal libcairo2 python-gobject-2 libpango-1.0-0 libpangocairo-1.0-0 postgresql-client

ant_env_location=$(head -n1 /antenv/bin/pip | cut -f 3 -d/)
mkdir "/tmp/${ant_env_location}"
ln -s /antenv "/tmp/${ant_env_location}/antenv"

source /antenv/bin/activate
python /home/site/wwwroot/api/app/manage.py collectstatic

gunicorn --workers 2 --threads 2 --timeout 60 --access-logfile '-' --error-logfile '-' --bind=0.0.0.0:8001 --chdir=/home/site/wwwroot/api/app signals.wsgi

python manage.py runserver 0.0.0.0:8002
