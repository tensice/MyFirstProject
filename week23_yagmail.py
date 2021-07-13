import yagmail
to = "visvesh.raghuraman@gmail.com"
cc = "tensice@mailinator.com","yoru@mailinator.com"
bcc = "tensice123@mailinator.com"
subject = "Mail from yagamil"
body = '''<h1> Hello World</h1>
<img src="/Users/ragu/Downloads/chess.jpeg">'''
attachments = ["/Users/ragu/Downloads/chess.jpeg"]
gmail_user = "visvesh.raghuraman@gmail.com"
gmail_password = "pbfjuauezclidfpm"
yag = yagmail.SMTP(gmail_user,gmail_password)
yag.send(to=to,cc=cc,bcc=bcc,subject=subject,contents=body,attachments=attachments)
print("Mail sent from super easy yagmail")







