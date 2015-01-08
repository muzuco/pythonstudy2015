from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/send_email', methods=['POST'])
def send_email():
    title = request.form['Title']
    contents = request.form['Contents']
    
    return title + contents

if __name__ == '__main__':
    app.run()
