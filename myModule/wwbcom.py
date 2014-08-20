#!/usr/bin/env python
#coding: utf-8

from __future__ import print_function
import platform
import sys
import time
import string, re
import json

def clean_non_alpha(s):
	''' s 不能是unicode '''
	# delEStr 中的每个字符表示要去掉的字符
	delEStr = string.punctuation + string.digits + '\r\n'
	# print delEStr
	# 生成一个映射表，这里是把所有要去掉的字符映射成空格
	identify = string.maketrans(delEStr, ' ' * len(delEStr))
	s = ' '.join([i for i in string.translate(s, identify).lower().split(' ') if i != ''])
	return s

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

def check_legal_name(name):
	if not isinstance(name, unicode):
		name = name.decode('utf-8')
	pattern = re.compile(ur'([\u00b7\u4e00-\u9fa5]+)')
	m = pattern.match(name)
	if m:
		return m.groups()
	else:
		return False

def check_legal_chinese(word):
	if not isinstance(word, unicode):
		word = word.decode('utf-8')
	pattern = re.compile(ur'([\u0000-\u007e\u4e00-\u9fa5\uff01-\uff5e]+)')
	m = pattern.match(name)
	if m:
		return m.groups()
	else:
		return False

def strq2b(ustring):
	"""全角转半角"""
	rstring = ""
	for uchar in ustring:
		inside_code=ord(uchar)
		if inside_code == 12288:								#全角空格直接转换			
			inside_code = 32 
		elif (inside_code >= 65281 and inside_code <= 65374):	#全角字符（除空格）根据关系转化
			inside_code -= 65248
		rstring += unichr(inside_code)
	return rstring
	
def strb2q(ustring):
	"""半角转全角"""
	rstring = ""
	for uchar in ustring:
		inside_code=ord(uchar)
		if inside_code == 32:								#半角空格直接转化				  
			inside_code = 12288
		elif inside_code >= 33 and inside_code <= 126:		#半角字符（除空格）根据关系转化
			inside_code += 65248
		rstring += unichr(inside_code)
	return rstring

def test():
	pass

if __name__ == '__main__':
	test()