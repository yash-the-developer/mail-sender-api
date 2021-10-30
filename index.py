from flask import Flask
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def main():
    return 'Api is working'


@app.route('/<string:sender_email>/<string:sender_password>/<string:recievers_email>/<string:subject>/<string:body>')
def answeranyquestion(sender_email,sender_password,recievers_email,subject,body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recievers_email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email,sender_password)
        server.send_message(msg)
        server.quit()
        return("Message sent successfully")
        
        
    except Exception as e:
        return(e)


if __name__ == '__main__':
  app.run()