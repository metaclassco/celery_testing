FROM python:3.6.6
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

# Install cron
RUN apt-get update && apt-get -y install cron

# Copy cronjobs file to the cron.d directory
COPY config/cronjobs /etc/cron.d/cronjobs

WORKDIR /
COPY . /

# Create file for cron logs
RUN mkdir logs && touch /logs/cron.log
RUN chmod 0755 /logs/cron.log

# Create file to save env variables for cron jobs
RUN touch /config/project_env.sh
RUN chmod 0755 /config/project_env.sh

# Install requirements
RUN pip install -r requirements.txt

WORKDIR /app
RUN chmod +x /config/entrypoint.sh
CMD ["/config/entrypoint.sh"]
