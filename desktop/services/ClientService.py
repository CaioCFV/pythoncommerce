from abstracts.Api import Api
import requests

class ClientService(Api):
    def list(self):
       try:
        response = requests.get(self.BASE_URL + "/client")
        return response.json()
       
       except requests.exceptions as error: 
           print(error)
       