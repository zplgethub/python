#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-18 15:40:15
# @Author  : zpl (zh_octopus@qq.com)
# @Link    : 
# @Version : 2.7.11

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#绑定主页访问
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "111":
        return render_template('signin_ok.html', username=username)
    return render_template('signin_error.html',username=username)

if __name__ == "__main__":
    app.run()
