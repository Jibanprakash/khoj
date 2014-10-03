#!/usr/bin/python

'''
  This program is a part of Khoj - The multi-platform Local search engine

  Copyright (C) 2014 Jiban Prakash, jibanprakash.jp(at)gmail(dot)com
  Saurabh Araiyer,  sizzsa(at)gmail(dot)com
  
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

''' 
This file implements the basic
folder parsing and storing the 
meta data
'''
import os, sys
from stat import *
import time

root_dir = "/home/jiban/Desktop/Work/TestKhoj" # Search DIR

def walktree(top, callback):
	storemetadata(top)
	'''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''
	for f in os.listdir(top):
		pathname = os.path.join(top, f)
		mode = os.stat(pathname).st_mode
		if S_ISDIR(mode):
			# It's a directory, recurse into it
			#storemetadata(pathname, f)
			walktree(pathname, callback)
		elif S_ISREG(mode):
			# It's a file, call the callback function
			callback(pathname)
		else:
			# Unknown file type, print a message
			print 'Skipping %s' % pathname

def visitfile(file):
    print 'visiting', file

	
def storemetadata(dirpath):
	dirname = dirpath[dirpath.rfind("/", 0,len(dirpath)) + 1:]

	print "storing metadata for ", dirpath, dirname
	metadata_file = dirpath + "/" + dirname + ".txt"

	dir_path = dirpath
	dir_size = 0
	dir_ctime = 0
	dir_atime = 0
	dir_mtime = 0
	try:
		fo = open(metadata_file, "w+")
		fo.write(dir_path)
		dir_size = os.stat(dir_path).st_size
		fo.write(" ~ " + str(dir_size))
		dir_ctime = os.stat(dir_path).st_ctime
		fo.write(" ~ " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dir_ctime))))
		dir_atime = os.stat(dir_path).st_atime
		fo.write(" ~ " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dir_atime))))
		dir_mtime = os.stat(dir_path).st_mtime
		fo.write(" ~ " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dir_mtime))))
		fo.write("\n")
		for f in os.listdir(dir_path):
			pathname = os.path.join(dir_path, f)
			fo.write(pathname)
			dir_size = os.stat(pathname).st_size
			fo.write(" ~ " + str(dir_size))
			dir_ctime = os.stat(pathname).st_ctime
			fo.write(" ~ " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dir_ctime))))
			dir_atime = os.stat(pathname).st_atime
			fo.write(" ~ " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dir_atime))))
			dir_mtime = os.stat(pathname).st_mtime
			fo.write(" ~ " + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dir_mtime))))
			fo.write("\n")
	except IOError as err:
		print err

if __name__ == '__main__':
	walktree(root_dir, visitfile)

