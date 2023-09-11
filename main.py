import telebot, mysql.connector, time
from telebot import types
TokenBot1 = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
bot = telebot.TeleBot(TokenBot1)
mydb = mysql.connector.connect(database='glpi', host='localhost', user='glpi', password='123')
# Crie um comando ou função que será acionado quando o botão for pressionado
@bot.message_handler(commands=['share'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = telebot.types.KeyboardButton('Compartilhar Contato', request_contact=True)
    markup.add(button)

    bot.send_message(message.chat.id, "Olá! Clique no botão abaixo para compartilhar seu contato:", reply_markup=markup)

# Defina um manipulador para lidar com o contato compartilhado pelos usuários
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_contact = message.contact.phone_number

    bot.send_message(user_id, f"Obrigado, {user_name}! Seu contato ({user_contact}) foi compartilhado com o bot com sucesso.")

# Inicie o bot
bot.polling()