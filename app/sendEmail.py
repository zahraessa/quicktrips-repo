import smtplib

gmail_user = 'quicktripssystems@gmail.com'
gmail_password = 'quicktrips101'

def contactUsConfirmation(name, email, query):
    sent_from = gmail_user
    to = [email]
    subject = 'QuickTrips Contact Us - Copy of your query'
    body = "Hi" + name + "\n Here is a copy of your query. We will be in touch with you soon!. \n" + query

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

def RegistrationConfirmation(name, username, email):
    sent_from = gmail_user
    to = [email]
    subject = 'QuickTrips - Confirmation of registration'
    body = "Hi" + name + "\n Thank you for registering to our application! \n + Your username is " + \
           username + ". \n The QuickTrips Team!"

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


def ForgotPasswordEmail(name, email, code):
    sent_from = gmail_user
    to = [email]
    subject = 'QuickTrips - Confirmation of registration'
    body = "Hi" + name + "\n Here is your rest token: \n " + code + ". \n The QuickTrips Team!"

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
