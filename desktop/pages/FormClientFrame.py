from styleguide.component import Heading1, Gap1, Gap2,  Label, Input, ButtonPrimary
from abstracts.Screen import Screen
import tkinter as tk

class FormClientFrame(Screen):
    def setup(self):
        title = Heading1(self.frame, "CADASTRAR CLIENTE")
        title.setGrid(row=1,  column=1, sticky="w", padx=0, pady=0)

        gap = Gap1(self.frame)
        gap.setGrid(row=2, column=1)

        label = Label(self.frame, "Nome:")
        label.setGrid(row=3,  column=1, sticky="w", padx=0, pady=0)
        
        input = Input(self.frame)
        input.setGrid(row=4, column=1)

        gap = Gap1(self.frame)
        gap.setGrid(row=5, column=1)

        label = Label(self.frame, "CPF:")
        label.setGrid(row=6,  column=1, sticky="w", padx=0, pady=0)

        input = Input(self.frame)
        input.setGrid(row=7, column=1)

        gap = Gap2(self.frame)
        gap.setGrid(row=8, column=1)

        btn = ButtonPrimary(self.frame, "CADASTRAR")
        btn.setGrid(row=9, column=1, padx=0, pady=0, sticky="w")

    def open(self):
       self.frame.tkraise()


 #self.frame.grid_rowconfigure(0, weight=1)
        #self.frame.grid_columnconfigure(0, weight=1)

        #label = tk.Label(self.frame, text="CPF:", fg="blue", anchor="w", bg="SystemButtonFace")
        #label.grid(row=5,  column=1, sticky="w", padx=0, pady=0)

        #input = tk.Text(self.frame, width=50, height=1.5)
        #input.grid(row=6, column=1, padx=0, pady=10)



        # tabelaframe = tk.Frame()
        # tabela = ttk.Treeview(self.frame, columns=("ID", "Nome", "Email"), show="headings", height=3)
        # tabela.grid(row=8, column=1, sticky="nsew")
        # tabela.heading("ID", text="ID")
        # tabela.heading("Nome", text="Nome")
        # tabela.heading("Email", text="Email")

        # tabela.column("ID", width=50)
        # tabela.column("Nome", width=150)
        # tabela.column("Email", width=200)

        # tabela.tag_configure("linha1", background="#E0E0E0")
        # tabela.tag_configure("linha2", background="#FFFFFF") 

        #scroll_y = ttk.Scrollbar(self.frame, orient="vertical", command=tabela.yview)
        #tabela.configure(yscrollcommand=scroll_y.set)

        #scroll_y.grid(row=0, column=1, sticky="ns")

        # scroll_y.pack(side="right", fill="y")

        # clientes = [
        #     (1, "Caio Silva", "caio@email.com"),
        #     (2, "Maria Souza", "maria@email.com"),
        #     (3, "João Pereira", "joao@email.com"),
        #     (1, "Caio Silva", "caio@email.com"),
        #     (2, "Maria Souza", "maria@email.com"),
        #     (3, "João Pereira", "joao@email.com"),
        # ]

        # for i, cliente in enumerate(clientes):
        #     tag = "linha1" if i % 2 == 0 else "linha2"
        #     tabela.insert("", "end", values=cliente, tags=(tag,))

        # tabela.grid(row=8)