from styleguide.component import Heading1, Gap1
from abstracts.Screen import Screen
import tkinter as tk
from tkinter import ttk
from services.VariantService import VariantService

class ListVariantFrame(Screen):
    def setup(self):
        title = Heading1(self.frame, "VARIANTES")
        title.setGrid(row=1,  column=1, sticky="w", padx=0, pady=0)

        gap = Gap1(self.frame)
        gap.setGrid(row=2, column=1)

        tabela = ttk.Treeview(self.frame, columns=("id", "name", "ean", "quantity", 'price', 'product'), show="headings", height=10)
        tabela.grid(row=8, column=1, sticky="nsew")
        tabela.heading("id", text="ID")
        tabela.heading("name", text="Nome")
        tabela.heading("ean", text="EAN")
        tabela.heading("quantity", text="Estoque")
        tabela.heading("price", text="Preço")
        tabela.heading("product", text="ID do produto")

        tabela.column("id", width=80, anchor="center")
        tabela.column("name", width=115, anchor="center")
        tabela.column("ean", width=115, anchor="center")
        tabela.column("quantity", width=115, anchor="center")
        tabela.column("price", width=115, anchor="center")
        tabela.column("product", width=115, anchor="center")

        tabela.tag_configure("linha1", background="#E0E0E0")
        tabela.tag_configure("linha2", background="#FFFFFF") 

        variant = VariantService().list()

        for i, variant in enumerate(variant):
            tag = "linha1" if i % 2 == 0 else "linha2"
            tabela.insert("", "end", values=(variant['id'], variant['name'], variant['ean'], variant['quantity'], variant['price'], variant['product_id']), tags=(tag,))

    def open(self):
       self.frame.tkraise()
