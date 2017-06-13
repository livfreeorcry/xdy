import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def roller():
	rollString=request.args.get('roll')
	return rollString