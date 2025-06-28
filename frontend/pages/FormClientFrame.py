from styleguide.component import Heading1, Gap1, Gap2,  Label, Input, ButtonPrimary
from abstracts.Screen import Screen
from services.ClientService import ClientService
from tkinter import messagebox

class FormClientFrame(Screen):
    def setup(self):
        Heading1(self.frame, "CADASTRAR CLIENTE").setGrid(row=1,  column=1, sticky="w", padx=0, pady=0)

        Gap1(self.frame).setGrid(row=2, column=1)

        Label(self.frame, "Nome:").setGrid(row=3,  column=1, sticky="w", padx=0, pady=0)
        
        self.name = Input(self.frame)
        self.name.setGrid(row=4, column=1)

        Gap1(self.frame).setGrid(row=5, column=1)

        Label(self.frame, "CPF:").setGrid(row=6,  column=1, sticky="w", padx=0, pady=0)

        self.cpf = Input(self.frame)
        self.cpf.setGrid(row=7, column=1)

        Gap2(self.frame).setGrid(row=8, column=1)

        btn = ButtonPrimary(self.frame, "CADASTRAR")
        btn.setGrid(row=9, column=1, padx=0, pady=0, sticky="w")
        btn.event(self.send)

    def open(self):
       self.setup()
       self.frame.tkraise()

    def send(self, *args):  
        service = ClientService()

        response = service.add({
            'name': self.name.value(),
            'cpf': self.cpf.value()
        })

        error = next(iter(response.values()))

        if not isinstance(error, (int, float)) and len(error):
            return messagebox.showwarning('Campos inválidos', error['error'])

        mensagem = f"Cliente cadastrado com sucesso!\n\nNome: {response['name']}\nCPF: {response['cpf']}"
        messagebox.showinfo("Sucesso!", mensagem)