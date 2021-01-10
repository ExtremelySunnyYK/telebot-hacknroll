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

TOKEN = config('KEY')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

BOT = {}

message_to_user = "Add this to groups that you want to notify about shaking legs"
humialiting_message = "I AM A PERSON WHO HAS NO SELF CONTROL"
user_groups = {}

# Define constants that will allow us to reuse the deep-linking parameters.
CHECK_THIS_OUT = 'check-this-out'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'

def start(update, context):
    """Sends humiliating message to chats"""
    global BOT
    
    BOT = context.bot
    chat_id = update.message.chat_id
    print("BOT: ", BOT)
    userId = update.message.from_user['username']
    if userId not in user_groups:
        print("Initiating new user")
        user_groups[userId] = []
    user_groups[userId].append(chat_id)
    print("USER GROUPS: ", user_groups)

    url = helpers.create_deep_linked_url(BOT.get_me().username, CHECK_THIS_OUT, group=True)

    
    if chat_id > 0: 
        update.message.reply_text(f'Howdy Good day {update.effective_chat.first_name}')
        text = f"Add this to people you care about \n {url}"
        update.message.reply_text(text)
    else:
        update.message.reply_text(f'Hello everyone, our friend has a problem and needs our help!')
        text = f"Your group id is: \n`{chat_id}`\n(You can tap this to copy to clipboard!)\nAdd this to Shake Master!"
        update.message.reply_markdown(text)


# Listener for "start" command
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)


# Start the Bot
updater.start_polling()
