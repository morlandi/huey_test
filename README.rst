
Purpose
-------

Test `Huey <https://github.com/coleifer/huey>`_ in a simple environment.

Manual setup
------------

::

    $ mkvirtualenv huey_test
    $ pip install -r requirements.txt

Run consumer
------------

::

    $ huey_consumer.py main.huey
        [2017-06-17 18:48:03,246] INFO:huey.consumer:MainThread:Huey consumer started with 1 thread, PID 54742
        [2017-06-17 18:48:03,246] INFO:huey.consumer:MainThread:Scheduler runs every 1 seconds.
        [2017-06-17 18:48:03,247] INFO:huey.consumer:MainThread:Periodic tasks are enabled.
        [2017-06-17 18:48:03,247] INFO:huey.consumer:MainThread:UTC is enabled.
        [2017-06-17 18:48:03,247] INFO:huey.consumer:MainThread:The following commands are available:
        + count_beans
        + print_time

Execute async tasks
-------------------

::

    $ python main.py -n 100
        Enqueued job to count 100 beans
    $ python main.py -n 1000
        Enqueued job to count 1000 beans
    $ python main.py -n 2000 -w
        Enqueued job to count 2000 beans
        waiting task completion ...
        Counted 2000 beans

References
----------

- `huey, a little task queue <https://huey.readthedocs.io/en/latest/index.html>`_
- `Looking for an alternative to Celery? Try Huey <https://www.packtpub.com/books/content/looking-for-alternative-celery-try-huey>`_
