from flask import Flask
from flask import request
from flask import render_template

import smtplib

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/send_email', methods=['POST'])
def send_email():
    # login info
    username = 'buskerlic'
    password = 'rhrhtld1@g'
    toaddrs = 'muzuco@netmarble.com'
    fromaddrs = 'buskerlic@gmail.com'
    title = request.form['Title']
    contents = request.form['Contents']
    message = 'Subject: %s\n\n%s' % (title, contents)
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddrs, toaddrs, message)
        server.quit()
        return 'OK: Check the mail.'
    except smtplib.SMTPException:
        return 'Error: unable to send email.'

if __name__ == '__main__':
    app.run()
