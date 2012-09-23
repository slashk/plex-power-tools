#!/usr/bin/python

import fnmatch
import os
import sqlite3


def walk_video_directory(filepath):
  pattern = '[!._]*'
  x = []
  for root, dirs, files in os.walk(filepath):
    for filename in fnmatch.filter(files, pattern):
      x.append(os.path.join(root,filename))
  return x

directory = "/opt/video/tv/"
db = "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db"

conn = sqlite3.connect(db)
c = conn.cursor()
videofiles = walk_video_directory(directory)
for x in videofiles:
  c.execute('select media_item_id from media_parts where file=?', (x,))
  result = c.fetchone()
  #print result
  #print "%s: %s" % (x, str(result[0])) 
  if result is None:
    print 'rm "%s"' % x 
  #else:
    #print result
