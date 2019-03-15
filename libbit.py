import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib
import BitRepository

def main(argv=sys.argv[1:]):
    argparser = argparse.ArgumentParser(description="Basic Information Tracker")
    argsubparser = argparser.add_subparsers(title="Commands", dest="command")
    argsubparser.required = True

    args = argparser.parse_args(argv)

    if args.command == "init": cmd_init(args)




def repo_path(repo, *path):
    """Compute path under repo's bitdir"""
    return os.path.join(repo.bitdir, *path)


def repo_file(repo, *path, mkdir=False):
    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)



def repo_dir(repo, *path, mkdir=False):
    path = repo_path(repo, *path)

    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception("Not a directory %s" % path)

    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None




argsp = argsubparsers.add_parser("init", help="Initialize new and empty repository")
argsp.add_argument("path", metavar="directory", nargs="?", default=".". help="Where to create repository")


def cmd_init(args):
    repo_create(args.path)