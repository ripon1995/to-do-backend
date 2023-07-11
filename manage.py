#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import firebase_admin
from firebase_admin import credentials


def main():
    """Run administrative tasks."""
    cred = credentials.Certificate("utils/todo-1938b-firebase-adminsdk-vdquj-a63d16a98d.json")
    firebase_admin.initialize_app(cred)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoapp.settings.dev')
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
