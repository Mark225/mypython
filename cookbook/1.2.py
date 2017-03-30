#!/usr/bin/python
'''
解压可迭代对象赋值给多个变量
扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的。
'''
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(phone_numbers)
#值得注意的是上面解压出的 phone_numbers 变量永远都是列表类型，
#不管解压的电话号码数量是多少(包括0个).

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing) #前七个数字

#星号表达式在迭代元素为可变长元组的序列时是很有用的。
#比如，下面是一个带有标签的元组序列：
records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
    ]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


#星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')


#解压一些元素后丢弃它们，你不能简单就使用 * ，
#但是你可以使用一个普通的废弃名称，比如 _ 或者 ign 。
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)


