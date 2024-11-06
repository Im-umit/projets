import smtplib
from email.mime.text import MIMEText

port =587
smtp_server ="smtp-relay.brevo.com"
login="7af4c7001@smtp-brevo.com"
password="g9d1wIPY6rh5stTF"

sender_email ="info@mahkememerkezi6.com"
receiver_email ="koyuncuumit34@gmail.com"

text="Merhaba hakkınızda tazminat davası açılmıştır bilginize hüseyin sarısaç"

message = MIMEText(text, "plain")
message["subject"] ="Merhaba"
message["from"] = sender_email
message["to"] = receiver_email

with smtplib.SMTP(smtp_server, port) as server:
	server.starttls()
	server.login(login,password)
	server.sendmail(sender_email, receiver_email, message.as_string())
	
print("Mesajınız gönderildi")