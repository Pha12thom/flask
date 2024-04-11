from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'



@app.route('/')

def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)