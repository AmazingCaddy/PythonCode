#!/usr/bin/env python
#coding: utf-8

import sys

def find(k, num, vis):
	for i in xrange(len(num)):
		if vis[i] == 0 and num[i] > k:
			vis[i] = 1
			return i
	return len(num)

def warOne(naomi, ken, n):
	vis = [0 for i in xrange(n)]
	cnt = 0
	for i in xrange(n):
		j = find(naomi[i], ken, vis)
		if j == n:
			break
		else:
			cnt = cnt + 1
	return n - cnt

def warTwo(naomi, ken, n):
	n_l = 0
	n_r = n - 1
	k_l = 0
	k_r = n - 1
	cnt = 0
	for i in xrange(n):
		if naomi[n_l] > ken[k_l]:
			cnt = cnt + 1
			n_l = n_l + 1
			k_l = k_l + 1
		else:
			n_l = n_l + 1
			k_r = k_r - 1
	return cnt

def solve(t):
	n = input()
	naomi = map(float, sys.stdin.readline().strip().split())
	ken = map(float, sys.stdin.readline().strip().split())
	naomi.sort()
	ken.sort()
	#print naomi
	#print ken
	print "Case #%d:" % t, warTwo(naomi, ken, n), warOne(naomi, ken, n)

def main():
	case = input()
	for t in xrange(0, case):
		solve(t + 1)

if __name__ == "__main__":
	main()
	#print D(0)