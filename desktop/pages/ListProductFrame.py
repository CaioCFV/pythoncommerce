from styleguide.component import Heading1, Gap1
from abstracts.Screen import Screen
import tkinter as tk
from tkinter import ttk
from services.ProductService import ProductService

class ListProductFrame(Screen):
    def setup(self):
        title = Heading1(self.frame, "PRODUTOS")
        title.setGrid(row=1,  column=1, sticky="w", padx=0, pady=0)

        gap = Gap1(self.frame)
        gap.setGrid(row=2, column=1)

        tabelaframe = tk.Frame()
        tabela = ttk.Treeview(self.frame, columns=("id", "cpf", "name"), show="headings", height=10)
        tabela.grid(row=8, column=1, sticky="nsew")
        tabela.heading("id", text="ID")
        tabela.heading("cpf", text="Nome")
        tabela.heading("name", text="Email")

        tabela.column("id", width=80, anchor="center")
        tabela.column("cpf", width=280, anchor="center")
        tabela.column("name", width=280, anchor="center")

        tabela.tag_configure("linha1", background="#E0E0E0")
        tabela.tag_configure("linha2", background="#FFFFFF") 

        clientes = ProductService().list()

        for i, cliente in enumerate(clientes):
            tag = "linha1" if i % 2 == 0 else "linha2"
            tabela.insert("", "end", values=(cliente['id'], cliente['name'], cliente['description']), tags=(tag,))

    def open(self):
       self.frame.tkraise()