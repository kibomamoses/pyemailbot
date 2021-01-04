import smtplib
import speech_recognition as kiboma
import pyttsx3
from email.message import EmailMessage

listener = kiboma.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listening():
    try:
        with kiboma.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return listening().lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'kiboma': 'COOL_KIBOMA_EMAIL',
    'moses': 'moses@gmail.com',
    'jane': 'jane@gmail.com',
    'john': 'john@gmail.com',
    'hellen': 'hellen@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = listening()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = listening()
    talk('Tell me the message in your email')
    message = listening()
    send_email(receiver, subject, message)
    talk('Hey kiboma. Your email is sent')
    talk('Do you want to send another email email?')
    send_more = listening()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
