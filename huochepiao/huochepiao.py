#encoding:utf-8
import urllib2, urllib, httplib
import json
import platform
import re
import time

import stations

def get_platform_encoding():
	platform_encoding = 'utf-8'
	if platform.system() not in ['Linux', 'Darwin']:
		platform_encoding = 'gbk'
	return platform_encoding

def get_url(params):
	'''
		params:
		train_date:
		from_station:
		to_station:
		purpose_codes:
	'''
	url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%(train_date)s&leftTicketDTO.from_station=%(from_station)s&leftTicketDTO.to_station=%(to_station)s&purpose_codes=%(purpose_codes)s"
	request = url % params
	#print request
	r = urllib.urlopen(request)
	rlt = json.loads(r.read())
	result = rlt['data']
	#print result
	if result and isinstance(result, list):
		for l in result:
			if l['queryLeftNewDTO']['canWebBuy'] == 'Y':
				print l['queryLeftNewDTO']['station_train_code']

def validate_station(station_name):
	for station in stations.stations:
		if station_name == station['station_name']:
			return station['station_code']
	return False

def is_leap_year(year):
	return (year % 400 == 0) if (year % 100 == 0) else (year % 4 == 0)

def validate_date(date):
	prog = re.compile('\d\d\d\d-\d\d-\d\d')
	result = prog.match(date)
	if result == None:
		return False
	dates = date.split('-')
	yy = int(dates[0])
	mm = int(dates[1])
	dd = int(dates[2])
	if mm not in range(1, 13):
		return False
	monthes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	d = monthes[mm] + int(is_leap_year(yy))
	return 1 <= dd and dd <= d

def main():
	today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	platform_encoding = get_platform_encoding()
	start_station_str = u'请输入正确的出发火车站名: '.encode(platform_encoding)
	end_station_str = u'请输入正确的到达火车站名: '.encode(platform_encoding)
	train_date_str = (u'请输入出发日期(YYYY-MM-DD, e.g., ' + unicode(today) + u'): ').encode(platform_encoding)
	purpose_codes_str = u'是否学生票(Y/N): '.encode(platform_encoding)
	con_message = u'是否继续查询(Y/N) '.encode(platform_encoding)
	error_message = u'输入格式错误'.encode(platform_encoding)

	while True:
		while True:
			start_station = raw_input(start_station_str)
			start_station = start_station.decode(platform_encoding)
			from_station = validate_station(start_station)
			if from_station:
				break
			print error_message

		while True:
			end_station = raw_input(end_station_str)
			end_station = end_station.decode(platform_encoding)
			to_station = validate_station(end_station)
			if to_station:
				break
			print error_message

		while True:
			train_date = raw_input(train_date_str)
			train_date = train_date.decode(platform_encoding)
			if (validate_date(train_date)):
				break
			print error_message
		
		while True:
			purpose_codes = raw_input(purpose_codes_str)
			purpose_codes = purpose_codes.decode(platform_encoding)
			if purpose_codes in ['Y', 'y', 'N', 'n']:
				break
			print error_message

		if purpose_codes in ['y', 'Y']:
			purpose_codes = '0X00'
		else:
			purpose_codes = 'ADULT'

		params = {
			'train_date': train_date,
			'from_station': from_station,
			'to_station': to_station,
			'purpose_codes': purpose_codes	#ADULT
		}
		#print params
		get_url(params)
		con_message = raw_input(con_message)
		if con_message not in['Y', 'y']:
			break

if __name__ == '__main__':
	main()
	#get_url('')