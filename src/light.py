"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

from vector import Vector

class Light(object):
  def __init__(self, position=Vector(0, 0, 0), intensity=1):
    self.position = position
    self.intensity = intensity