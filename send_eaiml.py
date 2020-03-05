import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 需要登陆Q邮箱
from_addr = '821807519@qq.com'
password = 'yxevjxotglgtbbie'
stmp_server ='smtp.qq.com'
# 并定义邮件信息
msgRoot = MIMEMultipart(' related')  # 实例化邮件对象
msgRoot['from'] = '821807519@qq.com'
msgRoot['Subject'] = '自动化测试'
msgRoot['To'] = ",".join(["77473328@qq.com"]) #添加邮件发送人
msgText = MIMEText(" web自动化测试报告") # 定义邮件标题
msgRoot.attach(msgText) #添加邮件标题

# 添加附件
att = MIMEText(open("./report/test_report_20200221121252.html",'rb').read(),'base64','utf-8' )
att["Content-Type"] = 'application/ octet-stream'
att["Content-Disposition"] = "attachment;filename=test.html"
msgRoot.attach(att)
server = smtplib.SMTP(stmp_server,25)

# 登陆邮件服务器
server.login(from_addr, password)
# 发送邮件
server. sendmail (from_addr, ["77473328@qq.com"],msgRoot.as_string())


