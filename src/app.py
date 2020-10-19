
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello,Nishad! Welcom To gitHub Action"

if __name__ == "__main__":
        app.run()
