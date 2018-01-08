from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from string import Template
from random import randint
import json
import pymongo
import requests
import datetime
import time
import urlparse
import hashlib as hl
import os
import httpagentparser

app = Bottle(__name__)

@app.route('/')
def root():
	return static_file('index.html', root='templates')

@app.route('/blr2017')
def event():
	return static_file('blr2017.html', root='templates')

@app.route('/open-data-workshop')
def event():
	return static_file('open-data-workshop.html', root='templates')

@app.route('/.well-known/acme-challenge/<file_name>')
def ssl_cert(file_name):
	return static_file(file_name, root='templates')
		
# Static Routes
@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static')

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
