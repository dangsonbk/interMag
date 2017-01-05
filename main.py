import os
import sys
import re

from engine import mailMan

MAIL_FROM = "I3L Mailman <son.nguyen@lge.com>"
MAIL_TO = ["son.nguyen@lge.com"]
MAIL_SUBJECT = "I3L Project weekly sum-up"

def main():
    TEXT = "This is a testing email"

    mailTemplate = open("./template/cerberus.html", "r").read()
    # print mailTemplate

    _mailMan = mailMan.MailMan("lgesmtp.lge.com")
    _mailMan.sendMail(MAIL_FROM, MAIL_TO, MAIL_SUBJECT, TEXT, mailTemplate)

if __name__ == '__main__':
    main()
