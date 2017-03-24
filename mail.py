#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.yeah.net"  #设置服务器
mail_user="mark_616@yeah.net"    #用户名
mail_pass="13715625409yu"   #口令 
receivers = ['809081457@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('看到你列的2017小清单，我都自愧不如，我都不知道我的2017要干什么，希望你的目标都能超额完成，希望你开心。最后，真的别抽烟，喝酒就好！', 'plain', 'utf-8')
message['From'] = Header("mark_616@yeah.net", 'utf-8').encode()
message['To'] =  Header("809081457@qq.com", 'utf-8').encode()

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8').encode()


try:
    smtpObj = smtplib.SMTP(mail_host, 25) 
    smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user,mail_pass)
    print("logined")
    smtpObj.sendmail(mail_user,receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
finally:
    smtpObj.quit()
    print("离开")
