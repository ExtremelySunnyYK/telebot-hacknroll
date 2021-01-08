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


message_to_user = "Add this to groups that you want to notify about shaking legs"
humialiting_message = "I AM A PERSON WHO HAS NO SELF CONTROL"
mybots = {}

# Define constants that will allow us to reuse the deep-linking parameters.
CHECK_THIS_OUT = 'check-this-out'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'


def start(update,context):
    """Sends humiliating message to chats"""
    bot = context.bot
    mybots[update.message.chat_id] = bot
    url = helpers.create_deep_linked_url(bot.get_me().username, CHECK_THIS_OUT, group=True)
    text = f"Add this to people you care about \n {url}"

    update.message.reply_text(f'Howdy Good day {update.effective_chat.first_name}')
    update.message.reply_text(text)
    

def deeplink(update,context):
    pass

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    send_humiliation()

def humiliate(update,context):
    """Send a deep-linked URL when the command /humiliate is issued."""
    bot = context.bot

    update.message.reply_text("hi")

    mybots[update.message.chat_id] = context.bot
    print(mybots)


def send_humiliation():
    for id, bot in mybots.items():
        bot.send_message(id, text='Beep!')

# Listener for "start" command
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler("humiliate",humiliate))


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# Start the Bot
updater.start_polling()
