from telegram import KeyboardButton, ReplyKeyboardMarkup
from sqlalchemy.orm import sessionmaker
from db.engine import engine
from db.table import products

Session = sessionmaker(bind=engine)
session = Session()

product_names = session.query(products.names).all()

names = [name[0] for name in product_names]

name_buttons = [KeyboardButton(name) for name in names]

name_button_rows = [name_buttons[i:i + 2]
                    for i in range(0, len(name_buttons), 2)]

pocket = KeyboardButton("📥Savatcha")
back_to_menu = KeyboardButton("🔙Back to Menu")

main_keyboard = [
    [pocket],
    *name_button_rows,
    [back_to_menu],
]

# Create the ReplyKeyboardMarkup
main_keyboard_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)
