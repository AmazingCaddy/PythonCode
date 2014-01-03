#!/usr/bin/env python
#coding: utf-8

def Operator():
	x = int(raw_input('Enter x: '))
	y = int(raw_input('Enter y: '))

	print 'x + y  = ' + str(x + y)
	print 'x - y  = ' + str(x - y)
	print 'x * y  = ' + str(x * y)
	print 'x / y  = ' + str(x / y)
	print 'x // y = ' + str(x // y)
	print 'x % y  = ' + str(x % y)
	print 'x ** y = ' + str(x ** y)
	print 'x & y  = ' + str(x & y)
	print 'x | y  = ' + str(x | y)
	print 'x ^ y  = ' + str(x ^ y)
	print '~x ~y  = ' + str(~x) + ' ' + str(~y)
	print 'not x  = ' + str(not x)
	
if __name__ == '__main__':
	Operator()