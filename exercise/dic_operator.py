#!/usr/bin/env python
#coding: utf-8

phonebook = {'Alice': '2341', 'Beth': '9012', 'Cecil': '3258'}
print phonebook

items = [('name', 'Gumy'), ('age', 21)]
d = dict(items)
print d

x = {}
x[42] = 'wenbin'
print x

people = {
	'Alice': {
		'phone': '2341',
		'addr': 'Foo drive 23'
	},
	'Beth': {
		'phone': '9102',
		'addr': 'Bar street 42'
	},
	'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}
}
#  python 蟒蛇

labels = {
	'phone': 'phone number',
	'addr': 'address'
}

'''
name = raw_input('Name: ')
request = raw_input('phone number(p) or address(a)?')
if request == 'p':
	key = 'phone'
if request == 'a':
	key = 'addr'

if name in people:
	print "%s's %s is %s." % (name, labels[key], people[name][key])
'''

line = raw_input()
print line.strip().split()


