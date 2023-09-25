import argparse
import csv
import datetime
import logging
import os
import sys
import time
import traceback

import django
import environ
from memory_profiler import profile

__version__ = "0.0.1"

__doc__ = """ """

# setup django
sys.path.append(str(environ.Path(__file__) - 3))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from django.conf import settings


def get_opts():
    """Return an argparse object."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "--verbose", default=logging.INFO, action="store_const", const=logging.DEBUG, help="enable debug logging"
    )
    parser.add_argument("--version", action="version", version=__version__, help="show version and exit")
    args = parser.parse_args()
    logging.basicConfig(level=args.verbose)
    return args


# @profile
def do_something():
    logging.info("in do_something()")
    i = 0
    for i in range(1000):
        i += 10


def main():
    """script entry point"""
    try:
        # opts = get_opts()
        start = datetime.datetime.now()
        do_something()
        end = datetime.datetime.now()
        logging.info(f"script completed in: {end - start}")
    except Exception as err:
        logging.error(err)
        traceback.print_exc()
        return 255


if __name__ == "__main__":
    sys.exit(main())
