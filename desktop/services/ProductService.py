from abstracts.Api import Api
import requests
from tkinter import messagebox
class ProductService(Api):
    def list(self):
       try:
        response = requests.get(self.BASE_URL + "/product")
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showerror("Erro!", error)
       
    def add(self, payload):
       try:
        response = requests.post(self.BASE_URL + "/product", json=payload)
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showerror("Erro!", error)