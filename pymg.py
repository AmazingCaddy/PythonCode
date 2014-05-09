#!/usr/bin/env python
#coding: utf-8

import sys
import json

try:
	import pymongo
	import wwbcom
	from bson.objectid import ObjectId
except ImportError:
	sys.exit("Exceptions.ImportError: No module named pymongo\n")

class pymg(object):
	""" pydo is a class for mongodb operation """
	def __init__(self, config):
		super(pymg, self).__init__()
		params = dict()
		params['host'] = config['host'] if config.has_key('host') else 'localhost'
		params['port'] = config['port'] if config.has_key('port') else 27017
		params['db'] = config['db'] if config.has_key('db') else 'test'
		params['debug'] = config['debug'] if config.has_key('debug') else False

		self.__params = params
		self.__conn = None
		self.__db = None

	def __connect(self):
		if self.__conn:
			return
		try:
			self.__conn = pymongo.Connection(
				host = self.__params['host'],
				port = self.__params['port']
			)
			self.__db = self.__conn[self.__params['db']]
		except pymongo.errors.ConnectionFailure as e:
			self.__handle_error(e)

	def switch_db(self, dbname):
		self.__connect()
		self.__db = self.__conn[dbname]

	def find_one(self, collection, conditions = {}, fields = None):
		self.__connect()
		if isinstance(fields, dict):
			return self.__db[collection].find_one(conditions, fields)
		return self.__db[collection].find_one(conditions)
	
	def find(self, collection, conditions = {}, fields = None):
		self.__connect()
		if isinstance(fields, dict):
			return self.__db[collection].find(conditions, fields)
		return self.__db[collection].find(conditions)

	def insert(self, collection, entity):
		self.__connect()
		try:
			self.__db[collection].insert(entity)
			return self.run_command('getLastError')['n']
		except pymongo.errors.DuplicateKeyError as e:
			self.__handle_error(e)
		except pymongo.errors.PyMongoError as e:
			self.__handle_error(e)
		return False

	def update(self, collection, entity, conditions = {}, multiline = False):
		'''
			$set			指定一个键的值，如果没有会创建
			$unset	
			$inc			不存在的会自动创建，键值必须是数字
			$push and $pop	数组修改器
			$				定位修改器
			$ne				一个值不在数组中，才会加进去
			$addToSet		可以避免重复的问题
			$each			结合addToSet可以一次添加多个值
			$pull
		'''
		self.__connect()
		try:
			self.__db[collection].update(conditions, entity, multi = multiline)
			return self.run_command('getLastError')['n']
		except pymongo.errors.PyMongoError as e:
			self.__handle_error(e)
		return False

	def upsert(self, collection, entity, conditions = {}, multiline = False):
		self.__connect()
		try:
			self.__db[collection].update(conditions, entity, upsert = True, multi = multiline)
			return self.run_command('getLastError')['n']
		except pymongo.errors.PyMongoError as e:
			self.__handle_error(e)
		return False

	def remove(self, collection, conditions = {}):
		self.__connect()
		self.__db[collection].remove(conditions)

	def run_command(self, command):
		self.__connect()
		try:
			res = self.__db.command(command)
			return res
		except pymongo.errors.OperationFailure as e:
			self.__handle_error(e)
		return False

	def get_id(self, oid):
		return self.__get_id(oid)

	def __handle_error(self, e):
		if self.__params['debug']:
			wwbcom.print_error(e)
		else:
			raise e

	def __get_id(self, oid):
		return ObjectId(oid)

def test():
	config = {'host': 'localhost', 'port': 27017, 'debug': True}
	pym = pymg(config)
	#entity = {'_id': pym.get_id('536c6e6d3d4ebd1058764b28')}
	#print(pym.find('users', entity))
	res = pym.upsert('math', {"$inc": {'count': 3}}, {'count': 0})
	print res
	#res = pym.find_one('users')
	res = pym.update('users', {'$set': {'test': 'test_data'}}, {}, multiline=True)
	print res
	#res = pym.run_command('buildInfo')
	#res = pym.run_command({'collStats': 'users'})
	#res = pym.run_command('getLastError')
	#print(res)

if __name__ == '__main__':
	test()