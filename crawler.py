#!/usr/bin/env python
#coding: utf-8

from bs4 import BeautifulSoup
import urllib, urllib2
import re, hashlib, time
import socket

import MySQLdb

import platform

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

def fetch(url, pattern):
	fails = 0
	while fails < 3:
		try:
			req = urllib2.Request(url)
			response = urllib2.urlopen(req, None, 10)
			page = response.read()
		except socket.timeout, e:
			fails += 1
			time.sleep(5)
			print u'网络连接超时, 正在尝试再次请求: '.encode(platform_encoding), fails
		except urllib2.URLError, e:
			fails += 1
			time.sleep(5)
			print u'网络连接出现问题, 正在尝试再次请求: '.encode(platform_encoding), fails
		else:
			break
	if fails >= 3:
		return list()
	soup = BeautifulSoup(page, from_encoding='utf-8')
	links = soup.find_all('a')
	url_list = list()
	platform_encoding = get_platform_encoding()
	#chinese_pattern = re.compile(u'[\u4e00-\u9fa5]+')
	for li in links:
		if 'href' in li.attrs:
			ref = li.attrs['href']
			if isinstance(ref, unicode):
				ref = ref.encode('utf-8')
			ref = urllib.unquote(ref)
			try:
				#由于互动百科有些url有问题，会导致decode失败
				ref = ref.decode('utf-8')
			except:
				continue
			match_data = re.match(pattern, ref)
			if match_data:
				ref = '/'.join(match_data.groups())
				ref = ref.encode('utf-8')
				url_list.append(ref)
	return url_list

def fetch_fenlei(result_file, queue_file):
	platform_encoding = get_platform_encoding()
	pattern = ur'^(http://fenlei.baike.com)/([\u4e00-\u9fa5]+)'
	
	url_queue = list()
	fpqueue = open(queue_file, 'r')
	for line in fpqueue:
		url_queue.append(line.strip('\n'))
	fpqueue.close()

	fp = open(result_file, 'r')
	cnt = 0
	res = set()
	for line in fp:
		cnt += 1
		res.add(line.strip('\n'))
	fp.close()

	fp = open(result_file, 'a')
	try:
		while len(url_queue):
			url = url_queue[0]
			print url.decode('utf-8').encode(platform_encoding)
			if url in res:
				url_queue.remove(url)
				print u'已经搜索过'.encode(platform_encoding)
				continue
			url_list = fetch(url, pattern)
			cnt += 1
			print cnt
			res.add(url)
			url_queue.remove(url)
			fp.write(url + '\n')
			fp.flush()
			for url in url_list:
				if url not in res:
					url_queue.append(url)
			print 'start sleep'
			time.sleep(2)
			print 'end sleep'
	except KeyboardInterrupt:
		print 'Ended by KeyboardInterrupt'
	finally:
		#print "len(url_queue) =", len(url_queue)
		fpqueue = open(queue_file, 'w')
		for url in url_queue:
			fpqueue.write(url + '\n')
		print 'db file OK'
		fpqueue.close()
		fp.close()

if __name__ == '__main__':
	result_file = r'fenlei.txt'
	queue_file = r'url_queue.txt'
	fetch_fenlei(result_file, queue_file)
	