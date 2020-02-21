import smtplib
from email.message import EmailMessage


def email_body(data):
    email = EmailMessage()
    email['from'] = 'Rahul Kalwar'
    email['to'] = data
    email['subject'] = 'Resume'
    email.set_content(
        "Hello,\n\n"
        "Please find my resume in attached document.\n\n"
        "Regards,\n"
        "Rahul Kalwar")
    with open('resume.pdf', 'rb') as content_file:
        content = content_file.read()
        email.add_attachment(content, maintype='application/pdf', subtype='pdf', filename='resume.pdf')
    return email


def email_sent(email_object_to_sent):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("emailwithpython8@gmail.com", 'ckyolvyreghabjoa')
        smtp.send_message(email_object_to_sent)


if __name__ == "__main__":
    data = "kalwar.rahul@gmail.com"
    email = email_body(data)
    email_sent(email)