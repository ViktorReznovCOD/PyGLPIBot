"""
resumo de sintaxe para edição de caracteres nas mensagens do telegram
            *bold \*text*
            _italic \*text_
            __underline__
            ~strikethrough~
            ||spoiler||
            *bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
            [inline URL](http://www.example.com/)
            [inline mention of a user](tg://user?id=123456789)
            ![👍](tg://emoji?id=5368324170671202286)
            `inline fixed-width code`
            ```
            pre-formatted fixed-width code block
            ```
            ```python
            pre-formatted fixed-width code block written in the Python programming language
            ```
"""
import telebot, datetime
from telebot import types

bot = telebot.TeleBot(tokenBot)
hora_atual = datetime.datetime.now()
hora_formatada = hora_atual.strftime("%H:%M:%S")

nome_usuario = ""
sobrenome_usuario = ""
id_chat = 0
listacontatos = [('felipe.camelo','5591993937398'),('felipe.mendes','5591985650608')]
 
@bot.message_handler(commands=['Ajuda']) # comando que chama a função abaixo"
def ajuda(message):
    bot.reply_to(message, f"""ℹ️ Bem-vindo à seção de Ajuda!\n
        Aqui estão algumas opções para você:
        /Ajuda: Menu de ajuda.
        /Abrir_chamado: Abre um novo chamado.
        /Meus_chamados: Lista seus chamados abertos.
        /share: Compartilhar contato.\n
        ℹ️ Para acessar o GLPI, acesse: [GLPI](http://urldoglpi.inrtranet)""")
#
@bot.message_handler(commands=['share'])
def share(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = telebot.types.KeyboardButton('Compartilhar Contato', request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id, "Olá! Clique no botão abaixo para compartilhar seu contato:", reply_markup=markup)
#
@bot.message_handler(commands=['Abrir_chamado'])
def abrirChamado(message):
    global nome_usuario
    nome_usuario = message.from_user.first_name
    print(f'-2- {nome_usuario} está abrindo um chamado, {hora_formatada}')
    msg = bot.reply_to(message, f'🤖 Para abrir um novo chamado, informe um título:')
    bot.register_next_step_handler(msg, capturaTitulo)
#
def capturaTitulo (message):
    global titulo 
    titulo = message.text
    print('Capturei o titulo: -',titulo)
    msg = bot.reply_to(message, f'🤖 Conte, como podemos te ajudar?')
    bot.register_next_step_handler(msg, descricaoChamado)
#
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
    #bot.send_message(user_id, f"Obrigado, {user_name}! Seu contato ({user_contact}) foi compartilhado com o bot com sucesso.")
#
@bot.message_handler(commands=['Meus_chamados'])
def Meus_chamados(message):
   pass
#
@bot.message_handler(content_types=['contact'])
def captura_contato(message):
    contato = message.contact.phone_number
    contatoexistente = any(contato==listacontatos[1] for i in listacontatos)
    print(f'Numero de quem interagiu: {contato}')
    print(f'Lista de contatos: {listacontatos}')
    if contatoexistente:
        print(f'Contato existe!')
    else:
        print(f'Contato não existe')
    return message.contact.phone_number
#
@bot.message_handler(func=lambda message:True) #if message.content_type == 'contact' else True) comando que chama a função abaixo respondendo toda e qualquer chamada + compartilhamento de contato
def mensagemgeral(message):
    global nome_usuario
    nome_usuario = message.from_user.first_name #capturando primeiro nome do user no chat
    bot.reply_to(message,f"""
    Olá <b>{nome_usuario}</b>, tudo bem? escolha uma das opções abaixo e toque na desejada:\n
    <b>[⁉️]/Ajuda:</b> Opções de ajuda ao usuário.
    <b>[➕] /Abrir_chamado:</b> Para abrir um novo chamado
    <b>[👀] /Meus_chamados:</b> Listar chamados abertos
        """,parse_mode="html")
#
bot.infinity_polling()