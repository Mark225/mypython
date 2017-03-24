import urllib

requset = urllib.request('http://www.xxxxx.com')
try:
    urllib.urlopen(request)
except urllib.URLError as e:
    print(e.reason)
