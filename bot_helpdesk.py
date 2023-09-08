import telebot, mysql.connector, time
TokenBot1 = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
bot = telebot.TeleBot(TokenBot1)
mydb = mysql.connector.connect(database='glpi', host='localhost', user='glpi', password='123')

@bot.message_handler(commands=['Ajuda']) # comando que chama a função abaixo"
def ajuda(message):
    print('Menu ajuda!...')
    bot.reply_to(message, f"""ℹ️ Bem-vindo à seção de Ajuda!\n\n
        Aqui estão algumas opções para você:\n
        /Iniciar: Abre um novo chamado.\n
        /Meus_chamados: Lista seus chamados abertos.\n\n
        ℹ️ Para acessar o GLPI, acesse: [GLPI](http://172.16.41.19/glpi)""")
    
@bot.message_handler(commands=['Abrir_chamado'])
def AbrirChamado(message):
    print('Abrir chamados!...')
    msg = bot.reply_to(message, f'🤖 Para abrir um novo chamado, informe um título:')
    bot.register_next_step_handler(msg, capturaTitulo)
def capturaTitulo (message):
    global titulo 
    titulo = message.text
    print('Capturei o titulo: -',titulo)
    msg = bot.reply_to(message, f'🤖 Conte, como podemos te ajudar?')
    bot.register_next_step_handler(msg, descricaoChamado)
def descricaoChamado (message):
    descricao = message.text
    print('Capturei a descrição: -',descricao)
    msg = bot.reply_to(message,f'🤖 Certo!... um momento pfvr....')
    # PROCESSA INFORMAÇÕES E FAZ O INSERT + COMMIT NO BANCO
    bot.send_message(message.chat.id, f'''
                     🤖 Chamado aberto com sucesso
                     ⏹️ Titulo: {titulo}
                     ⏹️ Descrição :{descricao}
                     ''')
@bot.message_handler(commands=['Meus_chamados'])
def Meus_chamados(message):
    bot.send_message(chat_id=message.chat.id,text='um momento por favor...')
    time.sleep(2)
    if mydb.is_connected():
        cursor = mydb.cursor() 
        cursor.execute("SELECT id,name FROM glpi_tickets;")
        resultados = cursor.fetchall()
        response = f"Os chamados abertos são:\n"
        for resultado in resultados:
            i=+1 # contador
            bot.reply_to(message,f'{resultado[i]}')
            lista = []
            lista.append(resultado[:])
@bot.message_handler(func=lambda message:True) # comando que chama a função abaixo respondendo toda e qualquer chamada.
def mensagemgeral(message):
    print(f'Nome do usuário que interagiu: ', message.from_user.first_name)
    firstname = message.from_user.first_name #capturando primeiro nome do user no chat
    lastname = message.from_user.last_name
    nomeuser = (f'{firstname}'+f' {lastname}')
    bot.reply_to(message,f"""
        Olá {nomeuser}, tudo bem? escolha uma das opções abaixo e toque na desejada:
        [⁉️] /Ajuda: Opções de ajuda ao usuário.
        [➕] /Abrir_chamado: Para abrir um novo chamado
        [👀] /Meus_chamados: Listar chamados abertos
        """)    
bot.infinity_polling()