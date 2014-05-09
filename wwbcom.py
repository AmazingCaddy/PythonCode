#!/usr/bin/env python
#coding: utf-8

from __future__ import print_function
import platform
import sys
import time

def print_error(*args):
	ms = time.time() % 1
	timestamp = "".join([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), ',', ('%.3f' % ms)[2:]])
	print(timestamp, '[ERROR]', *args, file=sys.stderr)

def print_warn(*args):
	ms = time.time() % 1
	timestamp = "".join([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), ',', ('%.3f' % ms)[2:]])
	print(timestamp, '[WARN]', *args, file=sys.stderr)

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

def test():
	pass

if __name__ == '__main__':
	test()