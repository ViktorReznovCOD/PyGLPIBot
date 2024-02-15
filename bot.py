import telebot
import datetime,auth,soucer
bot = telebot.TeleBot(auth.credentials("telegram"),parse_mode="HTML")
hora_atual = datetime.datetime.now()
hora_formatada = hora_atual.strftime("%H:%M:%S")
import time


# infos do bot ativo
# sexta_feira = bot.get_me()
# sexta_feita_id = sexta_feira.id
# sexta_feira_first_name = sexta_feira.first_name
# sexta_feira_can_join_groups = sexta_feira.can_join_groups
# sexta_feira_can_read_all_group_messages = sexta_feira.can_read_all_group_messages
class Chamado:
    """
    _summary_
    
    Classe chamado
    """
    print("--debug Classe Chamado")
    def __init__(self, chamado={}):
        print("--debug passando pelo init de chamado")
        chamado['titulo'] = self.titulo
        chamado['descricao'] = self.descricao
        print(chamado)
        
class Usuario:
    """
    _summary_
    
    Classe usuario
    """
    print("--debug classe Usuario")     
    def __init__(self, nome, id):
        print("--debug passando pelo init de usuario")
        self.nome = nome
        self.id = id

# Adicionar um argunmento para o comando "python3 bot.py".
# exemplo python3 bot.py debug = True

# MENU DE AJUDA DEVE RESPONDER UMA MENSAGEM CONTENDO A LISTA DE COMANDOS PRESENTE NESSE ARQUIVO.
@bot.message_handler(commands=['ajuda']) # comando que chama a função abaixo"
def ajuda(message):
    bot.reply_to(message,"""ℹ️ Bem-vindo à seção de Ajuda!\n
        Aqui estão algumas opções para você:
        /Ajuda: Menu de ajuda.
        /Abrir_chamado: Abre um novo chamado.
        /Meus_chamados: Lista seus chamados abertos.
        /listar_contatos: listar usuarios e contatos do GLPI
        /share: Compartilhar contato.\n
        ℹ️ Para acessar o GLPI, acesse: [GLPI](http://urldoglpi.inrtranet)""")

#
# @bot.message_handler(commands=['share'])
# def share(message):
#     print(message)
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     button = telebot.types.KeyboardButton('Compartilhar Contato', request_contact=True)
#     markup.add(button)
#     bot.send_message(message.chat.id, "Olá! Clique no botão abaixo para compartilhar seu contato:", reply_markup=markup)

#
@bot.message_handler(commands=['novochamado'])
def novochamado(message):
    print("--debug novochamado")
    nome_usuario = message.from_user.first_name
    bot.reply_to(message," {} deseja abrir um chamado?".format(nome_usuario))
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("Sim"), telebot.types.KeyboardButton("Não"))
    bot.register_next_step_handler(message,novochamado2)
    # bot.send_message(message.chat.id, "Por favor, selecione uma opção", reply_markup=markup)
def novochamado2(message):
    try:
        if message.text == "Sim":
            print("--debug SIM")
        elif message.text == "Não":
            print("--debug NÃO")
        else:
            print("--debug ELSE")
    except Exception as e:
        bot.reply_to(message,"Ops")
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text.lower() == "sim":
#         bot.reply_to(message,"Ótimo! Vou abrir um chamado.")
#     elif message.text.lower() == "não":
#         bot.reply_to(message,"Tudo bem, se precisar de ajuda, estou aqui.")
#     else:
#         bot.reply_to(message, "Desculpe, não entendi. Por favor, selecione 'sim' ou 'não'.")

@bot.message_handler(commands=['meus_chamados'])
def meus_chamados(message):
    a = message
    print(a)
#

# MENSAGEM GERAL
"""
Para qualquer interação o bot responde isso...
"""
@bot.message_handler(func=lambda message:True) 
def mensagedefault(message):
    print("--debug mensagedefault")
    
    nome_usuario = message.from_user.first_name
    bot.reply_to(message,"""
    Olá <b>{}</b>    escolha uma das opções abaixo e toque na desejada:\n
    <b>[❓]/Ajuda:</b> Ajuda ao usuário.
    <b>[🚀]/start:</b> Interações iniciais
        """.format(nome_usuario),parse_mode="html")

bot.infinity_polling()