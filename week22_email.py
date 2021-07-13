import smtplib

def send_mail_ssl(sf,st,et):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user,gmail_password)
    server.sendmail(sf,st,et)
    server.quit()
    print("Sent email via SSL")

def send_mail_tls(sf,st,et):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user,gmail_password)
    server.sendmail(sf,st,et)
    server.quit()
    print("Sent email via TLS")


gmail_user = "visvesh.raghuraman@gmail.com"
gmail_password = "pbfjuauezclidfpm"
sent_from = gmail_user
sent_to = ["tensice@mailinator.com",gmail_user]
subject = "First python email"
body = "Hello, how are you? tls\n tensice"
email_text = f"""From:{sent_from}' 
To:{sent_to}'
Subject:{subject}
{body}"""
#send_mail_tls(sent_from,sent_to,email_text)



#Who you want to send email
#Subject,content
#Send via SSL or TLS(more secure)
#SSL = secured sockets layer
#TLS = transport layer security
sending_to = []
while True:
    to = input("Type who you want to send the email to. Type -1 to if you are finished with the list of people you are sending to.\n")
    if "-" not in to:
        sending_to.append(to)

    if to == "-1":
        break

new_subject = input("""Type the subject\n""")
new_body_final = ""
while True:
    new_body = input("Type the body. Press enter for a new line. Type *** to exit.\n")
    if "***" not in new_body:
        new_body_final += new_body + "\n"
    if new_body == "***":
        break
tls_or_ssl = input("Type SSL or TLS\n")

new_email_text = f"""From:{gmail_user}
To:{to}
Subject:{new_subject}
{new_body_final}"""

if tls_or_ssl == "SSL":
    send_mail_ssl(gmail_user,sending_to,new_email_text)
if tls_or_ssl == "TLS":
    send_mail_tls(gmail_user,sending_to,new_email_text)
