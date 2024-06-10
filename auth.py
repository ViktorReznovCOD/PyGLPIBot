import json

class Auth():
    def __init__(self, flag, json_path="auth_data.json"):
        with open(json_path, "r") as auth_data:
            self.flag =  flag
            self.dados  = json.load(auth_data)

        
    def get_data(self):
        try:
            if self.flag == "glpi":
                return self.dados[self.flag]
            
            elif self.flag == "telegram":
                return self.dados[self.flag]
        
        except Exception as e :
            return e

# if __name__ in '__main__':
#     print(Auth("glpi").get_data())    