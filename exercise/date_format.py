#!/usr/bin/env python
#coding: utf-8

months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
]

ending = ['st', 'nd', 'rd'] + 17 * ['th'] \
		+ ['st', 'nd', 'rd'] + 7 * ['th'] \
		+ ['st']

def date_format ():
	year 	=	raw_input ('Year: ')
	month 	=	raw_input ('Month: ')
	day		=	raw_input ('Day (1-31): ')

	month_number = int(month)
	day_number = int(day)

	month_name = months[month_number - 1]
	ordinal = day + ending[day_number - 1]

	print month_name + ' ' + ordinal + ', ' + year

if __name__ == '__main__' :
	date_format()
