import os
from dice import Roll
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def roller():
	rollString=str(request.args.get('roll'))
	return Roll(rollString).roll()