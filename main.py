import pandas as pd
import os
# from mysql.connector import mysql
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import mysql.connector
from flask_bcrypt import Bcrypt
from datetime import datetime
import time
from flask_cors import CORS, cross_origin
import jwt
import smtplib, socket
from werkzeug.utils import secure_filename
import config
import uuid
from flask import render_template


UPLOAD_FOLDER = './assets/uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
bcrypt = Bcrypt(app)
secret = 'muqtadirbillah'
CORS(app, supports_credentials=True)

# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

# @cross_origin()
# @cross_origin(headers=['Access-Control-Allow-Origin', 'http://localhost:3000'])
@cross_origin(headers=['Access-Control-Allow-Origin', '*'])
# @crossdomain(origin='*', headers=['access-control-allow-origin', 'Content-Type'])
@cross_origin(supports_credentials=True)


@app.route('/')
def index():
  return render_template('index.html', title="Home", content="Hello, World!")

@app.route('/audio/upload', methods=['POST'])
def uploadAudio():
    # print(request.form['projectFilePath'])
    date = str(datetime.date(datetime.now()));
    if 'file' not in request.files:
        print('No file part')
        return ('Something went wrong!')
    #file = request.files['file']
    # app.logger.info(request.files)
    upload_files = request.files.getlist('file')
    # app.logger.info(upload_files)
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if not upload_files:
        print('No selected file')
    print(len(upload_files))
    try:
        for file in upload_files:
            print('uploading')
            print(uuid.uuid4())
            myuuid = uuid.uuid4()
            original_filename = str(myuuid)+file.filename
            extension = original_filename.rsplit('.', 1)[1].lower()
            # filename = str(original_filename+'.'+extension)
            filename = str(original_filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_list = os.path.join(UPLOAD_FOLDER, 'files.json')
            print(filename)
        return("Uploading")
    except error as err:
        return(err)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)