from behave import *
from veintiuna import *

##################################3333
@given('un repartidor')
def step_imp(context):
  context.repartidor = Repartidor()

@when('el juego inicia')
def step_imp(context):
  context.repartidor.nueva_mano()

@then('el repartidor toma dos cartas')
def step_imp(context):
  assert len(context.repartidor.mano) == 2

################################33
@given('una {mano}')
def step_imp(context, mano):
  context.repartidor = Repartidor()
  context.repartidor.mano = [(x, 'Diamantes') for x in mano.split(',')]

@when('el repartidor sume las cartas')
def step_imp(context):
  context.valor_mano = context.repartidor.sumar_mano()

@then('el {valor:d} es correcto')
def step_imp(context, valor):
  assert context.valor_mano == valor

##############################################

@given('los totales de las manos del {repartidor:d} y {jugador:d}')
def step_imp(context,repartidor,jugador):
  context.repartidor=Repartidor()
  context.valor_repartidor=repartidor
  context.valor_jugador = jugador

@when('el repartidor determina la jugada')
def setp_imp(context):
  context.jugada_v = context.repartidor.jugar(context.valor_repartidor,context.valor_jugador)

@then('la {jugada} es correcta')
def setp_imp(context,jugada):
  assert context.jugada_v==jugada

