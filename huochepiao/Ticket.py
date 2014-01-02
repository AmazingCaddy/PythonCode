#encoding:utf-8
import copy

class Ticket(object):
	'''
		e.g.
		"train_no": "1100000K7500",
		"station_train_code": "K75",
		"start_station_telecode": "CCT",
		"start_station_name": "长春",
		"end_station_telecode": "NGH",
		"end_station_name": "宁波",
		"from_station_telecode": "SNH",
		"from_station_name": "上海南",
		"to_station_telecode": "NGH",
		"to_station_name": "宁波",
		"start_time": "05:18",
		"arrive_time": "09:43",
		"day_difference": "0",
		"train_class_name": "",
		"lishi": "04:25",
		"canWebBuy": "Y",
		"lishiValue": "265",
		"yp_info": "1005053219401525000810050500653010150098",
		"control_train_day": "20300303",
		"start_train_date": "20140110",
		"seat_feature": "W3431333",
		"yp_ex": "10401030",
		"train_seat_feature": "3",
		"seat_types": "1413",
		"location_code": "T2",
		"from_station_no": "35",
		"to_station_no": "41",
		"control_day": 67,
		"sale_time": "0800",
		"is_support_card": "0",
		"gg_num": "--",
		"gr_num": "--",
		"qt_num": "--",
		"rw_num": "8",
		"rz_num": "--",
		"tz_num": "--",
		"wz_num": "有",
		"yb_num": "--",
		"yw_num": "有",
		"yz_num": "有",
		"ze_num": "--",
		"zy_num": "--",
		"swz_num": "--"
	'''
	def __init__(self, arg):
		super(Ticket, self).__init__()
		self.__hashmap = arg

	def getProperties(self):
		return copy.deepcopy(self.__hashmap)

	def getPropertyByName(self, name):
		if self.__hashmap.has_key(name):
			return copy.deepcopy(self.__hashmap[name])
		return None

	def setPropertyByName(self, name, value):
		if self.__hashmap.has_key(name):
			self.__hashmap[name] = value
			return True
		return False
