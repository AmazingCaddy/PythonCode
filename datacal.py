#!/usr/bin/env python
#coding: utf-8

import re
import time
from datetime import datetime

KENDO1 = 1
SCHEMA_DATA = 2
KENDO2 = 3
RESIZE_GRID_HEIGHT = 4
HIDE_GRID_LOADING_ICON = 6
KPI_GRID_VIEW_ON_DATA_BOUND = 230
BIND_TO_DATA_BOUND_EVENT = 232
BIND_ON_GRID_DATA_BOUND_EVENT = 235
ACCOUNTS_VIEW_BIND_GRID_EVENTS = 237
JQUERY_OR_KENDO = 241
process_map = dict()
"""
kendo1
schema.data
kendo2
ResizeGridHeight
HideGridLoadingIcon
KpiGridView.OnDataBound
BindToDataBoundEvent
BindOnGridDataboundEvent
AccountsView.BindGridEvents
jQueryOrKendo

"""

def solve_time(datetime_string):
	format = "%Y-%m-%d %H:%M:%S.%f"
	dt = datetime.strptime(datetime_string, format)
	result = int(time.mktime(dt.timetuple())) * 1000 + dt.microsecond / 1000
	return result

def get_time(date, time):
	return solve_time(" ".join([date, time]))

def solve_file(fp):
	logs = list();
	for line in fp:
		lines = line.strip("\n").split(" ")
		logs.append(lines)
	return logs

def solve_log(log):
	keys = ["dt", "jsf", "func", "tag", "ms"]
	values = [" ".join(log[0:2])] + log[2:6]
	return dict(zip(keys, values))

def solve_logs(logs):
	dict_logs = list()
	for log in logs:
		#if len(log) > 5:
		if len(log) == 5:
			log.append('0')
		dic = solve_log(log)
		dict_logs.append(dic)
	return dict_logs

def get_delta_time(log_pre, log_cur):
	return solve_time(log_cur["dt"]) - solve_time(log_pre["dt"])

def get_loop_time(logs):
	log_length = len(logs)
	if log_length != 37 * 6:
		return -1
	loops = list()
	for i in xrange(0, 37):
		first = i * 6 + 2
		second = i * 6 + 4
		sub_total = i * 6 + 5
		loops.append((i, int(logs[first]["ms"]), int(logs[second]["ms"]), int(logs[sub_total]["ms"])))
	return loops

def solve_optimized(fp):
	pass

def solve_original(fp):
	logs = solve_file(fp)
	logs = solve_logs(logs)

	#for log in logs:
	#	print log

	sub_totals = list()
	total_time = 0
	
	during_time = get_delta_time(logs[KENDO1 - 1], logs[KENDO1])
	total_time += during_time
	sub_totals.append(("kendo1", during_time))

	during_time = int(logs[SCHEMA_DATA]["ms"])
	total_time += during_time
	sub_totals.append(("schema.data", during_time))
	
	during_time = get_delta_time(logs[KENDO2 - 1], logs[KENDO2])
	total_time += during_time
	sub_totals.append(("kendo2", during_time))
	
	during_time = int(logs[RESIZE_GRID_HEIGHT]["ms"])
	total_time += during_time
	sub_totals.append(("ResizeGridHeight", during_time))
	
	during_time = int(logs[HIDE_GRID_LOADING_ICON]["ms"])
	total_time += during_time
	sub_totals.append(("HideGridLoadingIcon", during_time))
	
	during_time = int(logs[KPI_GRID_VIEW_ON_DATA_BOUND]["ms"])
	total_time += during_time
	sub_totals.append(("KpiGridView.OnDataBound", during_time))
	
	during_time = int(logs[BIND_TO_DATA_BOUND_EVENT]["ms"])
	total_time += during_time
	sub_totals.append(("BindToDataBoundEvent", during_time))
	
	during_time = int(logs[BIND_ON_GRID_DATA_BOUND_EVENT]["ms"])
	total_time += during_time
	sub_totals.append(("BindOnGridDataboundEvent", during_time))
	
	during_time = int(logs[ACCOUNTS_VIEW_BIND_GRID_EVENTS]["ms"])
	total_time += during_time
	sub_totals.append(("AccountsView.BindGridEvents", during_time))
	
	during_time = get_delta_time(logs[JQUERY_OR_KENDO - 1], logs[JQUERY_OR_KENDO])
	total_time += during_time
	sub_totals.append(("jQueryOrKendo", during_time))
	
	sub_totals.append(("total", total_time))

	during_time = int(logs[JQUERY_OR_KENDO]["ms"])
	sub_totals.append(("actually", during_time))
	
	for sub_total in sub_totals:
		print "%d" % sub_total[1]

	loop_time = get_loop_time(logs[8: 8 + 222])


def main():
	filepath = "F:\\code\\inputs\\"
	#filename = "accounts_020rows_01.txt"
	rows = ["020", "050", "100", "200", "500"]
	cols = ["01", "02", "03", "04", "05"]
	for r in rows:
		for c in cols:
			filename = filepath + "accounts_" + r + "rows_" + c + ".txt"
			fp = open(filename, 'r')
			solve_original(fp)
			print ""


if __name__ == '__main__':
	main()