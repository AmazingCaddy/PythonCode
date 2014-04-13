#!/usr/bin/env python
#coding: utf-8

import sys

def solve(t):
	row1 = input()
	m1 = []
	for i in xrange(0, 4):
		m1.append(map(int, sys.stdin.readline().strip().split()))
	row2 = input()
	m2 = []
	for i in xrange(0, 4):
		m2.append(map(int, sys.stdin.readline().strip().split()))
	s1 = set(m1[row1 - 1])
	s2 = set(m2[row2 - 1])
	s = list(s1 & s2)
	if len(s) == 1:
		print "Case #%d: %d" % (t, s[0])
	elif len(s) > 1:
		print "Case #%d: Bad magician!" % t
	else:
		print "Case #%d: Volunteer cheated!" % t

def main():
	case = input()
	for i in xrange(0, case):
		solve(i + 1)

if __name__ == "__main__":
	main()