from styleguide.component import Heading1, Gap1
from abstracts.Screen import Screen
import tkinter as tk
from tkinter import ttk
from services.VariantService import VariantService

class ListVariantFrame(Screen):
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

        clientes = VariantService().list()

        for i, cliente in enumerate(clientes):
            tag = "linha1" if i % 2 == 0 else "linha2"
            tabela.insert("", "end", values=(cliente['id'], cliente['name'], cliente['ean']), tags=(tag,))

        self.show()

    def open(self):
       self.frame.tkraise()


    def show(self):
        pass
        #self.frame.grid_rowconfigure(0, weight=1)
        #self.frame.grid_columnconfigure(0, weight=1)

        #label = tk.Label(self.frame, text="CPF:", fg="blue", anchor="w", bg="SystemButtonFace")
        #label.grid(row=5,  column=1, sticky="w", padx=0, pady=0)

        #input = tk.Text(self.frame, width=50, height=1.5)
        #input.grid(row=6, column=1, padx=0, pady=10)




        #scroll_y = ttk.Scrollbar(self.frame, orient="vertical", command=tabela.yview)
        #tabela.configure(yscrollcommand=scroll_y.set)

        #scroll_y.grid(row=0, column=1, sticky="ns")

        # scroll_y.pack(side="right", fill="y")





        # tabela.grid(row=8)