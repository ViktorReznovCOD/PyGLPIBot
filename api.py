import requests, pprint
import base64
import time
class Api:
    def __init__(self,user_token):
        self.user_token = user_token
        self.urlv1 = "http://localhost/glpi/glpi/apirest.php/"
        self.max_retries = 10
        self.seconds_time_between_retries = 3
        self.headers = {
            "Authorization":"Basic {}".format(user_token)
        }

    def call(self, endpoint, method="GET", additional_attributes={}, body=None, retry=0):
        finalurl = self.urlv1 + endpoint
        
        if additional_attributes:
            self.headers["Session-Token"]=additional_attributes
        else:
            pass
        
        try:
            if method == "POST":
                response = requests.post(finalurl,headers=self.headers,json=body)
            else:
                response = requests.get(finalurl, headers=self.headers)
        
            if response.status_code==400:
                print(response.url)
                print(response.text)
                time.sleep(10)
                raise Exception("response.status_code == 400")
            elif response.status_code==401:
                print(response.url)
                print(response.text)
                raise Exception("response.status_code == 401")
            return response.json()
        
        except Exception as err:
            retry +=1
            if retry < self.max_retries:
                print("Failed due to {}. Waiting for {} seconds before attepting {} to {}".format(err,self.seconds_time_between_retries,retry, self.max_retries))
                time.sleep(self.seconds_time_between_retries)
                return self.call(endpoint, method, additional_attributes, body, retry)
            else:
                raise Exception("Maximum number of attempts exceeded",err)
   
    def session_token(api):
        response = api.call("initSession")
        session_token = response['session_token']
        return session_token
