
import telebot
import requests
from telebot import types
import urllib

bot = telebot.TeleBot("1116569811:AAGYSoDPFrRxpNd5uPnt_6Wqv2IxDOFA3Kk")

markup = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
btn1 = types.KeyboardButton('/Онлайн-трекшен')
btn2 = types.KeyboardButton('/Скайпы')
btn3 = types.KeyboardButton('/НСС')
btn4 = types.KeyboardButton('/Оплаты')

markup.add(btn1, btn2, btn3, btn4)

@bot.message_handler(commands = ['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, человечек! Чем тебе помочь?', reply_markup=markup)

@bot.message_handler(commands = ['Онлайн-трекшен'])
def start_message2(message):
    bot.send_message(message.chat.id, 'Онлайн-трекшен - это программа развития', reply_markup=markup)

@bot.message_handler(regexp ='йоу')
def reply_virus(message):
    sticker_id = "CAACAgIAAxkBAAI3mV56KzjgXZ3-wyIxLUO6xipXgBtHAAK2CQACeVziCcZOco3KlyVIGAQ"
    bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(regexp ='космос')
def reply_space(message):
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    data = requests.get(url).json()

bot.polling()