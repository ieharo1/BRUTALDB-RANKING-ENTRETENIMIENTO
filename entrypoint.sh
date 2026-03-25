#!/bin/sh
set -e

if [ -n "$POSTGRES_HOST" ]; then
  echo "Esperando a PostgreSQL en $POSTGRES_HOST:$POSTGRES_PORT..."
  while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 1
  done
fi

python manage.py migrate --noinput
python manage.py seed_demo
python manage.py collectstatic --noinput

exec "$@"
