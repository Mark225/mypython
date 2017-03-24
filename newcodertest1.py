#coding = utf-8
import sys 

def multi(part):
    multiNum = 1
    for i in range(len(part)):
        multiNum = multiNum * int(part[i])  
    return multiNum


def judge(num):
    for i in range(len(num)):       
        if multi(num[:i])==multi(num[i:]):
           print('yes')
           return
    print('no')

while True:
    line = input()
    if not line:
        break
    judge(str(line))

