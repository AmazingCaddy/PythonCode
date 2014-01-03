#!/usr/bin/env python
#coding: utf-8

# string to list
hello_str = 'Hello'
print 'string to list: list(\'Hello\') is', list(hello_str)

# 修改列表 元素赋值
x = [1, 1, 1]
print 'original x is', x
x[1] = 2
print 'x[1] = 2, x is', x
print ''

# 删除元素
names = ['Alice', 'Beth', 'Ceil', 'Dee-Dee', 'Earl']
print 'original names is', names
del names[2]
print 'del names[2], names is', names
print ''

# 分片赋值
name = list('Perl')
print 'original name is', name
name[2:] = list('ar')
print 'name[2:] = list(\'ar\'), name is', name
print ''

name = list('Perl')
print 'original name is', name
name [1:] = list('ython')
print 'name [1:] = list(\'ython\'), name is', name
print ''

numbers = [1, 5]
print 'original numbers is', numbers
numbers[1:1] = [2, 3, 4]
print 'numbers[1:1] = [2, 3, 4], numbers is', numbers
numbers[1:4] = []
print 'numbers[1:4] = [], numbers is', numbers
print ''

# 列表方法
print 'the function of list:\n'
# append
print 'append function'
lst = [1, 2, 3]
print 'original lst is', lst
lst.append(4)
print 'lst.append(4), lst is', lst
print ''

# count
print 'count function'
count_array = ['to', 'be', 'or', 'not', 'to', 'be']
print count_array
print 'the count of \'to\' is', count_array.count('to')
print ''

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x
print 'the count of \'1\' is', x.count (1)
print 'the count of \'[1, 2]\' is', x.count ([1, 2])
print ''

#extend
print 'extend function'
a = [1, 2, 3]
b = [4, 5, 6]
print 'a =', a
print 'b =', b
a.extend (b)
print 'a.extend(b), a is', a
print ''

# index 索引一个不存在的值会扔出异常
print 'index function'
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print knights
print 'the index of \'who\' in knights is', knights.index('who')

# insert
print 'insert function'
numbers = [1, 2, 3, 5, 6, 7]
print 'numbers is', numbers
numbers.insert (3, 'four')
print 'numbers.insert (3, \'four\'), numbers is', numbers
print ''

# pop
print 'pop function'
x = [1, 2, 3]
print 'x is', x
x.pop()
print 'x.pop(), x is', x
print ''

# remove
print 'remove function'
x = ['to', 'be', 'or', 'not', 'to', 'be']
print 'x is', x
x.remove('be')
print 'x.remove(\'be\'), x is', x
print ''

# reverse
print 'reverse function'
x = [1, 2, 3]
print 'x is', x
x.reverse()
print 'x.reverse(), x is', x
print ''

# sort
print 'sort function'
x = [4, 6, 2, 1, 7, 9]
print 'x is', x
x.sort()
print 'x.sort(), x is', x
print ''

# advanced sort
print 'advanced sort'
num = [5, 2, 9, 7]
print 'num is', num
num.sort(cmp)
print 'num.sort(cmp), num is', num
print ''

# sort可选参数 key and reverse
print 'sort可选参数 key and reverse'
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
print 'x is', x
x.sort(key = len)
print 'x.sort(key = len), x is', x
x.sort(key = len, reverse = True)
print 'x.sort(key = len, reverse = True), x is', x
print ''

def compare(a, b):
	return (-1 if a < b else (0 if a == b else 1))
x = [4, 2, 0, 9, -10]
x.sort(cmp = compare)
print x

