import os

import psutil

from utils import is_process_running, send_slack_message


def check_celery_workers_heartbeat():
    """
    Notifies through Slack when there are no active Celery workers.
    """
    if not is_process_running('celery'):
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        error_message = (
            '*Error:* Celery workers are not running.\nMemory used: *{}%*\nDisk used: *{}%*'
        ).format(memory_info.percent, disk_info.percent)
        send_slack_message(text=error_message)


if __name__ == '__main__':
    check_celery_workers_heartbeat()
