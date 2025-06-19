import argparse
import tkinter as tk
from tkinter import font
from pages.FormClientFrame import FormClientFrame
from pages.FormProductFrame import FormProductFrame
from pages.FormVariantFrame import FormVariantFrame
from pages.ListClientFrame import ListClientFrame
from pages.ListProductFrame import ListProductFrame
from pages.ListVariantFrame import ListVariantFrame

import tkhotreload as tkhr


class MainScreen: 
    def __init__(self, root):
        root.iconbitmap("./assets/iconedeumcarrinho.ico") 
        # root.properties and root.properties(title="Loja dos Veneno")
        root.configure(bg="#fff") 
        self.root = root
        self.__center()
        
    def __center(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2

        self.root.geometry(f"{700}x{500}+{x}+{y}")
    
    def getRoot(self):
        return self.root
    
    def addFrame(self, frame):
        return
    
    def start():
        return

def app(*debugroot):
    root = tk.Tk()

    if debugroot:
       root = debugroot[0] 

    main = MainScreen(root)
    appRoot = main.getRoot()
    
    fonte_personalizada = font.Font(family="Verdana", size=12)

    appRoot.option_add("*Font", fonte_personalizada)

    # FRAMEZIN
    frm_client         = FormClientFrame(appRoot)
    frm_product        = FormProductFrame(appRoot)
    frm_variant        = FormVariantFrame(appRoot)
    frm_client_view    = ListClientFrame(appRoot)
    frm_client_view    = ListProductFrame(appRoot)
    frm_client_view    = ListVariantFrame(appRoot)

    # frm_order   = OrderFrame(appRoot)
    # frm_about   = AboutFrame(appRoot)

    # MENUZIN
    menubar = tk.Menu(appRoot)
    client = menubar.add_command(label="Clientes", command=lambda: frm_client.open())
    client = menubar.add_command(label="Produtos", command=lambda: frm_product.open())
    client = menubar.add_command(label="Produtos", command=lambda: frm_variant.open())

    submenu_clientes = tk.Menu(menubar, tearoff=0)
    submenu_clientes.add_command(label="Novo Cliente", command=lambda: print("Novo Cliente"))
    submenu_clientes.add_command(label="Listar Clientes", command=lambda: print("Listar Clientes"))
    submenu_clientes.add_separator()

    # menubar.add_cascade(label="Clientes", menu=submenu_clientes)
    # menubar.add_command(label="Produtos", command=lambda: frm_product.open())
    # menubar.add_command(label="Pedidos",  command=lambda: frm_order.open())
    # menubar.add_command(label="Sobre",    command=lambda: frm_about.open())

    appRoot.config(menu=menubar) 

    if not debugroot: 
        appRoot.mainloop() 


# Inicia o Hot Reload
#tkhr.app(target=main, watch_dir=".")


def main(debug=False):
    if debug:
        print("Modo DEBUG ativado!")
        tkhr.app(target=app, watch_dir=".")
    else:
        app()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Executar o aplicativo.")
    parser.add_argument("--debug", action="store_true", help="Ativar modo debug")
    args = parser.parse_args()
    main(debug=args.debug)
