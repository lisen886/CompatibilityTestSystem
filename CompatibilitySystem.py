# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/CompatibilitySystem",methods = ['POST'])
def CompatibilitySystem():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username=="lisen" and password=="123456" or username=="admin" and password=="":
            return render_template("playVideo.html")
        else:
            return render_template("loginfail.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8091,debug=True)