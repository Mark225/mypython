#!E:/python

import re

phone = "2004-909-123# 这是一个电话号码"

num = re.sub(r'#.*$',"",phone)
print(num)

number = re.sub(r'\D',"",phone)
print("phone number",number)
