#!/usr/bin/env python
#coding: utf-8

import Stations
import urllib
import Ticket
import types

def url_test():
	out = [
		('K75', '上海南', '宁波'),
		('D2287', '上海虹桥', '宁波')
	]
	print '%15s' % '(12:22)'
	print '%16s' % '上(12:22)'
	print '%17s' % '上海(12:22)'
	print '%18s' % '上海南(12:22)'
	print '%19s' % '上海虹桥(07:00)'
	#print '%22s' % '上海虹桥哈(07:00)'
	format_str = '%%%ds(%%s)' % (len(out[1])*2)
	print format_str
	for o in out:
		print '%-6s\t%s\t-> %-5s' % o

def main():
	stations_dict = dict()
	for station in Stations.stations:
		stations_dict[station['station_name']] = station
	print 'stations_dict = {'
	count = 0
	for key, val in stations_dict.items():
		if count:
			print ','
		else:
			count = 1
		print ('u"' + key + '":{').encode('utf-8')
		cnt = 0
		for k, v in val.items():
			if cnt:
				print ','
			else:
				cnt = 1
			print ('u"' + k + '":u"' + v + '"').encode('utf-8')
		print '}'
	print '}'

def test():
	ticket = Ticket.Ticket({'xx' : 'yy'})
	print type(ticket)
	if isinstance(ticket, Ticket.Ticket):
		print 'OK'
if __name__ == '__main__':
	#test()
	#main()
	url_test()