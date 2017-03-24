import urllib.request
import socket
import re
import sys
import os
targetDir = r"D:\picb"
def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos+1:])
    return t

if __name__ == "__main__":
    hostname = "http://wenku.baidu.com/link?url=yh6qY4EC7p4MUu1vw3RUPIzp5Yz0gvxdkaMkDr0MCjHwfcn5Sn2Gwfc7R6LlWNVbynE92ZdALiyT16Q9Y5gXkGLWYF8UHeaKTEX6SBiqvvW"
    req = urllib.request.Request(hostname)
    webpage = urllib.request.urlopen(req)
    contentBytes = webpage.read()
    for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(contentBytes))):
        print(link)
        urllib.request.urlretrieve(link, destFile(link))
        print(t)
