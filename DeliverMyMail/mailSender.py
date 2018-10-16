#!/usr/bin/python
import smtplib
from smtplib import SMTPException

sender = 'testSender@testdomain.com'
receivers = ['testReceiver@testdomain.com']

message = """From: <Enter from address here>
To: testReceiver@testdomain.com
Subject: Mail from Python Bots 

You have been chosen by the bots !.
"""

try:
   smtpObj = smtplib.SMTP('Enter SMTP server within these quotes')
   smtpObj.sendmail(sender, receivers, message)
   print ("Your Mail has been delivered !")
   
except SMTPException:
   print ("Error: {0}".format(SMTPException))

except BaseException as e:
    print("Error: {0}".format(e))
