#!/bin/bash

# Next needed to save and then pass env variables to cron job
# E.g. SLACK_TOKEN
printenv | sed "s/^\(.*\)$/export \1/g" > /config/project_env.sh

crontab /etc/cron.d/cronjobs
service cron start

if [ "$TEST_FAILURE" = "true" ]; then
    tail -f /dev/null
else
    celery worker --app=worker.app --loglevel=INFO
fi
