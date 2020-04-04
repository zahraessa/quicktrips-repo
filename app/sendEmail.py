import smtplib, ssl

from email.mime.text import MIMEText

gmail_user = 'quicktripssystems@gmail.com'
gmail_password = 'quicktrips101'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)


def contactUsConfirmation(name, email, query):
    sender = gmail_user
    receiver = email

    msg = MIMEText("Hi " + name + ",\nHere is a copy of your query. We will be in touch with you soon! \n\n" + query +
                   "\n\nThe QuickTrips Team!")
    msg['From'] = gmail_user
    msg['To'] = email
    msg['Subject'] = 'QuickTrips Contact Us - Copy of your query'
    msg['Message']
    server.sendmail(sender, receiver, msg.as_string())


def RegistrationConfirmation(name, username, email, code):
    sender = gmail_user
    receiver = email

    msg = MIMEText("Hi " + name + ","
                                  "\nThank you for registering to our application! "
                                  "\n + Your username is """ + username +
                   "\nHere is your confirmation token: "
                   "\n" + code +
                   "\n\nThe QuickTrips Team!")
    msg['From'] = gmail_user
    msg['To'] = email
    msg['Subject'] = 'QuickTrips - Confirmation of registration'
    msg['Message']
    server.sendmail(sender, receiver, msg.as_string())



def ForgotPasswordEmail(name, email, code):
    sender = gmail_user
    receiver = email

    msg = MIMEText("Hi " + name + ","
                   "\nHere is your password reset token: "
                   "\n" + code +
                   "\n\nThe QuickTrips Team!")
    msg['From'] = gmail_user
    msg['To'] = email
    msg['Subject'] = 'QuickTrips - Confirmation of registration'
    msg['Message']
    server.sendmail(sender, receiver, msg.as_string())