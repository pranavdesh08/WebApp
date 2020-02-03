# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template,request,json,send_file, Response
import pandas as pd
from luck import unique_val,dataAnalysis
from werkzeug import secure_filename
import os
import csv



app= Flask(__name__)



templ1 = unique_val()
templ2= unique_val()


#j = {}
@app.route('/')
def index():
    
    return render_template('home.html', templ1=templ1, result= {})
#,templ2=templ2
@app.route('/processed-template', methods=['POST'])
def process_template():
    a = request.form.getlist('a')  
    j = dataAnalysis(a)
    
    return j

    
@app.route('/upload')
def upload_file():
   return render_template('home.html')


@app.route('/download')
def download_file():
    path = "C:/Users/12014/.spyder-py3/MyFlaskApp/templates/file1.csv"
    return send_file(path, mimetype='text/csv', attachment_filename='file1.csv', as_attachment=True)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_return():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
    
if __name__=="__main__":
    app.run()
    