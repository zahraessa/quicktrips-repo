import smtplib

gmail_user = 'quicktripssystems@gmail.com'
gmail_password = 'quicktrips101'


sent_from = gmail_user
to = ['zahraessa99@gmail.com']
subject = 'QUICKTRIPS VERIFICATION'
body = "Verify here"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
