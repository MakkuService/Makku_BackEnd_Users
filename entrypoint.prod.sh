#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $db_host $db_port; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"