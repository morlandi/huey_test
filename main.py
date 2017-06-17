from __future__ import print_function
from builtins import input
import argparse
from config import huey  # DO NOT REMOVE ! makes sure tasks are imported
from tasks import count_beans


if __name__ == '__main__':

    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num-beans", type=int, default=0)
    parser.add_argument("-w", "--wait-task-completed", action='store_true')
    args = parser.parse_args()

    num_beans = args.num_beans
    if num_beans <= 0:
        num_beans = input('How many beans ? ')

    res = count_beans(int(num_beans))
    #res = count_beans.schedule(args=(int(num_beans), ), delay=10)
    print('Enqueued job to count %s beans' % num_beans)

    if args.wait_task_completed:
        print('waiting task completion ...')
        print(res(blocking=True))  # OK, let's just block until its ready

