import os
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailMan(object):
    """docstring for MainMan"""
    def __init__(self, server):
        self.server = server
        self.message = ""

    def sendMail(self, sender, to, subject, text, html):

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to[0]

        # Create the body of the message (a plain-text and an HTML version).
        text = "This is automatically generated email, please do not reply"
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        # Send the message via local SMTP server.
        s = smtplib.SMTP(self.server)
        s.sendmail(sender, to, msg.as_string())
        s.quit()

if __name__ == '__main__':
    FROM = "SON NGUYEN DANG/LGEVH VC IVI SOFTWARE DEVELOPMENT 1 <son.nguyen@lge.com>"
    TO = ["son.nguyen@lge.com"]
    SUBJECT = "Test email"
    TEXT = "This is a testing email"

    mailMan = MailMan("lgesmtp.lge.com")
    mailMan.sendMail(FROM, TO, SUBJECT, TEXT)
