#!/usr/bin/python2

from mongoengine import connect, DoesNotExist
from flask import Flask, abort, redirect, url_for
from Entry import Entry

app = Flask(__name__)

@app.route("/")
def hello():
    return "main"

@app.route("/<url>/report")
def report(url):
    return "report"

@app.route("/<url>/<key>")
def admin(url, key):
    return "admin"

@app.route("/<url>")
def run(url):
    try:
        a = Entry.objects.get(short_url=url)
        raise Exception(a.long_url)
    except DoesNotExist:
        return redirect(url_for('hello')) 

if __name__ == "__main__":
    connect('imortal')
    app.run("0.0.0.0", debug=True)
