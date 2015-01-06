from flask import Flask
from flask import request, redirect

app = Flask(__name__)
@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == '__main__':
    app.run(port=3000)