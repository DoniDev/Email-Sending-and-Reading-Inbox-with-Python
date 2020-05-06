import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# send_mail('subject', 'body of the message', 'sender@example.com', ['receiver1@example.com',])


# accessing my email and password with environment variables for security purposes
username = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASSWORD')
name = 'Doniyor'
sender = f'<{username}>'


def send_mail(text='Email Body',subject='FreecodeCamp',from_email=name + ' ' + sender,to_emails=None):
    assert isinstance(to_emails,list)


    # Create the MIMEMultipart message object and load it with appropriate headers for From, To, and Subject fields.
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject


    # txt_part = MIMEText(text, 'plain')
    # msg.attach(txt_part)


    html_part = MIMEText('<h1>Welcome to send email with Python</h1>', 'html')
    msg.attach(html_part)




    # Returns the entire formatted message as a string
    msg_str = msg.as_string()




    # setting up a server and logging in to our account
    # server will run and it should quit after email is sent
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)

    # these two are default configurations of smtplib for security purposes
    server.ehlo()
    server.starttls()

    # logging to our account with server
    server.login(username,password)

    server.sendmail(from_email,to_emails,msg_str)

    server.quit()


send_mail(to_emails=['dabduvokhidov@gmail.com','abduvokhidovdoniyor5@gmail.com'])
