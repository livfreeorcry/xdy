import os
import re
from dice import Roll, parseString
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def roller():
	rollString=request.values.get('text') if request.values.has_key('text') else request.values.get('roll',"1d6")
	rollString=re.sub(r'[!@#$\'\"]','',rollString)
	parsed = parseString(rollString)
	dice = Roll(sides=parsed['sides'], ammount=parsed['ammount'], bonus=parsed['bonus'])
	dropped = []
	if 'keep' in parsed:
		dropped.extend(dice.keep(parsed['keep']))
	if 'drop' in parsed:
		dropped.extend(dice.drop(parsed['drop']))
		
	if dropped and dice.bonus:
		attachmentString="%s + %d : Dropped: %s" % (
			str(dice),
			dice.bonus,
			str(dropped)
			)
	elif dropped:
		attachmentString="%s : Dropped: %s" % (
			str(dice),
			str(dropped)
			)
	elif dice.bonus:
		attachmentString="%s + %d" % (
			str(dice),
			dice.bonus,
			)
	else:
		attachmentString=str(dice)

	response = {
	"response_type" : "in_channel",
	"text": "Rolled %s and got: *%d*" % (rollString, int(dice)),
	"attachments":[
	    {
	    "text": attachmentString
	    }
		]
	}
	return jsonify(response)