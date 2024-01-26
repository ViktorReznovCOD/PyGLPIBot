from Projetos.PyGLPIBot.api import Api
import auth,pprint
from faker import Faker

dados_auth=auth.credentials("basic")
api = Api(dados_auth)
session_token = Api.session_token(api)


# PROFILE
def get_my_profiles(api):
    # a resposta é um json com chave "myprofiles", valor é um array de jsons...
    response = api.call("getMyProfiles", additional_attributes=session_token)
    if "myprofiles" in response:
        my_profiles = response["myprofiles"]
        list_profiles = [profile["name"] for profile in my_profiles if "name" in profile]
        return list_profiles
    else:
        print("Erro ao obter perfis.")
        return []

def get_active_profile(api):
    pass

def change_active_profile(api):
    pass

# ENTITIES
def get_my_entities(api):
    pass
def get_active_entities(api):
    pass
def change_active_entities(api):
    pass

# ITEMS
def get_an_item(api,item_type):
    endpoint = item_type
    response = api.call(endpoint,additional_attributes=session_token)
    return response
def get_all_items(api):
    pass
def get_sub_items(api):
    pass
def get_multiple_items(api):
    pass
def add_items(api,item_type):
    fake = Faker()
    endpoint = item_type
    body = {
        "input":{"name":"computador do(a) {}".format(fake.name()),
                 "serial":"{}".format(fake.uuid4()),
                 "otherserial":"{}".format(fake.uuid4()),
                 "contact":"{}".format(fake.name()),
                 "contact_num":"{}".format(fake.phone_number()),
                 #"users_id_tech":"{}".format(random.choice()),# "id_tecnico", o padrão é o "0"
                 #"groups_id_tech":"{}".format(random.choice()),# "id_grupo_tecnico, o padrão é o "0"
                 "comment":"{}".format(fake.text()),
                #  "users_id":"{}".format(random.choice()),#"id do usuário, o padrão é o "0"
                #  "groups_id":"{}".format(random.choice()),# id do grupo, o padrão é o "0"
                #  "status"
        }
    }
    response = api.call(endpoint,method="POST",additional_attributes=session_token,body=body)
    return response
    


def _main():
    # a=add_items(api,"Computer")
    # print(a)
    itens = get_an_item(api,"Computer")
    pprint.pprint(itens)
    
if __name__ == "__main__":
    _main()