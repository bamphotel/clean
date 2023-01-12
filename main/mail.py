import smtplib
import imghdr
from email.message import EmailMessage
from django.contrib import messages

def mailall(request, subject, uname, msg, rec):
  Sender_Email = "itassignment321@gmail.com"
  Reciever_Email = rec
  Password = "rzjazgsxqyccggyb"
  newMessage = EmailMessage()
  newMessage['Subject'] = subject
  newMessage['From'] = Sender_Email
  newMessage['To'] = Reciever_Email
  newMessage.add_alternative(f"""\
   <html>
   <head>
   </head>
   <body style="padding:5%; text-align:center; background-color:DarkSlateGray; border-radius:30px;">
   <h2>Hi, {uname}</h2>
   {msg}
   <a style="padding:5px 10px; background-color:DodgerBlue; text-decoration:none; color:white; border-radius:10px; font-size:17px;" href="https://erkata.herokuapp.com">visit web</a>
   <br>\n\n\n
   <br>\n\n\n
   <footer>copyright© ERKATA Cleaning<footer>
    </body>
    </html>""", subtype = 'html')

  #newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)
    smtp.send_message(newMessage)
  print("--------email sent...---------")
  return
