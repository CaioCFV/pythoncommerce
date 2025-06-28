from styleguide.component import Heading1, Gap1
from abstracts.Screen import Screen
import tkinter as tk
from tkinter import ttk
from services.ClientService import ClientService



def formatar_cpf(cpf_str):
    # Remove tudo que não for número
    numeros = ''.join(filter(str.isdigit, cpf_str))
    if len(numeros) != 11:
        # raise ValueError("CPF deve ter 11 dígitos.")
        return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"

class ListClientFrame(Screen):
    def setup(self):
        title = Heading1(self.frame, "CLIENTES")
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

        clientes = ClientService().list()

        for i, cliente in enumerate(clientes):
            tag = "linha1" if i % 2 == 0 else "linha2"
            tabela.insert("", "end", values=(cliente['id'], cliente['name'], formatar_cpf(cliente['cpf'])), tags=(tag,))

    def open(self):
       self.frame.tkraise()
