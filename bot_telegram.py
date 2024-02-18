import telebot
import auth
import datetime
from soucer import adicionar_chamado

class Bot:
    def __init__(self,token):
        self.bot = telebot.TeleBot(token,parse_mode="HTML")
        self.sexta_feira = self.bot.get_me()
        self.sexta_feita_id = self.sexta_feira.id
        self.sexta_feira_first_name = self.sexta_feira.first_name
        self.sexta_feira_can_join_groups = self.sexta_feira.can_join_groups
        self.sexta_feira_can_read_all_group_messages = self.sexta_feira.can_read_all_group_messages
    def novo_chamado(self):
        @self.bot.message_handler(commands=['novochamado'])
        # Passo 1: Iniciar o chamado perguntando ao usuário detalhes sobre o problema a ser relatado.
        def iniciar_abertura_chamado(message):
            try:
                # mensagem orientando sobre a descrição do chamado
                self.first_name = message.from_user.first_name
                self.bot.reply_to(message,"""Olá <b>{}</b>! 😊
                                
                    Preciso entender melhor o que está acontecendo para poder te ajudar da melhor forma possível! Por favor, compartilhe comigo uma descrição do problema que você está enfrentando. 
                    
                    Por exemplo:
                    <i>"Minha impressora não está funcionando."</i>
                    
                    <i>"Não consigo acessar meu e-mail."</i>
                    
                    Quanto mais detalhes você fornecer, mais fácil será para mim entender e resolver o seu problema. Estou aqui para ajudar! 💬""".format(self.first_name))
                self.bot.register_next_step_handler(message,finalizar_abertura_chamado)
            except Exception as e:
                print("Ops {}".format(e))
                self.bot.reply_to(message, "Ops {}".format(e))
        def finalizar_abertura_chamado(message):
            # print(message)
            momento_insercao = datetime.datetime.now()
            print(momento_insercao)
            dados_chamado = {
                "name":"(novo chamado!) {}".format(message.text[:30]),
                "content":"{}".format(message.text),
                "comment":"Chamado aberto via API - {}".format(momento_insercao)
            }
            adicionar_chamado(dados_chamado)
            if adicionar_chamado == True:
                self.bot.reply_to(message, "Certo {}, seu chamado foi aberto com sucesso. Em alguns instantes nossa equipe irá retornar o contato.".format(self.first_name))
            else:
                self.bot.reply_to(message,"Chamado não foi aberto.")
    def listar_chamados(self):
        @self.bot.message_handler(commands=['meuschamados'])
        def meus_chamados(message):
            self.bot.reply_to(message,"Lista de chamados:\n .\n .\n .")

    def mensagens_padroes(self):
        @self.bot.message_handler(commands=['ajuda']) # comando que chama a função abaixo"
        def ajuda(message):
            self.bot.reply_to(message,"""
            🤖<b>Ajuda</b>
            Aqui estão algumas opções para você:
            /ajuda:         Exibe este menu de ajuda.
            /novochamado:   Abre um novo chamado.
            /meuschamados:  Lista seus chamados abertos.
            ℹ️ Para acessar o GLPI, acesse: [GLPI](http://urldoglpi.inrtranet)
""")

        @self.bot.message_handler(func=lambda message:True) 
        def mensagedefault(message):
            print("--debug mensagedefault")
            
            nome_usuario = message.from_user.first_name
            self.bot.reply_to(message,"""
Olá <b>{}</b>! 👋 Obrigado por entrar em contato conosco. Como posso ajudar você hoje? Por favor, digite sua mensagem ou toque no comando abaixo para receber ajuda: \n
<b>[❓]/ajuda:</b> Ajuda ao usuário.
                """.format(nome_usuario),parse_mode="html")

    def run(self):
        self.novo_chamado()
        self.listar_chamados()
        self.mensagens_padroes()
        self.bot.infinity_polling()
        
if __name__ == "__main__":
    
    bot = Bot(auth.credentials("telegram"))
    bot.run()