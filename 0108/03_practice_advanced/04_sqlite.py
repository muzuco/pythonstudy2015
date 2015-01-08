from flask import Flask
from flask import request
from flask import render_template

import smtplib

from sqlalchemy import create_engine


app = Flask(__name__)
@app.route('/')
def index():
    engine = create_engine('sqlite:///C:\\sqlite\\test.db', echo=True)
    connection = engine.connect()
    r = connection.execute('select * from first')
    data=[]
    for row in r:
        data.append(row)
        
    return render_template('sqlite.html', data = data)   
    #for row in r1:
    #    print row

if __name__ == '__main__':
    app.run()
