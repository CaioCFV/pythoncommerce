from abc import ABC, abstractmethod
import tkinter as tk

class Screen(ABC):
    def __init__(self, root):
        self.frame = tk.Frame(root, width=700, height=500, bg="#fff", padx=20, pady=20) 
        self.frame.place(x=0, y=0, width=700, height=500)
        self.root = root
        self.setup()

    @abstractmethod
    def setup(self):
        pass

    def open(self):
        pass