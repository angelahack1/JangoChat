#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser from environment variables
echo "Creating superuser..."
python manage.py create_superuser_from_env

# Start the main application
exec "$@"