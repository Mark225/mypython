#!/usr/bin/python
'''
解压序列赋值给多个变量
任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。
唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
'''

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, (year, mon, day) = data
print(name)
print(price)
print(mon)

s = 'Hello'
a, b, c, d, e = s
print(a)
print(c)
print(e)

#占位
_, shares, price, _ = data
print(shares)
print(price)
