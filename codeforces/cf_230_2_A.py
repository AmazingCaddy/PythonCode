#!/usr/bin/env python
#coding: utf-8

import sys
def main():
	in_str = raw_input()
	'nineteen'
	#in_str = 'ihimeitimrmhriemsjhrtjtijtesmhemnmmrsetmjttthtjhnnmirtimne'
	n_num = in_str.count('n')
	i_num = in_str.count('i')
	e_num = in_str.count('e')
	t_num = in_str.count('t')
	#print n_num, i_num, e_num, t_num
	ans = 0
	while True:
		if n_num >= 3 and i_num >= 1 and e_num >= 3 and t_num >= 1:
			ans += 1
			n_num -= 2
			i_num -= 1
			e_num -= 3
			t_num -= 1
		else:
			break
	print ans

if __name__ == '__main__':
	main()