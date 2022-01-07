from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask web app"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9000)
