import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# MIME - Multi-purpose internet mail extentions

gmail_user = "visvesh.raghuraman@gmail.com"
gmail_password = "pbfjuauezclidfpm"


def send_message_tls(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user,gmail_password)
    server.send_message(msg)
    server.quit()
    print("Sent multi-part message")

name = "Bob"
message = MIMEMultipart("mixed")
message['From'] = "visvesh.raghuraman@gmail.com"
message['To'] = "visvesh.raghuraman@gmail.com,tensice@mailinator.com"
message['Cc'] = "clash@mailinator.com"
message['Bcc'] = "yoru@mailinator.com"
message['Subject'] = "My First Multi-Part Message"

body = f'''<h2>Hello {name}</h2>
<p>How are doing today?
I need you to check a <b> <font color = 'red'> submission</font> </b> by the end of today.
Please do that ASAP.</p>
<a href = "https://lichess.org/"> Chess Website </a>
'''

body_html = MIMEText(body,'html')
message.attach(body_html)
img_file = "/Users/ragu/Downloads/chess.jpeg"

with open(img_file,'rb') as attachment:
    af = MIMEApplication(attachment.read(),_subtype='jpg')
    af.add_header('Content-Disposition',f'attachment; filename= {img_file}')
    message.attach(af)
send_message_tls(message)











