from abc import ABC, abstractmethod
import tkinter as tk
from styleguide.style import style

class Component(ABC):
    def __init__(self, root):
        self.frame = tk.Frame(root, width=700, height=500, bg="#fff", padx=20, pady=20) 
        self.frame.place(x=0, y=0, width=700, height=500)
        self.root = root
        self.setup()

    def setGrid(self, **grid):
        self.element.grid(**grid)

class ButtonPrimary(Component):
    def __init__(self, frame, name):
        self.element = tk.Button(frame, text=name, **style['btn_primary'])
    
    def event(self, command):
        self.element.bind("<Button-1>", command)

class Heading1(Component):
    def __init__(self, frame, name):
        self.element = tk.Label(frame, text=name, **style['title'])

class Label(Component):
    def __init__(self, frame, name):
        self.element = tk.Label(frame, text=name, **style['label'])

class Gap1(Component):
    def __init__(self, frame):
        self.element = tk.Frame(frame, height=20)

class Gap2(Component):
    def __init__(self, frame):
        self.element = tk.Frame(frame, height=40)

class Input(Component):
    def __init__(self, frame):
        self.element = tk.Text(frame, **style['input'])
    
    def value(self):
        return self.element.get("1.0", "end-1c")

class InputMedium(Component):
    def __init__(self, frame):
        self.element = tk.Text(frame, **style['input_medium'])
    
    def value(self):
        return self.element.get("1.0", "end-1c")

class Textarea(Component):
    def __init__(self, frame):
        self.element = tk.Text(frame, **style['textarea'])

    def value(self):
        return self.element.get("1.0", "end-1c")