import psutil

from utils import send_slack_message


CPU_LIMIT = 90
MEMORY_LIMIT = 80
DISC_LIMIT = 80


def check_resources_usage():
    mapping = {
        'CPU': {'used': psutil.cpu_percent(), 'limit': CPU_LIMIT},
        'Memory': {'used': psutil.virtual_memory().percent, 'limit': MEMORY_LIMIT},
        'Disc space': {'used': psutil.disk_usage('/').percent, 'limit': DISC_LIMIT},
    }

    warning_messages = []
    info_messages = []

    for resource_name, params in mapping.items():
        used = params['used']
        limit = params['limit']
        if used >= limit:
            warning_messages.append('*Warning:* {} usage: *{}%* (limit: {})'.format(resource_name, used, limit))
        else:
            info_messages.append('{} usage: *{}%*'.format(resource_name, used))

    if warning_messages:
        warning_messages_str = '\n'.join(warning_messages)
        info_messages_str = '\n'.join(info_messages)
        message = '{}\n{}'.format(warning_messages_str, info_messages_str)
        send_slack_message(text=message)


if __name__ == '__main__':
    check_resources_usage()
