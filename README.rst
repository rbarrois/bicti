bicti
=====

Simple startup tool for docker containers.

bicti is intended as the entrypoint of a container,
and provides a few helpers for systems that may require several services
(for instance, fastcgi and nginx and cron and logrotate).


Its features include:

- Declarative list of supported commands
- Launch all demons or only a few ones
- Drop into a shell instead
- 


Depencies
---------

bicti is written in Python; it supports all versions from 2.6 onwards.
It also relies on ``runit`` (http://smarden.org/runit/) for daemon management.

Setup
-----

In your dockerfile, add:

.. code-block:: sh

    RUN apt-get -qqy install runit python python-pip
    RUN pip install bicti && ln -s /sbin/bicti `which bicti`
    ADD ./bicti.ini /etc/bicti.ini
    RUN /sbin/bicti --setup
    ENTRYPOINT "/sbin/bicti"

This will:

1. Retrieve bicti and its dependencies
2. Load your ``bicti.ini`` configuration file (expected at ``/etc/bicti.ini``)
3. Setup all daemon startup scripts in ``/etc/runit``
4. Declare bicti as your entry point.


Core concepts
-------------

Beyond a few command-line flags, most of bicti's job is in setting up the configuration
for ``runit``.

Upon startup, bicti will:

1. Load its configuration file (``/etc/bicti.ini``)
2. Setup ``runit`` to start the declared services
3. Transfer control to ``runit``, which handles daemon auto-restart, orphan process reaping, etc.



Usage
-----

.. code-block:: sh

    $ docker run my/image --help
    usage: bicti.py [--config CONFIG] [--root ROOT] [-h] [--setup]
                    [--shell [SHELL]] [--all]
                    [SERVICE [SERVICE ...]]

    Bicti, the docker inner setup.

    positional arguments:
      SERVICE               Services to start (valid options: cron,uwsgi)

    optional arguments:
      --config CONFIG, -c CONFIG
                            Read configuration from CONFIG
      --root ROOT           Use paths relative to ROOT
      -h, --help            Show this help message and exit
      --setup               Setup the service files
      --shell [SHELL]       Drop to a shell (default=/bin/bash)
      --all                 Start all services

Configuration file:

.. code-block:: ini

    [bicti]
    ; Run before any service is started
    setup = /sbin/my-image-setup
    ; Run once all services have been stopped
    teardown = /sbin/my-image-cleanup

    ; One section per service
    [cron]
    ; Actual command to run
    command = /usr/bin/cron
    ; Require another service to be started first
    after = syslog

    [uwsgi]
    command = /usr/bin/uwsgi
    ; Command to run before starting the service
    setup_command = mkdir /var/log/uwsgi
    ; Special uid/gid
    uid = www-data
    gid = www-data
