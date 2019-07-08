import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import yaml
def sendEmail(sender,receiver,content,filePath):
  config = {}
  base_path = os.path.dirname(os.path.abspath(__file__))
  with open(base_path + "/config.yaml") as f:
    config = yaml.load(f, Loader=yaml.BaseLoader)
  sender_email = sender
  receiver_email = receiver
  password = 'exevqmxmkrcthcbg'
  content = content
  textApart = MIMEText(content)
  pdfFile = filePath
  fileName = '153'
  pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
  pdfApart.add_header('Content-Disposition', 'attachment', filename=fileName)
  m = MIMEMultipart()
  m.attach(textApart)
  m.attach(pdfApart)
  m['Subject'] = 'comicPdf'
  context = ssl.create_default_context()
  server = smtplib.SMTP_SSL('smtp.qq.com')
  server.login(sender_email, password)
  server.sendmail(
    sender,
    receiver,
    m.as_string())
  server.quit()