import imaplib
import email
import re


def getEmailOtp():
    username = 'randomstagtest@gmail.com'
    password = 'qyyz flrx axfk ffqc'
    # username = 'testing4603@gmail.com'
    # password = 'vtbbqwcfpaoplusn'

    mymail = imaplib.IMAP4_SSL('imap.gmail.com')
    mymail.login(username, password)
    mymail.select('INBOX')
    key = 'FROM'
    value = 'noreply_lahebo@lahebo.com'

    _, search_data = mymail.search(None, key, value)
    for num in search_data[0].split():
        # print(num)
        # print(len(search_data[0].split()))
        # print(search_data[0].split())
        mail = search_data[0].split()
        last_element = mail[-1]
        # print(last_element)

        _, data = mymail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        # print(email_message)
        for part in email_message.walk():

            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                fun = body.decode()
                # print(body.decode())
                pattern = r"\b\d{6}\b"
                otp_code = re.findall(pattern, fun)

                return otp_code
