#!/usr/bin/env python
import os
import sys

from dannywebsite.utils import settings_to_use


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_to_use(sys.argv))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
