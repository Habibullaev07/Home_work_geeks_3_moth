import os
import aiosmtplib    
from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_SENDER = os.getenv("SMTP_SENDER")
SMTP_PASS = os.getenv("SMTP_PASS")

async def send_email(recipient, subject, message_body, send_file=None):
    msg = EmailMessage()
    msg["subject"] = subject
    msg["From"] = SMTP_SENDER
    msg["To"] = recipient
    msg.set_content(message_body, subtype="html")

    if send_file:
        file_name = send_file.split("/")[-1]
        file_extension = file_name.split('.')[-1]
            
        if file_extension == "jpg":
            maintype = "image"
            subtype = "jpeg"
        elif file_extension == "mp4":
            maintype = "video"
            subtype = "mp4"
        elif file_extension == "mp3":
            maintype = "audio"
            subtype = "mp3"
      
        if maintype == "image":
            new_filename = "photo.jpg" 
        elif maintype == "video":
            new_filename = "video.mp4"
        elif maintype == "audio":
            new_filename = "audio.mp3"
            
        with open(send_file, 'rb') as file:
            msg.add_attachment(
                file.read(),
                maintype=maintype,
                subtype=subtype,
                filename=new_filename)
            
    await aiosmtplib.send(
        msg,
        hostname=SMTP_SERVER,
        port=SMTP_PORT,
        username=SMTP_SENDER,
        password=SMTP_PASS,
        start_tls=True)