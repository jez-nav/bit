import configparser
import os

class BitRepository(object):
    """A bit repository"""

   worktree = None
   bitdir = None
   conf = None

   def __init__(self, path, force=False):
       self.worktree = path
       self.bitdir = os.path.join(path, ".bit")

       if not (force or os.path.isdir(self.bitdir)):
           raise Exception("Not a .bit repository %s" % path)

       self.config = configparser.ConfigParser()
       config_file = repo_file(self, "config")

       if config_file and os.path.exists(config_file):
           self.config.read([config_file])
       elif not force:
           raise Exception("Config file missing")

       if not force:
           version = int(self.config.get("core", "repositoryformatversion"))
           if version != 0 and not force:
               raise Exception("Unsupported repositoryformatversion %s" % version)
