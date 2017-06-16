import os
import re
from dice import Roll
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def roller():
	rollString=request.args.get('text') if request.args.has_key('text') else request.args.get('roll',"1d6")
	rollString=re.sub(r'[!@#$\'\"]','',rollString)
	dice = Roll.from_string(rollString)
	response = {
	"response_type" : "in_channel",
	"text": "Rolled %s and got: *%d*" % (rollString, int(dice)),
	"attachments":[
	    {
	    "text": "%s + %d" % (str(dice), dice.bonus) if dice.bonus else str(dice.results)
	    }
		]
	}
	return jsonify(response)