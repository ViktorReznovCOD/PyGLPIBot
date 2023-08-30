import telebot, mysql.connector, time

TokenBot1 = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
bot = telebot.TeleBot(TokenBot1)
bot.delete_webhook()
#mydb = mysql.connector.connect(database='glpi', host='localhost', user='glpi', password='123')
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
@bot.message_handler(commands=['Iniciar'])
def iniciar(message):
    bot.reply_to(message,'''
        🤖 Descrição do Problema: Por favor, descreva detalhadamente qual é o problema ou a solicitação que você está enfrentando no GLPI:       
                 ''')
@bot.message_handler(commands=['Ajuda']) # comando que chama a função abaixo"
def ajuda(message):
    print('menu ajuda')
    bot.reply_to(message, "Tudo sobre ajuda.................")

@bot.message_handler(commands=['Meus_chamados'])
def Meus_chamados(message):
    #feedback terminal
    print('Usuário selecionou "Meus_chamados()"')
    bot.send_message(chat_id=message.chat.id,text='um momento por favor...')

@bot.message_handler(func=lambda message:True) # comando que chama a função abaixo respondendo toda e qualquer chamada.
def mensagemgeral(message):
    print(f'Nome do usuário que interagiu: ', message.from_user.first_name)
    firstname = message.from_user.first_name #capturando primeiro nome do user no chat
    lastname = message.from_user.last_name
    name = (f'{firstname}'+f' {lastname}')
    print(f'ID user:', message.chat.id)  
    bot.reply_to(message,f"""
        Olá {name}, escolha uma das opções abaixo e toque na desejada:
        /Ajuda: Opções de ajuda ao usuário.
        /Iniciar: Abrir um novo chamado.
        /Meus_chamados: Listar chamados abertos
                 """)    
bot.infinity_polling()