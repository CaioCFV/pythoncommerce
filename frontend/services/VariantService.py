from abstracts.Api import Api
import requests
from tkinter import messagebox
class VariantService(Api):
    def list(self):
       try:
        response = requests.get(self.BASE_URL + "/variant")
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showinfo("Erro!", error)
    
    def add(self, payload):
       try:
        response = requests.post(self.BASE_URL + "/variant", json=payload)
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showinfo("Erro!", error)
    
    def getVariantsByProductId(self, product_id):
       try:
        response = requests.get(self.BASE_URL + "/variant_by_product/"+product_id)
        return response.json()
       
       except requests.exceptions as error: 
           messagebox.showinfo("Erro!", error)
       