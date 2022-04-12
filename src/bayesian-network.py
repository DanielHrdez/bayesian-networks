"""
Universidad de La Laguna
Escuela Superior de Ingeniería y Tecnología
Grado en Ingeniería Informática
Asignatura: Inteligencia Artificial Avanzada
Programa para el uso de redes bayesianas.
Authores:
  - Daniel Hernández de Elón
  - Adrián Fleitas de la Rosa
"""

import pysmile_license
import pysmile

HEARD_NEAR = "HN"
HEALTH = "Health"
WEAPON = "Weapon"
PROXIMITY_HEALTH = "proximity_health"
PROXIMITY_WEAPON = "proximity_weapon"
NUMBER_ENEMIES = "Number_enemies"
OPONENT_WEAPON = "Oponent_weapon"
ST = "st"
ST_1 = "st_1"

ARGUMENT_LIST = [
  ST,
  HEALTH,
  WEAPON,
  OPONENT_WEAPON,
  HEARD_NEAR,
  NUMBER_ENEMIES,
  PROXIMITY_WEAPON,
  PROXIMITY_HEALTH,
]

net = pysmile.Network()
net.read_file('../model/seminario.xdsl')
net.update_beliefs()

def calculate_next_value(values):
  for i in range(len(values)):
    net.set_evidence(ARGUMENT_LIST[i], values[i])
  net.update_beliefs()
  beliefs = net.get_node_value(ST_1)
  max_value = 0
  max_belief = ''
  for i in range(len(beliefs)):
    if (beliefs[i] > max_value):
      max_value = beliefs[i]
      max_belief = net.get_outcome_id(ST_1, i)
  
  return max_belief

if __name__ == '__main__':
  introduce = 'Introduce el valor para '
  St = input(f'{introduce} el State: [Attack | grab_weapon | grab_energy | explore | run_away | detect_danger]\n')
  H = input(f'{introduce} Health: [high | low]\n')
  W = input(f'{introduce} Weapon: [armed | disarmed]\n')
  OW = input(f'{introduce} Oponent Weapon: [armed | disarmed]\n')
  HN = input(f'{introduce} Hear Near: [yes | no]\n')
  NE = input(f'{introduce} Near Enemies: [yes | no]\n')
  PW = input(f'{introduce} Proximity Weapon: [yes | no]\n')
  PH = input(f'{introduce} Proximity Health: [yes | no]\n')
  St_next = calculate_next_value([St, H, W, OW, HN, NE, PW, PH])
  print(f'El valor para St_next es: {St_next}')
  