import os

import psutil
from slack import WebClient


def is_process_running(process_name):
    """
    Checks if there is any running process that contains the given name
    `process_name`.
    """
    # Iterate over the all running processes
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string
            if process_name.lower() == proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def send_slack_message(text, channel='#random'):
    """
    Sends `text` to provided `channel`.
    """
    client = WebClient(token=os.environ['SLACK_TOKEN'])
    client.chat_postMessage(channel=channel, text=text, as_user=False, icon_emoji=':robot_face:')


def check_celery_workers_is_running():
    """
    Notifies through Slack when there are no active Celery workers.
    """
    if not is_process_running('celery'):
        error_message = '*Error:* Celery workers are not running.'
        send_slack_message(text=error_message)
    else:
        error_message = '*Error:* Celery workers are not running.'
        send_slack_message(text=error_message)


if __name__ == '__main__':
    check_celery_workers_is_running()
