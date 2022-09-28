"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Definición de la clase Intersect.
class Intersect(object):

  # Método constructor de la clase Intersect.
  def __init__(self, distance, hit_point, normal):
    self.distance = distance
    self.hit_point = hit_point
    self.normal = normal
