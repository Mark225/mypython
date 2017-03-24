#! python3
# -*- coding=utf-8 -*-
#@Author
import urllib.request
import re

def findArticle(url):

    request = urllib.request.Request(url)

    response = urllib.request.urlopen(request)

    data = response.read()

    data = data.decode('utf-8')

    matchobj1 = re.findall(r'<div class="final-question">\n(.*)\n</div>',data,re.M)

    matchobj2 = re.findall(r'<div class="design-answer-box">\n(.*)\n</div>',data,re.M)

    message = matchobj1[0] + '\n' + re.sub(r'<br/>', "\n", matchobj2[0])

    #print(message)
    
    return message
#-------------------------------------------------
def writeFile(path,message):
    
    with open(path, 'a') as f:
         f.write(message + '\n'+ '\n')
                 
    print("!!!!!!!!One recoder has been wroten!!!!!!!!")
#-------------------------------------------------
absent = []    
for i in range(1,12):
    try:
        url = 'https://www.nowcoder.com/ta/review-network/review?tpId=33&tqId=21189&query=&asc=true&order=&page=%d' % i
        f = findArticle(url)
        w = writeFile('E:/net_Newcoder1.txt','%d:' % i + f)
    except Exception as e:
        absent.append(i)
        print("!!!!!!!!Error in page:%d!!!!!!!!!!!!" % i)
        print('Error:',e)

print(absent)


