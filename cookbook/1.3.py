#!/usr/bin/python
'''
保留最后N个元素
保留有限历史记录正是 collections.deque 大显身手的时候。
'''
from collections import deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)



q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
print(q.pop())
print(q)
print(q.popleft())

