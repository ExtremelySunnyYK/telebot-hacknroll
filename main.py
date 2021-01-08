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

# TOKEN = config('KEY')
TOKEN = "1582533456:AAFswg2spaHuwD0x6O3pG3ajSx4wjBuQL4s"
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

message_to_user = "Add this to groups that you want to notify about shaking legs"


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message_to_user
    )


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# Listener for "start" command
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# Start the Bot
updater.start_polling()
