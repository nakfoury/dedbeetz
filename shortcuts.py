#!/usr/bin/env python
"""Shortcuts for commonly used commands during project development"""

import sys
import os


def sqlproxy():
    return os.system('cloud_sql_proxy -instances="dedbeetz:us-west2:dedbeetz-postgresql"=tcp:5432')


def deploy():
    return os.system('python manage.py collectstatic --no-input & gcloud --quiet --project dedbeetz app deploy')


if __name__ == '__main__':
    try:
        exit(0 if locals()[sys.argv[1]]() == 0 else 1)
    except IndexError:
        print('A command is required', file=sys.stderr)
        exit(1)
    except (TypeError, KeyError):
        print(f'Bad command: {sys.argv[1]}', file=sys.stderr)
        exit(1)
