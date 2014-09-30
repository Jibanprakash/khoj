#!/usr/bin/python

''' 
This file implements the basic
folder parsing and storing the 
metadata
'''
import os, sys
from stat import *

root_dir = "/home/jiban/Desktop/Work" # Search DIR

class dir_metadata:

	def __init__(self, dirname, filename):
		self.name = filename
		self.path = dirname
		self.size = 0
		self.ctime = 0
		self.atime = 0
		self.mtime = 0

	def setmetadata(self):
		self.size = os.stat(self.path).st_size
		self.ctime = os.stat(self.path).st_ctime
		self.atime = os.stat(self.path).st_atime
		self.mtime = os.stat(self.path).st_mtime

	def dumpmetadata(self):
		print self.path, self.name
		filename = self.path + "/" + self.name+ ".txt"
		print filename
		try:
			fo = open(filename, "a+")
			writeobj =  self.path
			fo.write(writeobj)
		except IOError as e:
			print " The Error is" , e

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            storemetadata(pathname, f)
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print 'Skipping %s' % pathname

def visitfile(file):
    print 'visiting', file

def storemetadata(dirname , filename):
	print "storing metadata for ", dirname, filename
	dir_data = dir_metadata(dirname, filename)
	dir_data.setmetadata()
	dir_data.dumpmetadata()
	
if __name__ == '__main__':
    walktree(root_dir, visitfile)

