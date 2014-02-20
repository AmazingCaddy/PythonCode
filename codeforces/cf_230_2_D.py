#!/usr/bin/env python
#coding: utf-8
'''
	dp[1][A][C] = min { 
		W[A][C],
		W[A][B] + W[B][C] 
	}
	dp[n][A][C] = min { 
		dp[n - 1][A][B] + W[A][C] + dp[n - 1][B][C],
		dp[n - 1][A][C] + W[A][B] + dp[n - 1][C][A] + W[B][C] + dp[n - 1][A][C]
	}
'''
import sys

def dfs(n, A, B, C, dp, w):
	if n == 0:
		return 0
	if dp[n][A][C] != 0:
		return dp[n][A][C]
	x = dfs(n - 1, A, C, B, dp, w) + w[A][C] + dfs(n - 1, B, A, C, dp, w)
	y = dfs(n - 1, A, B, C, dp, w) + w[A][B] + dfs(n - 1, C, B, A, dp, w) + w[B][C] + dfs(n - 1, A, B, C, dp, w)
	#print 'n = %d, A = %d, C = %d' %(n, A, C)
	#print '(x, y) = (%d, %d)' % (x, y) 
	dp[n][A][C] = min(x, y)
	return dp[n][A][C]

def get_tri(n, x, y):
	tri = [[[0 for i in range(y)] for j in range(x)] for k in range(n)]
	return tri

def main():
	w = list()
	for i in range(3):
		w.append(map(int, sys.stdin.readline().strip().split()))
	n = int(raw_input())
	dp = get_tri(n + 1, 3, 3)
	ans = dfs(n, 0, 1, 2, dp, w)
	print ans

if __name__ == '__main__':
	main()