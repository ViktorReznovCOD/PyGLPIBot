import telebot, mysql.connector, time
from telebot import types
TokenBot1 = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
bot = telebot.TeleBot(TokenBot1)
mydb = mysql.connector.connect(database='glpi', host='localhost', user='glpi', password='123')

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="Share your phone number", request_contact=True)
    keyboard.add(reg_button)
    response = bot.send_message(message.chat.id, 
                                "You should share your phone number", 
                                reply_markup=keyboard)
    print(response.contact)  # response.contact = None here

if __name__ == '__main__':
    bot.polling(none_stop=True)

