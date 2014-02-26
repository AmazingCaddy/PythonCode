#!/usr/bin/env python
#coding: utf-8

import urllib, urllib2, socket
import httplib
import sys

def test():
	url = 'http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html'
	try:
		response = urllib2.urlopen(url, timeout=1)
		text = response.read()
		print text
	except urllib2.URLError, e:
	#	if isinstance(e.reason, socket.timeout):
	#		print "timeout"
		print "Error"

if __name__ == '__main__':
	test()
	#print sys.argv