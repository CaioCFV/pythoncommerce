from styleguide.component import Heading1, Gap1, Gap2,  Label, ButtonPrimary, InputMedium
from abstracts.Screen import Screen
from services.VariantService  import VariantService
from tkinter import messagebox
class FormVariantFrame(Screen):
    
    def setup(self):
        Heading1(self.frame, "CADASTRAR VARIANTES").setGrid(row=1,  column=1, sticky="w", padx=0, pady=0)

        Gap1(self.frame).setGrid(row=2, column=1)

        Label(self.frame, "Nome:").setGrid(row=3,  column=1, sticky="w", padx=0, pady=0)
        
        self.name = InputMedium(self.frame)
        self.name.setGrid(row=4, column=1, sticky="w")

        Gap1(self.frame).setGrid(row=5, column=1)

        Label(self.frame, "Código ean:").setGrid(row=6,  column=1, sticky="w", padx=0, pady=0)

        self.ean = InputMedium(self.frame)
        self.ean.setGrid(row=7, column=1, sticky="w")

        Gap1(self.frame).setGrid(row=8, column=1)

        Label(self.frame, "QTD. Estoque:").setGrid(row=9,  column=1, sticky="w", padx=0, pady=0)

        self.quantity = InputMedium(self.frame)
        self.quantity.setGrid(row=10, column=1,  sticky="w")

        Label(self.frame, "Preço").setGrid(row=3,  column=2, sticky="w", padx=40, pady=0)

        self.price = InputMedium(self.frame)
        self.price.setGrid(row=4, column=2, sticky="w", padx=40)

        Gap1(self.frame).setGrid(row=5, column=2)

        Label(self.frame, "ID do produto:").setGrid(row=6,  column=2, sticky="w", padx=40, pady=0)

        self.product_id = InputMedium(self.frame)
        self.product_id.setGrid(row=7, column=2, sticky="w", padx=40)

        Gap2(self.frame).setGrid(row=11, column=1)

        btn = ButtonPrimary(self.frame, "CADASTRAR")
        btn.setGrid(row=12, column=1, padx=0, pady=0, sticky="w")
        btn.event(self.send)

    def open(self):
       self.setup()
       self.frame.tkraise()

    def send(self, *args):  
        service = VariantService()

        response = service.add({
            'name': self.name.value(),
            'ean': int(self.ean.value() or 0),
            'quantity': int(self.quantity.value() or 0),
            'price': int(self.price.value() or 0),
            'product_id': int(self.product_id.value() or -1)
        })

        error = next(iter(response.values()))
        
        if not isinstance(error, (int, float)) and len(error):
            return messagebox.showwarning('Campos inválidos', error['error'])

        mensagem = f"Variante cadastrada com sucesso!\n\nNome: {response['name']}\nEAN: {response['ean']}\nPreço: {response['price']}\nEstoque: {response['quantity']}"
        messagebox.showinfo("Sucesso!", mensagem)