#!/usr/bin/env python
#coding: utf-8

from bs4 import BeautifulSoup
import urllib, urllib2
import re
import hashlib

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

def check_image(problemid):
	base_url = 'http://www.acm.cs.ecnu.edu.cn/problem.php'
	params = {
		'problemid': problemid
	}
	html = urllib2.urlopen(base_url, urllib.urlencode(params))
	html_string = html.read()
	soup = BeautifulSoup(html_string, 'lxml', from_encoding='gb2312')
	tables = soup.find_all('table')
	if len(tables) >= 2 and tables[1].find_all('img'):
		print problemid
	
def fetch(url):
	html = urllib2.urlopen(url)
	html_string = html.read()
	soup = BeautifulSoup(html_string, 'lxml', from_encoding='utf-8')
	links = soup.find_all('a')
	res = dict()
	cnt = 0
	for li in links:
		if 'href' in li.attrs:
			ref = li.attrs['href']
			#print ref
			if re.match(r'http://www\.baike\.com/wiki.*', ref):
				cnt += 1
				m = hashlib.md5()
				m.update(ref)
				md5_code = m.hexdigest()
				res[md5_code] = ref
	print len(res), cnt
	return res

def test (num):
	num += 1

if __name__ == '__main__':
	#url = r'http://www.baike.com/wiki/%E8%BE%BD%E5%A4%AA%E5%AE%97'
	#print urllib.unquote(url)
	url = r'http://www.baike.com/wiki/%E5%94%90%E5%A5%95%5B%E6%B8%B8%E6%B3%B3%E8%BF%90%E5%8A%A8%E5%91%98%5D'
	fetch(url)
	