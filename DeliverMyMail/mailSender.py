#!/usr/bin/python3
import smtplib
import socket
import sys
from smtplib import SMTPException

sender = 'testSender@testdomain.com'
receivers = ['testReceiver@testdomain.com']

#structured mail
mailContent = """From: testSender@testdomain.com
To: testReceiver@testdomain.com
Subject: Hello from python code

You have been chosen by the python gods !

"""

# messages can be without any format like plainMessage below but these messages are usually caught by spam filters
plainMessage = """ 
This is a message without To , From and subject 
"""


try:
    # Set timeout to a minute to force stop the connection , change this if necessary
    socket.setdefaulttimeout(1 * 60)

    # # without SSL
    # smtpObj = smtplib.SMTP('enter smtp server ip')
    # smtpObj.sendmail(sender, receivers, plainMessage)
    # print ("Your Mail has been delivered !")

    #with SSL and auth
    """ For gmail , there is a security feature which might throw an error saying -
    mtplib.SMTPAuthenticationError: Please log in via your web browser and then try again. Learn more at https://support.google.com/mail/answer/78754 
    To resolve this , enable "Allow less secure apps" option in gmail. Check references section at the end of the code for further info.
    """
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("gmailId", "gmailPassword")
    server.sendmail(
        "From address",
        "To address",
        mailContent)
    server.quit()

except SMTPException:
    lineNo = sys.exc_info()[-1].tb_lineno
    print("Error: SMTP exception , Check line {0}".format(lineNo))

except BaseException as e:
    lineNo = sys.exc_info()[-1].tb_lineno
    print("Error: {0} at line {1}".format(e, lineNo))


# References -
# 1. https://www.afternerd.com/blog/how-to-send-an-email-using-python-and-smtplib/
# 2. https://docs.python.org/3/library/smtplib.html
