import telebot, mysql.connector, time
TokenBot1 = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
bot = telebot.TeleBot(TokenBot1)
mydb = mysql.connector.connect(database='glpi', host='localhost', user='glpi', password='123')

''' bot.delete_webhook()
é usada em bots do Telegram para desativar o webhook previamente configurado. Um webhook é uma forma de receber atualizações em tempo real do Telegram sempre que um evento ocorre em uma conversa com o bot, como quando um usuário envia uma mensagem.

Quando um webhook está ativo, o Telegram envia automaticamente as atualizações para o URL especificado no webhook, em vez de você ter que verificar constantemente o servidor do Telegram em busca de novas mensagens. Isso pode ser útil em cenários em que você deseja que seu bot responda instantaneamente às mensagens dos usuários.

No entanto, há situações em que você pode querer desativar o webhook. Por exemplo:

Depuração e teste: Durante o desenvolvimento de um bot, você pode querer desativar o webhook temporariamente para facilitar o teste e a depuração do código do bot sem que as atualizações sejam enviadas automaticamente para o seu servidor.

Mudança de abordagem: Se você estava usando um webhook e decide mudar para um método de polling (verificação periódica das atualizações) para receber mensagens, você deve desativar o webhook.

Manutenção do servidor: Em alguns casos, você pode precisar desativar o webhook temporariamente para manutenção do servidor onde o bot está hospedado.

Para desativar o webhook e voltar a usar o método de polling para receber mensagens, você pode chamar a função bot.delete_webhook().

Exemplo de uso:

python
Copy code

import telebot

# Inicialize o bot
bot = telebot.TeleBot("TOKEN_DO_SEU_BOT")

# Desative o webhook
bot.delete_webhook()

# Resto do seu código para configurar a interação com os usuários usando polling
bot.infinity_polling()
Lembre-se de que, após desativar o webhook, você precisará usar um loop de polling, como bot.infinity_polling(), para verificar e responder às mensagens dos usuários.


'''
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