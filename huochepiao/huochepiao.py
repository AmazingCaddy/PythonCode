#encoding:utf-8
import urllib2, urllib, httplib
import json
import platform
import re
import time

import DetectCode, Stations, Train, Validate, Ticket

def get_all_tickets(params):
	'''
		params:
		train_date:
		from_station:
		to_station:
		purpose_codes:
	'''
	url_params = {
		'leftTicketDTO.train_date':	params['train_date'],
		'leftTicketDTO.from_station': params['from_station'],
		'leftTicketDTO.to_station': params['to_station'],
		'purpose_codes': params['purpose_codes']
	}
	#urllib.urlencode(url_params)
	url_list = [
		'https://kyfw.12306.cn/otn/leftTicket/query?', 
		'leftTicketDTO.train_date=',
		'%(train_date)s',
		'&leftTicketDTO.from_station=',
		'%(from_station)s',
		'&leftTicketDTO.to_station=',
		'%(to_station)s',
		'&purpose_codes=',
		'%(purpose_codes)s'
	]
	
	request_url = ''.join(url_list) % params
	print request_url

	''' for debug log '''
	#httpHandler = urllib2.HTTPHandler(debuglevel=1)
	#httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
	#opener = urllib2.build_opener(httpHandler, httpsHandler)
	#urllib2.install_opener(opener)

	request = urllib2.Request(request_url)
	
	try:
		response = urllib2.urlopen(request)
	except urllib2.HTTPError, e:
		print e.code

	print time.time()
	
	json_string = response.read()
	print time.time()
	
	rlt = json.loads(json_string)

	results = rlt['data']

	tickets = list()
	if results and isinstance(results, list):
		for res in results:
			ticket = Ticket.Ticket(res['queryLeftNewDTO'])
			tickets.append(ticket)
	#		if l['queryLeftNewDTO']['canWebBuy'] == 'Y':
	#			print l['queryLeftNewDTO']['station_train_code']
	return tickets

def get_all_canbuy_tickets(tickets):
	canbuy_tickets = list()
	for ticket in tickets:
		if ticket.getPropertyByName('canWebBuy') == 'Y':
			canbuy_tickets.append(ticket)
	return canbuy_tickets

def print_tickets(tickets):
	'''
		"gg_num": "--",	
		"gr_num": "--",	高级软卧
		"qt_num": "--",	其他
		"rw_num": "8",	软卧
		"rz_num": "--",	软座
		"tz_num": "--",	特等座
		"wz_num": "有",	无座
		"yb_num": "--",	
		"yw_num": "有",	硬卧
		"yz_num": "有",	硬座
		"ze_num": "--",	二等座
		"zy_num": "--",	一等座
		"swz_num": "--"	商务座
	'''
	platform_encoding = DetectCode.get_platform_encoding()
	number = 0
	for ticket in tickets:
		number += 1
		out = list()
		out.append('%-4d' % number)
		out.append(ticket.getPropertyByName('station_train_code').encode(platform_encoding))
		out.append('%s(%s)' % (ticket.getPropertyByName('from_station_name').encode(platform_encoding), ticket.getPropertyByName('start_time').encode(platform_encoding)))
		out.append('%s(%s)' % (ticket.getPropertyByName('to_station_name').encode(platform_encoding), ticket.getPropertyByName('arrive_time').encode(platform_encoding)))
		out.append('全程:(%s)' % ticket.getPropertyByName('lishi').encode(platform_encoding))
		format = '%s%-8s%s -> %s %s\t' % tuple(out)
		print format
	pass

def get_all_stations(params):
	'''
		train_no:
		from_station_telecode:
		to_station_telecode:
		depart_date:
	'''
	url_list = [
		'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?',
		'train_no=',
		'%(train_no)s',
		#'5l000D320171',
		'&from_station_telecode=',
		'%(from_station_telecode)s',
		#'AOH',
		'&to_station_telecode=',
		'%(to_station_telecode)s'
		#'NGH',
		'&depart_date=',
		'%(depart_date)s'
		#'2014-01-04'
	]
	request = ''.join(url_list) % params

def main():
	today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	platform_encoding = DetectCode.get_platform_encoding()
	from_station_str = u'出发火车站名: '.encode(platform_encoding)
	to_station_str = u'到达火车站名: '.encode(platform_encoding)
	train_date_str = (u'出发日期(YYYY-MM-DD, e.g., ' + unicode(today) + u'): ').encode(platform_encoding)
	purpose_codes_str = u'是否学生票(Y/N): '.encode(platform_encoding)
	con_message = u'是否继续查询(Y/N) '.encode(platform_encoding)
	error_message = {
		'station_not_exist': u'该火车站不存在，请输入正确的'.encode(platform_encoding),
		'date_format': u'日期格式错误，请重新输入'.encode(platform_encoding)
	}

	while True:
		message = '请输入'
		while True:
			from_station = raw_input(message + from_station_str)
			from_station = from_station.decode(platform_encoding)
			from_station_info = Validate.validate_station(from_station)
			if from_station_info:
				break
			message = error_message['station_not_exist']
			#print error_message

		message = '请输入'
		while True:
			to_station = raw_input(message +to_station_str)
			to_station = to_station.decode(platform_encoding)
			to_station_info = Validate.validate_station(to_station)
			if to_station_info:
				break
			message = error_message['station_not_exist']
			#print error_message

		message = '请输入'
		while True:
			train_date = raw_input(message +train_date_str)
			train_date = train_date.decode(platform_encoding)
			if (Validate.validate_date(train_date)):
				break
			message = error_message['date_format']
			#print error_message
		
		#message = '请输入'
		while True:
			purpose_codes = raw_input(purpose_codes_str)
			purpose_codes = purpose_codes.decode(platform_encoding)
			if purpose_codes in ['Y', 'y', 'N', 'n']:
				break
			#print error_message

		if purpose_codes in ['y', 'Y']:
			purpose_codes = '0X00'
		else:
			purpose_codes = 'ADULT'

		params = {
			'train_date': train_date,
			'from_station': from_station_info['station_code'],
			'to_station': to_station_info['station_code'],
			'purpose_codes': purpose_codes	#ADULT
		}
		#print params
		tickets = get_all_tickets(params)
		canbuy_tickets = get_all_canbuy_tickets(tickets)

		print_tickets(canbuy_tickets)

		con_message = raw_input(con_message)
		if con_message not in['Y', 'y']:
			break

if __name__ == '__main__':
	main()
	#get_url('')