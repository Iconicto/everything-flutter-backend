#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# Start server
echo "Starting gunicorn server"
gunicorn EverythingFlutter.wsgi -b 0.0.0.0:8000