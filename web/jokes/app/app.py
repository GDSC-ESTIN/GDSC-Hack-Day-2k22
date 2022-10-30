#!/usr/bin/python3
from flask import Flask, Response, request, render_template, make_response

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def main():
    return render_template('index.html')

@app.route("/",methods = ["POST"])
def main2():
    return '<p>GDSC{YESS_p0ST_R3qu3stttt}</p>'

