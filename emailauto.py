import os
from dotenv import load_dotenv
import smtplib
from socket import timeout
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

load_dotenv()
listener = sr.Recognizer()
engine = pyttsx3.init()
email_user =os.getenv('EMAIL_USER')
email_pwd=os.getenv('EMAIL_PWD')

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info(ptl=5):
    
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,timeout=None,phrase_time_limit=ptl)       
            info = listener.recognize_google(voice)
            print("Receiver : ", info)              
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_pwd)
    email = EmailMessage()
    email['From'] = email_user
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'raj': 'rajprabhakar3107@gmail.com',
    'harshan': 'harshukutty14@gmail.com',
    'hari': 'tsudhanhari06@gmail.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info(5)
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info(10)
    talk('Tell me the text in your email')
    message = get_info(30)
    send_email(receiver, subject, message)
    talk(' Your email is sent successfully')
    talk('Do you want to send more email?')
    send_more = get_info(5)
    if 'yes' in send_more:
        get_email_info()


get_email_info()