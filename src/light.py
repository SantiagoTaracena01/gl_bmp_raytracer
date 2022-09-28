"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de la clase Light.
from vector import Vector

# Definición de la clase Light.
class Light(object):

  # Método constructor de la clase Light.
  def __init__(self, position=Vector(0, 0, 0), intensity=1):
    self.position = position
    self.intensity = intensity
