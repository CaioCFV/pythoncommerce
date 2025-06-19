from abc import ABC, abstractmethod

class Api(ABC):
    def __init__(self):
        self.BASE_URL = 'http://127.0.0.1:5000/api'
