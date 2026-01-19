import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="webuser",
    password="AaZz@@1234",
    database="webapp"
)

@app.route('/')
def index():
    mountains = ['Everest', 'K2', 'Kilimanjaro']
    return render_template('index.html', mountain=mountains)

@app.route('/mountain/<mt>')
def mountain(mt):
    return "This is " + str(mt)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
