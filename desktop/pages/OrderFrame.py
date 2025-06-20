from styleguide.component import Heading1, Gap1
from abstracts.Screen import Screen
from services.ClientService import ClientService
from tkinter import messagebox
from tkinter import ttk
from services.ProductService import ProductService
from services.ClientService import ClientService
from services.VariantService import VariantService
from services.OrderService import OrderService

def formatar_para_reais(valor_em_centavos: int) -> str:
    valor_em_reais = valor_em_centavos / 100
    return f"R$ {valor_em_reais:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_cpf(cpf_str):
    # Remove tudo que não for número
    numeros = ''.join(filter(str.isdigit, cpf_str))
    if len(numeros) != 11:
        # raise ValueError("CPF deve ter 11 dígitos.")
        return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
    
class OrderFrame(Screen):
    def setup(self):
        Heading1(self.frame, "FAZER PEDIDO").setGrid(row=1,  column=1, sticky="w", padx=0, pady=0)
        Gap1(self.frame).setGrid(row=2, column=1)

        self.renderProductTable()


    def renderProductTable(self):
        table_products = ttk.Treeview(self.frame, columns=("id", "name", "description"), show="headings", height=3)
       
        table_products.grid(row=3, column=1, sticky="nsew")
        table_products.heading("id", text="ID")
        table_products.heading("name", text="Nome")
        table_products.heading("description", text="Descrição")

        table_products.column("id", width=40, anchor="center")
        table_products.column("name", width=220)
        table_products.column("description", width=400)

        table_products.tag_configure("linha1", background="#E0E0E0")
        table_products.tag_configure("linha2", background="#FFFFFF")

        self.products = ProductService().list()

        for i, product in enumerate(self.products):
            tag = "linha1" if i % 2 == 0 else "linha2"
            table_products.insert("", "end", values=(product['id'], "  "+product['name'], "  "+product['description']), tags=(tag,))

        table_products.bind("<<TreeviewSelect>>", self.renderVariantTable)

    def renderClients(self, event):
        tree = event.widget
        selected_item = tree.focus()
        item_values = tree.item(selected_item, 'values')
        self.variant_id = item_values[0]

        Gap1(self.frame).setGrid(row=9, column=1)
        Heading1(self.frame, "Vender para qual cliente ?").setGrid(row=10, column=1, sticky="w", padx=0, pady=0)
        Gap1(self.frame).setGrid(row=11, column=1)


        table_clients = ttk.Treeview(self.frame, columns=("id", "name",  "cpf"), show="headings", height=3)
       
        table_clients.grid(row=12, column=1, sticky="nsew")
        table_clients.heading("id", text="ID")
        table_clients.heading("name", text="Nome")
        table_clients.heading("cpf", text="Preço")

        table_clients.column("id", width=40, anchor="center")
        table_clients.column("name", width=100)
        table_clients.column("cpf", width=100)

        table_clients.tag_configure("linha1", background="#E0E0E0")
        table_clients.tag_configure("linha2", background="#FFFFFF")

        clients = ClientService().list()

        for i, variant in enumerate(clients):
            tag = "linha1" if i % 2 == 0 else "linha2"
            table_clients.insert("", "end", values=(variant['id'], variant['name'], formatar_cpf(variant['cpf'])), tags=(tag,))

        table_clients.bind("<<TreeviewSelect>>", self.send)

    def renderVariantTable(self, event):
        tree = event.widget
        selected_item = tree.focus()
        item_values = tree.item(selected_item, 'values')
        self.product_id = item_values[0]
        
        Gap1(self.frame).setGrid(row=4, column=1)
        Heading1(self.frame, "Selecione uma variante").setGrid(row=5, column=1, sticky="w", padx=0, pady=0)
        Gap1(self.frame).setGrid(row=6, column=1)


        table_variants = ttk.Treeview(self.frame, columns=("id", "name", "price", "quantity"), show="headings", height=3)
       
        table_variants.grid(row=7, column=1, sticky="nsew")
        table_variants.heading("id", text="ID")
        table_variants.heading("name", text="Nome")

        table_variants.column("id", width=40, anchor="center")
        table_variants.column("name", width=100)
        table_variants.column("price", width=100)
        table_variants.column("quantity", width=100)

        table_variants.tag_configure("linha1", background="#E0E0E0")
        table_variants.tag_configure("linha2", background="#FFFFFF")

        variants = VariantService().getVariantsByProductId(self.product_id)

        for i, variant in enumerate(variants):
            tag = "linha1" if i % 2 == 0 else "linha2"
            table_variants.insert("", "end", values=(variant['id'], variant['name'], formatar_para_reais(variant['price']), str(variant['quantity'])), tags=(tag,))

        table_variants.bind("<<TreeviewSelect>>", self.renderClients)

    def open(self):
       self.frame.tkraise()

    def send(self, event):  
        tree = event.widget
        selected_item = tree.focus()
        item_values = tree.item(selected_item, 'values')
        self.client_id = item_values[0]
        service = OrderService()

        response = service.createOrder({
            'client_id': self.client_id,
            'variants': [self.variant_id]
        })

        print(response)
        error = next(iter(response.values()))

        if not isinstance(error, (int, float)) and len(error):
            return messagebox.showwarning('Campos inválidos', error['error'])

        mensagem = f"Pedido cadastrado com sucesso!\n\nID DO PEDIDO: {response['order_id']}\nTotal: {formatar_para_reais(response['total'])}\nData do pedido: {response['date']}"
        messagebox.showinfo("Sucesso!", mensagem)