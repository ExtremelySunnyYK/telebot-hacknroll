from flask import Flask, render_template, request, url_for,jsonify
from werkzeug.utils import secure_filename
import requests
import os
import io

import logging
from decouple import config

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)


from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Updater, CommandHandler, Filters, CallbackContext

# Enable logging
from telegram.utils import helpers

app = Flask(__name__)

TELEGRAM_URL = "https://api.telegram.org/bot1582533456:AAFswg2spaHuwD0x6O3pG3ajSx4wjBuQL4s/"

@app.route('/shake',methods = ["GET","POST"])
def get_shake():
    ''' Receives POST Request from App and calls the shake leg function on telegram.    '''
    user_name = request.data
    requests.post(user_name,TELEGRAM_URL)

if __name__ == '__main__':
   app.run()
