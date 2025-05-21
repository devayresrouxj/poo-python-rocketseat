# Exemplo de herança
print("\nExemplo de herança:")

from abc import abstractmethod
from typing import override

class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome
  
  def andar(self):
    print(f"O animal {self.nome} andou")

  @abstractmethod
  def emitir_som(self) -> str:
    pass

class Cachorro(Animal):
  @override
  def emitir_som(self) -> str:
    return "Au, au"
  
class Gato(Animal):
  def emitir_som(self) -> str:
    return "Miau!"