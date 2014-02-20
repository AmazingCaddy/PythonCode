#!/usr/bin/env python
#coding: utf-8

import sys

def main():
	protein = list(raw_input())
	ans = 0
	cnt = 1
	for i in range(1, len(protein)):
		if protein[i] != protein[i - 1]:
			if cnt % 2 == 0:
				ans += 1
			cnt = 1
		else:
			cnt += 1
	if cnt % 2 == 0:
		ans += 1
	print ans

if __name__ == '__main__':
	main()