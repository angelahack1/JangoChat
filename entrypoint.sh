#!/bin/sh

set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Create superuser from environment variables
echo "Creating superuser..."
python manage.py create_superuser_from_env

# Start the main application
exec "$@"