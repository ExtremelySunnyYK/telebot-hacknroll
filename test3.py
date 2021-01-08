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

    text = ""
    if chat_id > 0: 
        text = f"Add this to people you care about \n {url}"
    else:
        text = f"Your group id is: \n{chat_id}\n Add this to Shake Master!"

    update.message.reply_text(f'Howdy Good day {update.effective_chat.first_name}')
    update.message.reply_text(text)


def humiliate(update, context):
    """Send a deep-linked URL when the command /humiliate is issued."""
    global BOT
    print("BOT: ", BOT)
    send_humiliation(update.message.from_user["username"])
    logging.info("sent")


def send_humiliation(user_name):
    for chat_id in user_groups[user_name]:
        BOT.send_message(chat_id=chat_id, text=humialiting_message)


# Listener for "start" command
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler("humiliate", humiliate))


# Start the Bot
updater.start_polling()
