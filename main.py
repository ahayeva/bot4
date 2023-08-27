import telebot
from telebot import types
import json
bot = telebot.TeleBot("6578062736:AAH-ybyQl_9x-MIjoAylOuMoOUyklNxbfa8")
with open('cafes.json', 'r', encoding='utf-8') as file:
    cafes = json.load(file)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Про бот🤖")
    item2 = types.KeyboardButton("Переглянути інформацію про заклади☕️")
    markup.add(item1, item2)

    bot.reply_to(message, "Привіт👋",
                 reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Про бот🤖")
def about_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Назад")
    markup.add(item)

    bot.reply_to(message, "Я телеграм бот який надасть вам інформацію про заклади у місті Дрогобич🏙, ви можете прочитати інформацію та дізнатись трішки більше про заклади. ",
                 reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Переглянути інформацію про заклади☕️")
def view_cafes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items = [types.KeyboardButton(cafe) for cafe in cafes]
    markup.add(*items)
    item = types.KeyboardButton("Назад")
    markup.add(item)

    bot.reply_to(message, "Оберіть заклад:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in cafes)
def cafe_info(message):
    cafe_name = message.text
    cafe_details = cafes[cafe_name]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Назад")
    markup.add(item)

    bot.send_photo(message.chat.id, cafe_details['photo'], caption=cafe_details['description'], reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Назад")
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Про бот🤖")
    item2 = types.KeyboardButton("Переглянути інформацію про заклади☕️")
    markup.add(item1, item2)

    bot.reply_to(message, "Ви повернулися назад.", reply_markup=markup)


bot.polling()