#!/usr/bin/env python
#coding: utf-8

import threading

import time, sys

class Thread(threading.Thread):
	def __init__(self, func, args, name = ""):
		super(Thread, self).__init__()
		self.__name = name
		self.__func = func
		self.__args = args
		self.__result = list()

	def run(self):
		self.__result = self.__func(*self.__args)
		self.__result['thread_name'] = self.__name

	def get_result(self):
		return self.__result

class MultiThreads(object):
	def __init__(self, func_list, args_list = None, name_list = None):
		super(MultiThreads, self).__init__()
		self.__func_list = func_list
		self.__args_list = list() if args_list is None else args_list
		self.__name_list = list() if name_list is None else name_list
		self.__results = list()
	
	def start(self):
		func_len = len(self.__func_list)
		args_len = len(self.__args_list)
		name_len = len(self.__name_list)
		
		for i in xrange(args_len, func_len):
			self.__args_list.append(())
		for i in xrange(name_len, func_len):
			self.__name_list.append(self.__func_list[i].__name__ + '_' + str(i))

		threads = list()
		for i in xrange(func_len):
			t = Thread(self.__func_list[i], self.__args_list[i], self.__name_list[i])
			threads.append(t)
		for t in threads:
			t.start()
		for t in threads:
			t.join()

		for t in threads:
			self.__results.append(t.get_result())
	
	def get_results(self):
		return self.__results
		
def loop(nloop = -1, nsec = 6):
	print 'loop', nloop, 'start at:', time.ctime()
	print 'loop %d hang up for %d s' % (nloop, nsec)
	time.sleep(nsec)
	print 'loop', nloop, 'done at:', time.ctime()

def main():
	print 'main thread start!'
	threads = []
	loops = [4, 2]
	nloops = range(len(loops))
	func_list = list()
	args_list = list()
	name_list = list()
	for i in nloops:
		func_list.append(loop)
		args_list.append((i, loops[i]))
		name_list.append(loop.__name__)
	func_list.append(loop)
	mts = MultiThreads(func_list, args_list, name_list)
	mts.start()
	print 'all done at:', time.ctime()

if __name__ == '__main__':
	main()