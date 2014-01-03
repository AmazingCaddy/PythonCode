#!/usr/bin/env python
#coding: utf-8

num = [1, 2, 3, 4]
def dfs(depth):
	if (depth == 4):
		print num
		return
	for i in range (depth, 4):
		num[i], num[depth] = num[depth], num[i]
		dfs (depth + 1)
		num[i], num[depth] = num[depth], num[i]

def compare (a, b):
	return (-1 if a < b else (0 if a == b else 1))

def main():
	i, sum = 1, 0
	for i in xrange(100):
		sum = sum + i
	print sum

if __name__ == '__main__':
	dfs(0)
	#x = [4, 2, 0, 9, -10]
	#x.sort(cmp = compare)
	#print x