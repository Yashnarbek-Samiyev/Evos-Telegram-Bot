from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import KeyboardButton, ReplyKeyboardMarkup

# Define your buttons
call_button = KeyboardButton("☎️Biz bilan aloqa")
order_button = KeyboardButton("🛒Buyurtma berish")
comment_button = KeyboardButton("✍️Fikr bildirish")
settings_button = KeyboardButton("⚙️Sozlamalar")

# Create a custom keyboard with your buttons
main_keyboard = [
    [call_button, order_button],
    [comment_button, settings_button]
]

main_keyboard_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)
