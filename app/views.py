from flask import render_template
from flask import request
from app import app
from app import process_data


@app.route('/',methods=['GET'])
def index():
	return render_template("index.html",data = process_data.process(),market = process_data.process_market())


@app.route('/coins',methods=['GET'])
def coin_list():
	return render_template("coins.html",data = process_data.coins())