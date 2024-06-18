#!/bin/bash
# entrypoint.sh

# Apply database migrations
echo "Making migrations..."
python manage.py makemigrations --noinput
echo "Applying database migrations..."
python manage.py migrate --noinput

# Start the server
echo "Starting server..."
exec "$@"
