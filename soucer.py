from api import Api
import auth,pprint
from faker import Faker # usado na criação de dados sintéticos

dados_auth=auth.credentials("basic") # dados de autenticação nos sistemas (tokens, usuarios, senhas e etc.)
api = Api(dados_auth) 
session_token = Api.session_token(api)

def adicionar_chamado(dados_chamado): # OK
    deu_certo = False
    try:
            
        _api = api
        endpoint = "Ticket"
        body = {
            "input": {
                "name":dados_chamado["name"],
                "content":dados_chamado["content"],
                "comment":dados_chamado["comment"],
                "users_id_recipient":374
            }
        }
        response = api.call(endpoint,"POST",additional_attributes=session_token,body=body)
        if api.call.status_code == 200:
            print(response)
            deu_certo = True
            return deu_certo
        else:
            print("--debug DEU CERTO É {}".format(deu_certo))
            return deu_certo
    except Exception as e:
        print("--debug\n falha na função -> adicionar_chamado(dados_chamado)\nerror: {}".format(e))
        
def _main():
    # a=add_items(api,"Computer")
    # print(a)
    # itens = get_an_item(api,"Computer")
    pass
if __name__ == "__main__":
    _main()