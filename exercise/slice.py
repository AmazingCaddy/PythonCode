#!/usr/bin/env python
#coding: utf-8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 开区间 [a, b)
print numbers[3: 6]
# [4, 5, 6]

# 	0,	1, 		..., n-1
# 	-n, -(n-1),	..., -1
print numbers[-3: -1]
# [8, 9]

# 负数步长，从右到左提取元素
print numbers[11: 5: -1]

# 这样可以复制整个序列
tmp = numbers[:]
print tmp
tmp[0] = 10
print numbers

#
sequeues = [None] * 10
print sequeues

