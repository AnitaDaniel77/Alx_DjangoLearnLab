#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
=======

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')

>>>>>>> 5b4842a05845136b4460cd1b3146030f79c267bb
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
<<<<<<< HEAD
=======

>>>>>>> 5b4842a05845136b4460cd1b3146030f79c267bb
