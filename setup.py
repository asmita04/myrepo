import os 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    retuen "welcome"

@app.route('/how are yoy')
def hello():
    retuen 'i am good,how about you'    

if __name__ == "__main__":
    app.run()
