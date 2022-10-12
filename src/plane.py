"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías utilizadas para el desarrollo de la clase Plane.
from intersect import Intersect
from vector import Vector

# Definición de la clase Plane.
class Plane(object):

  # Método constructor de la clase Plane.
  def __init__(self, center, width, length, material):
    self.center = center
    self.width = width
    self.length = length
    self.material = material

  # Método que calcula si un rayo atraviesa la esfera.
  def ray_interception(self, origin, direction):

    distance = (((self.center.y - origin.y)) / direction.y)
    hit_point = ((direction * distance) - origin)
    normal = Vector(0, -1, 0)

    if (
      (distance <= 0) or
      (hit_point.x > (self.center.x + (self.width / 2))) or (hit_point.x < (self.center.x - (self.width / 2))) or
      (hit_point.z > (self.center.z + (self.length / 2))) or (hit_point.z < (self.center.z - (self.length / 2)))
      ):
      return None

    # Retorno de la función.
    return Intersect(distance, hit_point, normal)

  # Representación textual de la esfera.
  def __repr__(self):
    return f"({self.y})"
