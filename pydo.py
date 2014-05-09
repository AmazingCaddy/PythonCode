#!/usr/bin/env python
#coding: utf-8

import sys

try:
	import MySQLdb
	import common
except ImportError:
	sys.exit("Exceptions.ImportError: No module named MySQLdb\n")

class pydo(object):
	""" pydo is a class for mysql operation """
	def __init__(self, config):
		super(pydo, self).__init__()
		
		params = dict()
		params['host'] = config['host'] if config.has_key('host') else 'localhost'
		params['port'] = config['port'] if config.has_key('port') else 3306
		params['user'] = config['user'] if config.has_key('user') else 'root'
		params['passwd'] = config['passwd'] if config.has_key('passwd') else '123456'
		params['db'] = config['db'] if config.has_key('db') else 'mysql'
		params['charset'] = config['charset'] if config.has_key('charset') else 'utf8'
		params['use_unicode'] = config['use_unicode'] if config.has_key('use_unicode') else True
		params['debug'] = config['debug'] if config.has_key('debug') else False

		self.__params = params
		self.__conn = None
		self.__cursor = None
		#self.__in_transaction = False

	def __del__(self):
		self.__close()

	def __connect(self):
		if self.__conn:
			return
		try:
			self.__conn = MySQLdb.connect(
				host = self.__params['host'],
				port = self.__params['port'],
				user = self.__params['user'],
				passwd = self.__params['passwd'],
				db = self.__params['db'],
				charset = self.__params['charset'],
				use_unicode = self.__params['use_unicode']
			)
			self.__conn.autocommit(False)
			self.__cursor = self.__conn.cursor(MySQLdb.cursors.DictCursor)
		except MySQLdb.Error as e:
			self.__handle_error(e)
	
	def execute(self, sql, params = None):
		self.__connect()
		if isinstance(params, list):
			params = tuple(params)
		try:
			self.__cursor.execute(sql, params)
			return True
		except MySQLdb.Error as e:
			self.__handle_error(e)
		return False

	def insert(self, table_name, entity, auto_increment = True):
		columns = entity.keys()
		prefix = "".join(['INSERT INTO `',table_name,'`'])
		fields = ",".join(["".join(['`', column, '`']) for column in columns])
		values = ",".join(["%s" for i in range(len(columns))])
		sql = "".join([prefix, "(", fields, ") VALUES (", values, ")"])
		params = [entity[key] for key in columns]
		if self.execute(sql, params):
			if auto_increment:
				return self.__cursor.lastrowid
			return self.__cursor.rowcount
		return False

	def update(self, table_name, entity, conditions = None):
		columns = entity.keys()
		prefix = "".join(['UPDATE `', table_name, '` SET '])
		fields = ",".join(["`%s`=%%s" % column for column in columns])
		params = [entity[key] for key in columns]
		if conditions:
			con_keys = conditions.keys()
			cond = "".join([' WHERE ', " and ".join(["`%s`=%%s" % key for key in con_keys])])
			params = params + [conditions[key] for key in con_keys]
		else:
			cond = ''
		sql = "".join([prefix, fields, cond])
		if self.execute(sql, params):
			return self.__cursor.rowcount
		return False

	def get_all(self, sql, params = None):
		self.execute(sql, params)
		return self.__cursor.fetchall()

	def get_row(self, sql, params = None):
		self.execute(sql, params)
		return self.__cursor.fetchone()
	
	def get_one(self, sql, params = None):
		self.execute(sql, params)
		res = self.__cursor.fetchone()
		#print self.__cursor.description
		''' first row first column '''
		return res[self.__cursor.description[0][0]]
	
	def select_db(self, dbname):
		try:
			self.__conn.select_db(dbname)
		except MySQLdb.Error as e:
			self.__handle_error(e)

	def commit(self):
		self.__conn.commit()

	def rollback(self):
		self.__conn.rollback()

	def close(self):
		self.__close()

	def __close(self):
		try:
			if self.__cursor:
				self.__cursor.close()
		except MySQLdb.Error as e:
			self.__handle_error(e)
		finally:
			self.__cursor = None			
			try:
				if self.__conn:
					self.__conn.close()
			except MySQLdb.Error as e:
				self.__handle_error(e)
			finally:
				self.__conn = None

	def __handle_error(self, e):
		#if self.__in_transaction:
		self.__conn.rollback()
		if self.__params['debug']:
			common.print_error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
		else:
			raise e

def test():
	config = {'debug': True}
	pym = pydo(config)
	pym.execute('''DROP DATABASE IF EXISTS `test`;''')
	pym.execute('''create database test;''')
	pym.execute('''use test;''')
	pym.execute('''
		create TABLE `t1` (
			`id` BIGINT(20) not null AUTO_INCREMENT,
			`name` varchar(32),
			`age` int(11) not null,
			PRIMARY key(`id`)
		) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
	''')
	pym.execute('''
		create TABLE `t2` (
			`id` BIGINT(20) not null AUTO_INCREMENT,
			`notion` varchar(32),
			PRIMARY key(`id`)
		) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
	''')
	pym.insert('t1', {'name': 'Alice', 'age': 18})
	pym.insert('t1', {'name': 'Bob', 'age': 20})
	#pym.insert('t1', {'name': 'Bob', 'age': 21, 'id': 2})
	pym.commit()

	pym.insert('t2', {'notion': 'xx'})
	pym.insert('t2', {'notion': 'yy'})
	pym.commit()
	#pym.insert('')

if __name__ == "__main__":
	test()