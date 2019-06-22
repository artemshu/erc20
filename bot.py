import config
import telebot
import datetime
import Bitr
import graph
from telebot import apihelper
from telebot import types
from pycbrf.toolbox import ExchangeRates
from kucoin.client import Client

#Создаем объекты бота, даты, курсов валют, клавиатуры
#apihelper.proxy = {'https':config.proxy}
bot = telebot.TeleBot(config.token)
datenow = datetime.datetime.now()
rates = ExchangeRates(datenow)
markup = types.ReplyKeyboardMarkup()
markup.row('Как пользоваться ботом?')
markup.row('Другие валюты')
markup.row('Информация')
markup.row('Графики')

#Отслеживаем сообщения
@bot.message_handler(content_types=["text"])
def messageKu(message):
    if message.text=='ETH' or message.text=='BTC':
        bot.send_message(message.chat.id,'Пожалуйста введите ERC20 токен')        
    if message.text == 'Как пользоваться ботом?':
            bot.send_message(message.chat.id,"Введите обозначение ERC20 токена тpемя заглавными латинскими буквами.",reply_markup=markup)
    if message.text == 'Другие валюты':
            usd = str(rates['USD'].value)
            eur = str(rates['EUR'].value)
            gbp = str(rates['GBP'].value)
#            eth = str(Ku.get_eth()*int(rates['USD'].value))
            money = 'USD : ' + usd + '\n' + 'EUR : '+ eur +'\n' + 'GBP : '+ gbp +'\n'
            bot.send_message(message.chat.id,money,reply_markup=markup)            
    if message.text == 'Информация':
            bot.send_message(message.chat.id,"*Здесь может быть какая-то информация*",reply_markup=markup)       
    if message.text=='/start':
            bot.send_message(message.chat.id,"Введите обозначение ERC20 токена тpемя заглавными латинскими буквами.",reply_markup=markup)        
    if message.text.isupper()==True:
        coin=message.text
        bot.send_message(message.chat.id,"Bittrex: "+ Bitr.get_bitr(coin),reply_markup=markup)
    if message.text.isupper()==False and len(message.text)==3:
            bot.send_message(message.chat.id,"Введите обозначение ERC20 токена тpемя заглавными латинскими буквами.",reply_markup=markup)
    if message.text == 'Графики':
            graph.create_maxmin()
            graph.create_middle()
            maxmin = open('maxmin.png', 'rb')
            middle = open('middle.png', 'rb')
            bot.send_photo(message.chat.id,maxmin,reply_markup=markup)
            bot.send_photo(message.chat.id,middle,reply_markup=markup)
#Запускаем прослушавание новых сообщений        
if __name__ == '__main__':
		bot.polling(none_stop=True)
