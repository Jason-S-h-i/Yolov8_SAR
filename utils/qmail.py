import smtplib
from email.mime.text import MIMEText
from email.header import Header


def SendEmail(subject='test', body='test'):
    # 邮件内容
    # subject = 'model train complete!!!'
    # body = '你的模型训练完了，快去看看吧！！！\n时间不等人，抓紧吧！！！\nJason_SHI from qqmail'

    # 构建邮件
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '1441098779@qq.com'
    msg['To'] = 'ssj1441098779@163.com'

    # 发送邮件
    smtp_server = 'smtp.qq.com'
    smtp_port = 587
    sender_email = '1441098779@qq.com'
    password = 'tphharcxkfjuibdj'  # 在QQ邮箱设置里拿到的码

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, [msg['To']], msg.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败:', str(e))


