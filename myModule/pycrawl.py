#!/usr/bin/env python
#coding: utf-8

from bs4 import BeautifulSoup
from StringIO import StringIO

import urllib, urllib2
import socket
import gzip, time

import wwbcom

class crawler(object):
	"""docstring for crawler"""
	def __init__(self):
		super(crawler, self).__init__()
		#self.arg = arg

	def get_html(self, url, req_header, timeout = 10, retry = 3, sleep_time = 5):
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
				time.sleep(sleep_time)
				print 'connection timeout, start to reconnect:', fails
			except urllib2.URLError, e:
				fails += 1
				time.sleep(sleep_time)
				print 'connection error, start to reconnect:', fails
			else:
				break
		return html

	def get_soup(self, url):
		req_header = {
			'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding': r'gzip,deflate,sdch',
			#'Accept-Language': r'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
			#'Cache-Control': r'max-age=0',
			#'Connection': r'keep-alive',
			#'Host': r'car.autohome.com.cn',
			'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
			'Referer': None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
		}
		html = self.get_html(url, req_header)
		soup = BeautifulSoup(html)
		return soup

def fake_car():
	c = crawler()
	url = r"http://car.autohome.com.cn/"
	soup = c.get_soup(url)
	print soup.find_all('a')

if __name__ == '__main__':
	fake_car()