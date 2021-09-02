from random import choice
_valores = [str(v) for v in range(2, 11)] + ['A', 'J', 'Q', 'K']
_pintas = ['Corazones', 'Diamantes', 'Treboles', 'Picas']
_cartas = [(v, p) for v in _valores for p in _pintas]

class Juego:  
  def nueva_mano(self):
    self.mano = [choice(_cartas), choice(_cartas)]

  def tiene_as(self):
    for c in self.mano:
      if c[0] == 'A':
        return True
    return False

  def sumar_mano(self):
    valor = 0
    for c in self.mano:
      valor += self.valor_carta(c)
    if self.tiene_as() and valor <= 11:
      valor += 10 
    return valor

  def valor_carta(self, carta):
    if carta[0] in ['J', 'Q', 'K']:
      return 10
    elif carta[0] == 'A':
      return 1
    else:
      return int(carta[0])

  def jugar(self):
    pass    

class Repartidor(Juego):
  def __init__(self):
    self.mano = []

  def jugar(self,valor_mano,valor_jugador):
    if (valor_mano<=16 or (valor_mano-valor_jugador)<0 )and valor_jugador<=21 and valor_jugador!=valor_mano:
      return "juego"
    else:
      return "planto"

class Jugador(Juego) :
  def __init__(self):
    self.mano = []