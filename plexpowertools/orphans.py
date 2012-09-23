#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012, Ken Pepple
#
# All rights reserved.

import fnmatch
import os
import sys

try:
  import sqlite3
except:
  print "ERROR: you need to install the necessary python eggs."
  print "$ sudo easy_install sqlite3"
  sys.exit(1)


directory = "/opt/video/tv/"
db = "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db"

def walk_video_directory(filepath):
  pattern = '[!._]*'
  x = []
  for root, dirs, files in os.walk(filepath):
    for filename in fnmatch.filter(files, pattern):
      x.append(os.path.join(root,filename))
  return x

def usage():
  pass

def main(argv):
  conn = sqlite3.connect(db)
  c = conn.cursor()
  videofiles = walk_video_directory(directory)
  for x in videofiles:
    c.execute('select media_item_id from media_parts where file=?', (x,))
    result = c.fetchone()
    if result is None:
      print '%s' % x 


if __name__ == '__main__':
  main(sys.argv)
