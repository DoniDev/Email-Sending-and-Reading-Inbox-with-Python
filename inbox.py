import imaplib
import email
import os


host = 'imap.gmail.com'

username = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASSWORD')


def get_inbox():

    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select('inbox') #drafts, sent, started

    _, search_data = mail.search(None,'SEEN') #SEEN or  UNSEEN

    my_messages = []

    print(search_data)

    for num in search_data[0].split():

        email_data = {}
        _ ,data = mail.fetch(num, '(RFC822)')
        # print(data)
        _, b = data[0]
        # print(b)
        email_message = email.message_from_bytes(b)
        # print(email_message)
        for header in ['subject','to','from','date']:
            print(f'{header}: {email_message[header]}')
            email_data[header]  = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                # print(body.decode())
                email_data['body'] = body.decode()
            elif part.get_content_type() == 'text/html':
                html_body = part.get_payload(decode=True)
                # print(html_body.decode())
                email_data['html_body'] = html_body.decode()
            my_messages.append(email_data)
    return my_messages

get_inbox()





