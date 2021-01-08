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

dict_bot = {'id': 1408688276, 'username': 'test_shake_leg_bot', 'first_name': 'testbot'}


message_to_user = "Add this to groups that you want to notify about shaking legs"
humialiting_message = "I AM A PERSON WHO HAS NO SELF CONTROL"
user_groups = {}

# Define constants that will allow us to reuse the deep-linking parameters.
CHECK_THIS_OUT = 'check-this-out'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'


def start(update,context):
    """Sends humiliating message to chats"""
    bot = context.bot
    user = update.message.from_user
    user_groups[user['username']] = update.message.chat_id
    url = helpers.create_deep_linked_url(bot.get_me().username, CHECK_THIS_OUT, group=True)
    text = f"Add this to people you care about \n {url}"

    # update.message.reply_text(f'Howdy Good day {update.effective_chat.first_name}')
    update.message.reply_text(text)
    # send_humiliation()


def humiliate(update,context):
    """Send a deep-linked URL when the command /humiliate is issued."""
    send_humiliation()
    logging.info("sent")


def send_humiliation():
    for id, bot in user_groups.items():
        bot.send_message(id, text='Beep!')
        logging.info((str(id),str(bot)))


# Listener for "start" command
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler("humiliate",humiliate))


# Start the Bot
updater.start_polling()
