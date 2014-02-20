#!/usr/bin/env python
#coding: utf-8

import sys
def main():
	n = int(raw_input())
	m = []
	for i in range(n):
		m.append(map(int, sys.stdin.readline().strip().split()))
	for i in range(n):
		for j in range(n):
			print "%.6f" % ((m[i][j] + m[j][i]) / 2.0),
		print
	for i in range(n):
		for j in range(n):
			print "%.6f" % ((m[i][j] - m[j][i]) / 2.0),
		print

if __name__ == '__main__':
	main()