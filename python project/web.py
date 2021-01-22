# -*- coding = utf-8 -*-
from flask import Flask,jsonify,render_template,request
from password import password
from gaode import geocode,weatherinfo

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def login() ->"html":
	return render_template("Login.html")



@app.route("/search",methods = ["POST"])
def hello_login():
	zhanghao = request.form["zhanghao"]
	mima = request.form["mima"]
	a = password(zhanghao,mima)
	if a == "true":
		return render_template("map.html")
	else:
		return render_template("loginfail.html",loginfail = "登录失败")






if __name__ == '__main__':
	app.run(debug=True)