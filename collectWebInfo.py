import urllib.request
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url = "http://www.weather.com.cn/weather/101281701.shtml"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

data = response.read()

data = data.decode('utf-8')

#print(data)
#<input type="hidden" id="hidden_title" value="">
#r'^input type="hidden" id="hidden_title" value="(.)"$'

matchObj = re.search( r'id="hidden_title" value="(.*)"', data)

if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group(1))
   message = "哈哈！我的阿俊，中山天气是：" + matchObj.group(1) + "。"
else:
   print ("No match!!")

#--------邮件发送--------
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = "mark_616@yeah.net"
password = "13715625409yu"
to_addr = '290975428@qq.com'
smtp_server = "smtp.yeah.net"

msg = MIMEText(message, 'plain', 'utf-8')
msg['From'] = _format_addr('超帅的Mark <%s>' % from_addr)
msg['To'] = _format_addr('You <%s>' % to_addr)
msg['Subject'] = Header('今日天气', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
print("发送成功！")
server.quit()
