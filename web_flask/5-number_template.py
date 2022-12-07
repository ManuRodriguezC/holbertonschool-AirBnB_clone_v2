#!/usr/bin/python3
"""
This module start the conection with flask,
for conect the web con database
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def slash():
    """This method return the messege of the page /"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """This method return other page"""
    return "HBNB"


@app.route('/c/<text>')
def c(text=None):
    """This method return the text if exist the param"""
    if text is not None:
        text = text.replace("_", " ")
        return "C {}".format(text)


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python(text=None):
    """
    This method return ne new text if text exist,
    else return Python is cool
    """
    if text is not None:
        text = text.replace('_', ' ')
        return "Python {}".format(text)
    return "Python is cool"


@app.route('/number/<int:n>')
def number(n):
    """This mtehod return if the param is int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def template_number(n):
    """Uses of the templates for pages"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
