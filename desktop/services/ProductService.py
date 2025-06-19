from abstracts.Api import Api
import requests

class ProductService(Api):
    def list(self):
       try:
        response = requests.get(self.BASE_URL + "/product")
        return response.json()
       
       except requests.exceptions as error: 
           print(error)
       