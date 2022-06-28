from telebot import TeleBot,types
from prices_now import prices

bot = TeleBot('YOUR TOKEN')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    text = 'Hello there!' +'\n''I’m monitoring prices for Magic Eden (Now only Magic Ticket collection).' +'\n''Write /prices_now if you want to know the lowest prices for each Tier!'
    bot.send_message(message.chat.id, text=text, reply_markup=actions())


@bot.message_handler(commands=['prices_now'])
def price(message):
    prices_now = prices()
    text = 'Lowest price for Normie is ' + str(prices_now[0]) + ' sol' +\
           '\n' 'Lowest price for Degen is ' + str(prices_now[1]) + ' sol' +\
           '\n' 'Lowest price for OG is ' + str(prices_now[2]) + ' sol'

    bot.send_message(message.chat.id, text)

def actions():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button_pricesnow = types.KeyboardButton('/prices_now')
    keyboard.add(button_pricesnow)

    return keyboard


bot.polling(none_stop=True, interval=0)



