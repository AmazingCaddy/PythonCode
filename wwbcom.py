#!/usr/bin/env python
#coding: utf-8

from __future__ import print_function
import platform
import sys
import time
import re
import json

def print_error(*args):
	ms = time.time() % 1
	timestamp = "".join([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), ',', ('%.3f' % ms)[2:]])
	print(timestamp, '[ERROR]', *args, file=sys.stderr)

def print_warn(*args):
	ms = time.time() % 1
	timestamp = "".join([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), ',', ('%.3f' % ms)[2:]])
	print(timestamp, '[WARN]', *args, file=sys.stderr)

def fprint(fout=sys.stdout, *args):
	print(*args, file=fout)

def get_platform_encoding():
	platform_encoding = 'utf-8'
	if platform.system() not in ['Linux', 'Darwin']:
		platform_encoding = 'gbk'
	return platform_encoding

def is_chinese(uchar):
	"""判断一个unicode是否是汉字"""
	if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
		return True
	else:
		return False

def check_legal_name (name):
	if not isinstance(name, unicode):
		name = name.decode('utf-8')
	pattern = re.compile(ur'([\u00b7\u4e00-\u9fa5]+)')
	m = pattern.match(name)
	if m:
		return m.groups()
	else:
		return False

def test():
	#l = '{"X": "Y", "X": "c"}'
	#print(json.loads(l))
	pass

if __name__ == '__main__':
	test()