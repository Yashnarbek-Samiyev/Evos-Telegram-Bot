from db.table import category
from telegram import KeyboardButton, ReplyKeyboardMarkup
from sqlalchemy.orm import sessionmaker
from db.table import category
import sqlalchemy as db
engine = db.create_engine(
    'postgresql+psycopg2://postgres:1223@localhost:5432/evos')


Session = sessionmaker(bind=engine)
session = Session()
category_names = session.query(category.name).all()
names = [name[0] for name in category_names]

pocket = KeyboardButton("📥Savatcha")
name_buttons = [KeyboardButton(name) for name in names]

name_button_rows = [name_buttons[i:i + 2]
                    for i in range(0, len(name_buttons), 2)]
print(name_button_rows)
back_to_menu = KeyboardButton("Back to Menu")

main_keyboard = [
    [pocket],
    *name_button_rows,
    [back_to_menu],
]

main_keyboard_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)
