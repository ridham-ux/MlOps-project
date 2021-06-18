with open("/cnndata/output.txt","r") as f:
    w=f.read()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender_address="ridham.dogra141@gmail.com"
sender_pass="radu@2000r"
reciever_address="ridham.dogra141@gmail.com"
subject="Regarding The model's accuray"
content="Hello there, Your model has ben trained and it has given the accuracy "+str(w)+" percentage"
message=MIMEMultipart()
message['From']=sender_address
message['To']=reciever_address
message['Subject']=subject 
message.attach(MIMEText(content,'plain'))
session=smtplib.SMTP_SSL("smtp.gmail.com",465)

session.login(sender_address,sender_pass)
text=message.as_string()
session.sendmail(sender_address,reciever_address,text)
session.quit()
print("Successfully sent your mail")
