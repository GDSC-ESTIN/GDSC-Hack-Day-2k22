#!/usr/bin/python3
from flask import Flask, Response, request, render_template, make_response
from flask_autoindex import AutoIndex


app = Flask(__name__)
ppath = "./templates"

@app.route("/",methods = ["GET"])
def main():
    return render_template('index.html')



AutoIndex(app, browse_root=ppath)    

