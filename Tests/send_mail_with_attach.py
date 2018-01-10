#!/usr/bin/env python

# -*- coding: utf-8 -*-
import os
import smtplib

from email import MIMEMultipart
from email import MIMEText
from email import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import datetime

fromaddr = "togoodtobytrue@gmail.com"
toaddr = ["vadim.shurhal@triogeeks.com"]#, "andrey.rud@triogeeks.com", "burund@triogeeks.com", "maksym.gak@triogeeks.com"]
mypass = "dflbv123"
dt = datetime.datetime.now()
dt =dt.strftime("%d-%m-%Y %H:%M")
msg = MIMEMultipart('alternative')

#msg['From'] = fromaddr
#msg['To'] = toaddr
msg['Subject'] = "Results of testing on %s" %dt

body = "For normal display of this report is compatible with the file style.css, which should be in the asset folder. Structure: Report + folder with file style.css"

#new_report = 'Hello \n \n' + \
#             "To view the report 'Create_ored_all_site', click on the link http://173.224.121.74/test_all_site_report.html \n \n" + \
#             "To view the report 'Check_pid', click on the link http://173.224.121.74/check_pid_report.html \n" \
#             "\n \n \n Best regards " \
#             "\n ShoPoShapkam.Team"


msg.attach(MIMEText(body, 'plain'))


############### Attach report.html

dir = os.getcwd()
files = os.listdir(dir)
pathreport = os.path.join(dir, 'report.html')
reportname = "report.html"

attachment = open(reportname, "rb")
part1 = MIMEBase('application', 'octet-stream')
part1.set_payload((attachment).read())
encoders.encode_base64(part1)
part1.add_header('Content-Disposition', "attachment; filename= %s" % reportname)
msg.attach(part1)

############ Attach ccs.ctyle

dir = os.getcwd()
pathcss = os.path.join(dir, 'assets/style.css')
cssname = "style.css"
attachment2 = open("assets/%s" % cssname, "rb")
part2 = MIMEBase('application', 'octet-stream')
part2.set_payload((attachment2).read())
encoders.encode_base64(part2)
part2.add_header('Content-Disposition', "attachment; filename= %s" % cssname)
msg.attach(part2)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()