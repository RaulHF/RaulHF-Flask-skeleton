from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "guys I hope that your morning has been as productive as Raul\'s"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()
