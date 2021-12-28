from flask import Flask, render_template, url_for, redirect, request
import json
from flask import session
from google.cloud import storage
from controller import read_from_storage
from controller import read_from_firestore
import os

app = Flask(__name__) # initialize
#使用者密鑰
app.secret_key=b'ad65fa4f'


@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/map')
def map1():
    data = read_from_firestore.read_file()
    return render_template('map.html',data=data) 

@app.route('/map2')
def map2():
    data = read_from_firestore.read_file()
    return render_template('map2.html',data=data)  

@app.route('/map3')
def map3():
    data = read_from_firestore.read_file()
    # data = [1,'tiger']
    return render_template('map3.html',data=json.dumps(data)) 

@app.route('/map4')
def map4():
    data = read_from_firestore.read_file()
    return render_template('map4.html',data=json.dumps(data)) 

@app.route('/map5')
def map5():
    data = read_from_firestore.read_file()
    return render_template('map5.html',data=json.dumps(data)) 

@app.route('/form')
def form():
    data = read_from_firestore.read_file()
    return render_template('form.html', data=data)

# 實際run
# if __name__=="__main__":
#     app.run(debug=True)

# 僅供gcp上8080port預覽
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))