import telebot
from telebot import types
from config import keys, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

def create_markup(quote=None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for val in keys.keys():
        if val != quote:
            buttons.append(types.KeyboardButton(val.capitalize()))

    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Увидеть список всех доступных валют: /values\n Чтобы начать конвертацию нажните команду /convert '
    bot.send_message(message.chat.id, 'Привет')
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def base_values(message:telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['convert'])
def values(message: telebot.types.Message):
    text = 'Выберете валюту из которой хотите конвертировать'
    bot.reply_to(message, text, reply_markup=create_markup())
    bot.register_next_step_handler(message, quote_handler)

def quote_handler(message: telebot.types.Message):
    quote = message.text.strip().lower()
    text = 'Выберете валюту в которую хотите конвертировать'
    bot.reply_to(message, text, reply_markup=create_markup(quote))
    bot.register_next_step_handler(message, base_handler, quote)

def base_handler(message: telebot.types.Message, quote):
    base = message.text.strip().lower()
    text = 'Выберете количество конвертируемой валюты'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, amount_handler, quote, base)

def amount_handler(message: telebot.types.Message, quote, base):
    amount = message.text.strip()
    try:
        new_price = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка конвертации: \n {e}")
    else:
        text =f'Цена {amount} {quote} в {base} - {new_price:.2f}'
        bot.reply_to(message, text)

bot.polling()
