import os
from dice import Roll
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def roller():
	rollString=request.args.get('roll')
	if rollString[0]=="'" or rollString[0]=='"':
		rollString=rollString[2:-1]
	return str(Roll(rollString).roll())