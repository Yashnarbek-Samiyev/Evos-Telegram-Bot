
from telegram import Update,  User
from telegram.ext import CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters, Updater
from db.functions.user import register
from db import table
from bot.keyboards.users import main_keyboard_markup
from bot import states
from telegram import ParseMode
import random


def start(update: Update, context: CallbackContext) -> None:

    user: User = update.effective_user
    register(user.id, user.first_name,
             user.last_name)
    update.message.reply_text(
        "Juda yaxshi birgalikda buyurtma beramizmi? 😃",
        reply_markup=main_keyboard_markup
    )

    return ConversationHandler.END


# ================================================================== Back to Menu


def back(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    start(update, context)
    return ConversationHandler.END
