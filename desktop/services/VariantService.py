from abstracts.Api import Api
import requests

class VariantService(Api):
    def list(self):
       try:
        response = requests.get(self.BASE_URL + "/variant")
        return response.json()
       
       except requests.exceptions as error: 
           print(error)
       