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
  
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")
animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} faz {animal.emitir_som()}")

print("\nExemplo de encapsulamento")

class ContaBancaria:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo # Atributo privado
  
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
    
  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultar_saldo(self):
    return self.__saldo
  
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
