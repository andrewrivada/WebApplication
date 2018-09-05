# -*- coding: utf-8 -*-

"""
Created on Fri Aug 31 13:32:45 2018

@author: Andrew
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'