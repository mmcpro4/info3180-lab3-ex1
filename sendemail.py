import smtplib


def sendemail(fromaddr,fromname,subject,msg):
    toaddr = 'username4@gmail.com'
    message = """From: {} <{}>
    To: {} Keniel
    Subject: {}
    {}
    """

    messagetosend = message.format(
                                 fromaddr,
                                 fromname,
                                 toaddr,
                                 subject,
                                 msg)

    # Credentials (if needed)
    username = 'username@hgmail.com'
    password = 'password123'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, messagetosend)
    server.quit()