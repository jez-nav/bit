import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib


def main(argv=sys.argv[1:]):
    argparser = argparse.ArgumentParser(description="Basic Information Tracker")
    argsubparser = argparser.add_subparsers(title="Commands", dest="command")
    argsubparser.required = True

    args = argparser.parse_args(argv)

    if      args.command == "init"           : cmd_init(args)

