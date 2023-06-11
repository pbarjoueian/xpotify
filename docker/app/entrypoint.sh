#!/bin/sh
# docker/app/entrypoint.sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrate and collectstatic files
python manage.py makemigrations users tracks ml
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
