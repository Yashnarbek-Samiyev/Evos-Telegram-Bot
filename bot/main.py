import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from bot import config
from bot.handlers import user
from bot.keyboards import users
from bot.keyboards import category
from bot.keyboards import products
from bot import states

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# CREATE EXTENSION postgis
logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', user.start),
            CommandHandler('stop', user.back),
            CallbackQueryHandler(users.main_keyboard_markup,
                                 pattern='^menu' + str(states.MENU) + '$'),
            CallbackQueryHandler(category.main_keyboard_markup,
                                 pattern='^category' + str(states.CATEGORY) + '$'),
            CallbackQueryHandler(products.main_keyboard_markup,
                                 pattern='^products' + str(states.PRODUCTS) + '$'),

        ],
        states={
            states.MENU: [


            ],
            states.CATEGORY: [
            ],
            states.PRODUCTS: [
            ],
        },
        fallbacks=[CommandHandler('start', user.start)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
