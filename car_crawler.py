#!/usr/bin/env python
#coding: utf-8

from bs4 import BeautifulSoup
import urllib, urllib2
import re, hashlib, time
import socket
from StringIO import StringIO
import gzip

import MySQLdb

import wwbcom

def fetch(url, pattern):
	platform_encoding = wwbcom.get_platform_encoding()
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
			except UnicodeDecodeError:
				continue
			except:
				raise Exception()
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
			for n_url in url_list:
				if n_url not in res:
					url_queue.append(n_url)
			cnt += 1
			print cnt
			res.add(url)
			fp.write(url + '\n')
			fp.flush()
			url_queue.remove(url)
			print 'start sleep'
			time.sleep(2)
			print 'end sleep'
	except KeyboardInterrupt:
		print 'Ended by KeyboardInterrupt'
	except Exception, e:
		print e
		print 'exit for something is wrong'
	finally:
		#print "len(url_queue) =", len(url_queue)
		fpqueue = open(queue_file, 'w')
		for url in url_queue:
			fpqueue.write(url + '\n')
		print 'db file OK'
		fpqueue.close()
		fp.close()

def get_html(url, req_header, timeout = 10, retry = 3):
	fails = 0
	html = ''
	while fails < retry:
		try:
			request = urllib2.Request(url, None, req_header)
			response = urllib2.urlopen(request, None, timeout)
			if response.info().get('Content-Encoding') == 'gzip':
				buf = StringIO(response.read())
				f = gzip.GzipFile(fileobj = buf)
				html = f.read()
			else:
				html = response.read()
		except socket.timeout, e:
			fails += 1
			time.sleep(5)
			print 'connection timeout, start to reconnect:', fails
		except urllib2.URLError, e:
			fails += 1
			time.sleep(5)
			print 'connection error, start to reconnect:', fails
		else:
			break
	return html

def fake_car():
	url = r"http://car.autohome.com.cn/"
	req_header = {
		'Accept':r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':r'gzip,deflate,sdch',
		'Accept-Language':r'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
		'Cache-Control':r'max-age=0',
		'Connection':r'keep-alive',
		'Host':r'car.autohome.com.cn',
		'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
		'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
	}
	html = get_html(url, req_header)
	print html
	#soup = BeautifulSoup(html)
	#print soup.title

if __name__ == '__main__':
	fake_car()