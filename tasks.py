from datetime import datetime
import os
import time
from config import huey
from huey import crontab


def guess_instance():
    """
    Example: from '/Users/morlandi/src2/github_public/huey_test/tasks.py',
             returns 'huey_test'
    """
    try:
        return os.path.split(os.path.split(__file__)[0])[1]
    except:
        return ''


def trace(message):
    text = '[%s] %s' % (guess_instance(), message)
    print(text)


@huey.task()
def count_beans(num):

    def update_progress(progress, i, num):
        new_progress = int(((i + 1) * 10) / num)
        if new_progress > progress:
            progress = new_progress
            print('%d%%' % (progress * 10), end=' ' if progress < 10 else '\n', flush=True)
        return progress

    trace('-- counter %s beans started ...' % num)
    progress = -1
    for i in range(0, num):
        time.sleep(0.01)
        progress = update_progress(progress, i, num)
    trace('-- counter %s beans completed' % num)

    return 'Counted %s beans' % num


@huey.periodic_task(crontab(minute='*'))
def print_time():
    trace(datetime.now())
