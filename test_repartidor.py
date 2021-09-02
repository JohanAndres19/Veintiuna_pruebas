from veintiuna import *

repartidor = Repartidor()
jugador =Jugador()
# prueba para el inicio del juego con el repartidor
# resultado 2 cartas en la mano
def test_nueva_mano():
  repartidor.nueva_mano()
  assert len(repartidor.mano) == 2

def test_tiene_as_verdadero():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == True

def test_tiene_as_falso():
  repartidor.mano = [('5', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == False

def test_valor_carta_figura():
  carta = ('J', 'Picas')
  assert repartidor.valor_carta(carta) == 10

def test_valor_carta_numerica():
  carta = ('4', 'Picas')
  assert repartidor.valor_carta(carta) == 4

def test_valor_mano_veintiuna():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.sumar_mano() == 21

###################################

def test_jugada_repartidor_planto():
  repartidor.mano =[('A', 'Treboles'), ('J', 'Picas')]
  jugador.mano =[('A', 'Treboles'), ('8', 'Picas')]
  assert repartidor.jugar(repartidor.sumar_mano(),jugador.sumar_mano())=='planto'

def test_jugada_repartidor_juego():
  repartidor.mano =[('9', 'Treboles'), ('J', 'Treboles')]
  jugador.mano =[('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.jugar(repartidor.sumar_mano(),jugador.sumar_mano())=='juego'