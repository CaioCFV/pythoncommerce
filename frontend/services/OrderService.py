from abstracts.Api import Api
import requests
from tkinter import messagebox

class OrderService(Api):
    def createOrder(self, payload):
       try:
        response = requests.post(self.BASE_URL + "/order", json=payload)
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showinfo("Erro!", error)
       