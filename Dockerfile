FROM python:3.6.6
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

# Install cron
RUN apt-get update && apt-get -y install cron

# Copy cronjobs file to the cron.d directory
COPY config/cronjobs /etc/cron.d/cronjobs

# Give execution rights on the cron job
RUN chmod 0755 /etc/cron.d/cronjobs

# Apply cron job
RUN crontab /etc/cron.d/cronjobs

WORKDIR /
COPY . /

# Install requirements
RUN pip install -r requirements.txt

# Start cron
RUN service cron start

WORKDIR /app

# Start Celery worker
CMD ["celery", "worker", "--app=worker.app", "--loglevel=INFO"]
