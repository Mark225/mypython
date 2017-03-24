#! python3
# -*- coding=utf-8 -*-
#@Author
from urllib import request
import re

def findArticle(url):

    request = urllib.request.Request(url)

    response = urllib.request.urlopen(request)

    data = response.read()

    data = data.decode('utf-8')

    matchObj1 = re.findall(r'<div class="final-question">\n(.*)\n</div>',data,re.M)

    matchobj2 = re.findall(r'<div class="design-answer-box">\n(.*)\n</div>',data,re.M)

    return d{matchobj1(0) : matchobj2(0)}


if __name__=='__main__':
    findArticle()
