from abstracts.Api import Api
import requests
from tkinter import messagebox
class ClientService(Api):
    def list(self):
       try:
        response = requests.get(self.BASE_URL + "/client")
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showinfo("Erro!", error)

    
    def add(self, payload):
       try:
        response = requests.post(self.BASE_URL + "/client", json=payload)
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showinfo("Erro!", error)
       