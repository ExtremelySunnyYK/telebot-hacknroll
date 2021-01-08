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

def start(update,context):
    """Sends humiliating message to chats"""
    bot = context.bot
    user = update.message.from_user
    user_groups[user['username']] = update.message.chat_id
    url = helpers.create_deep_linked_url(bot.get_me().username, message_to_user, group=True)
    text = f"Add this to people you care about \n {url}"

    update.message.reply_text(text)


def humiliate(update,context):
    """Send a deep-linked URL when the command /humiliate is issued."""
    send_humiliation()
    logging.info("sent")


def send_humiliation(user_name):
    for chat_id in user_groups.get(user_name):
        dict_bot.send_message(humialiting_message)
    # for id, bot in user_groups.items():
    #     bot.send_message(id, text='Beep!')
    #     logging.info((str(id),str(bot)))


# Listener for "start" command
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler("humiliate",humiliate))


# Start the Bot
updater.start_polling()
