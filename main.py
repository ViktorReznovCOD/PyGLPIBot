import telebot, mysql.connector,mysql, time
import threading
import datetime
# aqui posso setar a chave de api importando o token de um arquivo .txt
TokenBot = "5831647116:AAHDf0kOEPaEBZk5-W05gQZueSFuyzsdDDA"
bot = telebot.TeleBot(TokenBot)
bot.delete_webhook()
mydb = mysql.connector.connect(database='glpiteste01', host='localhost', user='glpiuser', password='glpipass')

@bot.message_handler(commands=['start','help'])
def boasvindas(message):
    bot.reply_to(message,"Como posso te ajudar?")
@bot.message_handler(commands=["chamados"])
def chamados(mensagem):
    bot.send_message(mensagem.chat.id, f"""
clique em uma opção
- /statusNovo -: LISTAR NOVOS CHAMADOS
- /statusEmAtendimento - : LISTAR EM ATENDIMENTO
- /sttsatribuidospmim - : LISTAR OS CHAMADOS ATRIBUIDOS PRA MIM
- /NovoChamado               
""")
@bot.message_handler(commands=["NovoChamado"])
def AbrirChamado(menssagem):
    if mydb.is_connected():
        cur = mydb.cursor()
        var1 = input('Insira o titulo do chamado: ')
        var2 = input('Insira a descricao do chamado: ')
        query = f"INSERT INTO glpi_tickets (name, content) VALUES ('{var1}','{var2}')"
        print(query)
        cur.execute(query)
        mydb.commit()
        time.sleep(1)
        bot.send_message(menssagem.chat.id, f"Chamado aberto com sucesso")
    time.sleep(2)
    responder(menssagem) 
@bot.message_handler(commands=["statusNovo"])
def sttsnovo(mensagem):
    mydb = mysql.connector.connect(database='glpiteste01', host='localhost', user='glpiuser', password='glpipass')
    if mydb.is_connected():
        cur = mydb.cursor()
        query = 'select id,name from glpi_tickets where status = 1'
        cur.execute(query)
        resultado = cur.fetchall()
        contador=0
        for i in resultado:
            contador = contador+1
        bot.send_message(mensagem.chat.id, f"QUANTIDADE DE NOVOS CHAMADOS: {contador}\n")
        if resultado is None:
            bot.send_message(mensagem.chat.id, f"{resultado}")
    time.sleep(5)
    responder(mensagem)
@bot.message_handler(commands=["statusEmAtendimento"])
def sttsatendimento(mensagem):
    if mydb.is_connected():
        cur = mydb.cursor()
        query = 'select id,name from glpi_tickets where status = 2'
        cur.execute(query)
        resultado = cur.fetchall()
        contador=0
        for i in resultado:
            contador = contador+1
        bot.send_message(mensagem.chat.id, f"QUANTIDADE DE CHAMADOS EM ATENDIMENTO: {contador}\n")
        if resultado is None:
            bot.send_message(mensagem.chat.id, f"{resultado}")
    time.sleep(5)
    responder(mensagem)
@bot.message_handler(commands=["sttsatribuidospmim"])
def sttsatribuidospmim(mensagem):
    if mydb.is_connected():
        cur = mydb.cursor()
        query = 'select id,name from glpi_tickets where users_id_recipient = 7'
        cur.execute(query)
        resultado = cur.fetchall()
        contador=0
        for i in resultado:
            contador = contador+1
        bot.send_message(mensagem.chat.id, f"QUANTIDADE DE CHAMADOS ATRIBUÍDOS A MIM: {contador}\n")
        if resultado is None:
            bot.send_message(mensagem.chat.id, f"{resultado}")
    time.sleep(5)
    responder(mensagem)