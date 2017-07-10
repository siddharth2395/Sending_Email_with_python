# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
import sys

fromaddr = str(raw_input('Email ID: '))
recipient = sys.argv[1].split(',') #give recipients as commandline arguments

print "total recipients:",len(recipient)

password = getpass.getpass()

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, password)

for toaddr in recipient:
	print "sending mail to :",toaddr
	# instance of MIMEMultipart
	msg = MIMEMultipart()

	# storing the senders email address
	msg['From'] = fromaddr

	# storing the receivers email address
	msg['To'] = toaddr

	# storing the subject
	msg['Subject'] = "Mail From script Test 4"

	# string to store the body of the mail
	body = "le me know what u recived, i hope its individual mail"

	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))

	# open the file to be sent
	filename = "resume.pdf" #specify the name of file with extension
	attachment = open(filename, "rb")

	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')

	# To change the payload into encoded form
	p.set_payload((attachment).read())

	# encode into base64
	encoders.encode_base64(p)

	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	# attach the instance 'p' to instance 'msg'
	msg.attach(p)

	# Converts the Multipart msg into a string
	text = msg.as_string()

	# sending the mail
	s.sendmail(fromaddr, toaddr, text)


# terminating the session
s.quit()
