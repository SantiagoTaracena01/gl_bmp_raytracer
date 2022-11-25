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

  # Método que calcula si un rayo atraviesa el plano.
  def ray_interception(self, origin, direction):

    # Distancia entre el rayo y el punto de intercepción.
    direction.y = 1E-06 if (direction.y == 0) else direction.y
    distance = (((self.center.y - origin.y)) / direction.y)
    hit_point = ((direction * distance) - origin)
    normal = Vector(0, -1, 0)

    # Condiciones en las que no hay una intercepción.
    neg_distance = (distance <= 0)
    too_left = (hit_point.x < (self.center.x - (self.width / 2)))
    too_right = (hit_point.x > (self.center.x + (self.width / 2)))
    too_close = (hit_point.z < (self.center.z - (self.length / 2)))
    too_far = (hit_point.z > (self.center.z + (self.length / 2)))

    # Retorno de None si alguna condición se cumple.
    if ((neg_distance) or (too_right) or (too_left) or (too_far) or (too_close)):
      return None

    # Retorno de un intercepto si este existe.
    return Intersect(distance, hit_point, normal)

  # Representación textual del plano.
  def __repr__(self):
    return f"({self.center}, {self.width}, {self.length})"
