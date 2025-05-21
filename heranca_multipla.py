from abc import abstractmethod

class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  @abstractmethod
  def emitir_som(self) -> str:
    pass

class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está amamentando."
  
class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando."
  
class Morcego(Mamifero, Ave):
  def emitir_som(self):
    return "Morcegos emitem sons ultrassônicos"

morcego = Morcego(nome="Batman")

# Acessando métodos da classe base 'Animal'
print(f"Nome do morcego: {morcego.nome}")
print(f"Som do morcego: {morcego.emitir_som()}")

# Acessando métodos das classes Mamifero e Ave
print(morcego.amamentar())
print(morcego.voar())