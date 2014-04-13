#!/usr/bin/env python
#coding: utf-8

import sys

eps = 1e-8

def D(x):
	global eps
	return -1 if x < -eps else 0 if x < eps else 1

def solve(t):
	global eps
	m = map(float, sys.stdin.readline().strip().split())
	C = m[0]
	F = m[1]
	X = m[2]
	v = 2
	ans = 0
	while True:
		if (X / v) < (C / v + X / (v + F)):
			ans = ans + X / v
			break
		else:
			ans = ans + C / v
			v = v + F
	print "Case #%d: %.8f" % (t, ans)

def main():
	case = input()
	for t in xrange(0, case):
		solve(t + 1)

if __name__ == "__main__":
	main()
	#print D(0)