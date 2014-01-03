#!/usr/bin/env python
#coding: utf-8

import sys
def main():
	s = map(int, sys.stdin.readline().strip().split())
	n = s[0]
	m = s[1]
	a = s[2]
	ans = ((n + a - 1) / a) * ((m + a - 1) / a)
	print ans

if __name__ == '__main__':
	main()