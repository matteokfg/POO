from abc import ABC, abstractmethod

class Compra(ABC):
    @abstractmethod
    def validate_codigo(self):
        pass

    @abstractmethod
    def validate_lista_inteiros(self):
        pass