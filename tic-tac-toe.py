import os
import dotenv
import telebot
import pyrebase
from telebot.types import InputMediaPhoto
from telebot.types import KeyboardButton
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineQueryResultArticle
from telebot.types import InputTextMessageContent
from telebot.types import InlineQueryResultPhoto
from telebot import custom_filters
from telebot.util import content_type_media
from telebot.util import content_type_service

config = {

    "apiKey"              : "AIzaSyCeryYrvAQkde8ZCi4DQZ6qy6Q_VXmDc-c",
    "authDomain"          : "tic-tac-toe-912cb.firebaseapp.com",
    "databaseURL"         : "https://tic-tac-toe-912cb-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId"           : "tic-tac-toe-912cb",
    "storageBucket"       : "tic-tac-toe-912cb.appspot.com",
    "messagingSenderId"   : "20753345181",
    "appId"               : "1:20753345181:web:4d30053306d49d2a7e8274",
    "measurementId"       : "G-2925GBY7J4"   
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_API_KEY_1"), parse_mode="HTML")


def create_game_board():    # Creates the game board

    game_board, buttons = InlineKeyboardMarkup(row_width = 3), []

    for _ in range(1,10):
        buttons.append(InlineKeyboardButton(" ", callback_data=f'{_}'))

    game_board.add(*buttons)

    return game_board

@bot.message_handler(commands="start")
def start(message):

    bot.send_message(message.chat.id, "<b>Wanna a play a game of Tic-Tac-Toe?\n\
    \nClick the buton and play with your friends!</b>",
    reply_markup = InlineKeyboardMarkup().row(InlineKeyboardButton("Play Tic-Tac-Toe!",
    switch_inline_query="tic_tac_toe")))

@bot.inline_handler(lambda query: query.query == 'tic_tac_toettt')
def send_game(query):

    choose = InlineKeyboardMarkup()
    X = InlineKeyboardButton("x", callback_data="x")
    O = InlineKeyboardButton("o", callback_data="o")
    choose.row(X,O)

    try:
        t_t_t = InlineQueryResultArticle('start_game',
        "ᴘʟᴀʏ ᴛɪᴄ-ᴛᴀᴄ-ᴛᴏᴇ 😄", InputTextMessageContent("<b>Play Tic-Tac-Toe!</b>",
        parse_mode="HTML"),reply_markup=choose, thumb_url="https://ibb.co/3hjt7xX")
        bot.answer_inline_query(query.id, [t_t_t])
    except:
        pass

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):

    PO = call.from_user.id
    game = call.inline_message_id

    print(button, player, game)


bot.infinity_polling()