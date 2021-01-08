from flask import Flask, render_template, request, url_for,jsonify
from werkzeug.utils import secure_filename
import requests
import os
import io

app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def get_shake():
    ''' Receives POST Request from App and calls the shake leg function on telegram.    '''
    pass

if __name__ == '__main__':
   app.run()
