import smtplib
from email.mime.text import MIMEText

server = 'localhost'
user_name = 'someone@email.com'
distribution_list = ['first@email.com', 'second@email.com']

msg = MIMEText('Test message send by by Python!')
msg['Subject'] = 'Python Test Email'
msg['From'] = user_name
msg['To'] = '; '.join(distribution_list)


server = smtplib.SMTP(server)
server.sendmail(user_name, distribution_list, msg.as_string())

server.quit()
