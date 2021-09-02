Feature: El repartidor del juego de 21

Scenario: Repartir dos cartas
  Given un repartidor
  When el juego inicia
  Then el repartidor toma dos cartas

Scenario Outline: Conocer el valor de la mano
  Given una <mano>
  When el repartidor sume las cartas
  Then el <valor> es correcto

  Examples: manos y total
  | mano         | valor |
  | 5,7          | 12    |
  | A,10,5       | 16    |
  | J,K          | 20    |
  | A,A,3        | 15    |
  | J,K,8        | 28    | 

Scenario Outline: El repartidor juega de acuerdo a las reglas
  Given los totales de las manos del <repartidor> y <jugador> 
  When el repartidor determina la jugada
  Then la <jugada> es correcta

  Examples: valores y jugada
  | repartidor | jugador | jugada   |
  | 10         | 10      | planto   |
  | 10         | 21      | juego    |
  | 21         | 18      | planto   | 
  | 5          | 10      | juego    |
  | 8          | 25      | planto   |
  | 19         | 21      | juego    |

