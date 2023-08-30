import telebot
import mysql.connector

TokenBot1 = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
TokenBot2 = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
bot = telebot.TeleBot(TokenBot1)
bot2 = telebot.TeleBot(TokenBot2)
bot.delete_webhook()
mydb = mysql.connector.connect(database='glpi', host='localhost', user='glpi', password='123')
'''
if mydb.is_connected():
    @bot.message_handler(commands=['inciar', 'ajuda'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot.infinity_polling()
else:
    print("Não conectou...")
'''
@bot.message_handler(commands=['iniciar'])
def iniciar(message):
    bot.reply_to(message,"Deseja abrir um chamado?")
@bot.message_handler(commands=['ajuda']) # comando que chama a função abaixo"
def ajuda(message):
    print('menu ajuda')
    bot.reply_to(message, "Tudo sobre ajuda.................")
@bot.message_handler(func=lambda message:True) # comando que chama a função abaixo respondendo toda e qualquer chamada.
def mensagemgeral(message):
    bot.reply_to(message, """
        Mensagem padrão
        /ajuda: Opções de ajuda ao usuário.
        /iniciar: Abrir um novo chamado.        
""")
bot.infinity_polling()