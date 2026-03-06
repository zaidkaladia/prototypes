from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "hey Zaid"



@app.route("/query-params")
def qp():
    qp = request.args.get("name")
    return f"my name is {qp}"


@app.route("/dynamic/<name>")
def dynamic(name):
    return f"my name is {name}"


app.run(debug = True)