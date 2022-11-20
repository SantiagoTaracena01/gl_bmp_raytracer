"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías utilizadas para el desarrollo de la clase Sphere.
from intersect import Intersect
from vector import Vector

# Definición de la clase Cube.
class Cube(object):

  # Método constructor de la clase Cube.
  def __init__(self, center, width, material):
    self.center = center
    self.width = width
    self.material = material

  def ray_interception(self, origin, direction):
    tmin = -999_999
    tmax = 999_999

    txmin = ((self.center.x - (self.width*0.5)) - origin.x) / direction.x
    txmax = ((self.center.x + (self.width*0.5)) - origin.x) / direction.x

    if txmin > txmax:
      txmin, txmax = txmax, txmin

    if txmin > tmin:
      tmin = txmin

    if txmax < tmax:
      tmax = txmax

    if tmin > tmax:
      return False

    tymin = ((self.center.y - (self.width*0.5)) - origin.y) / direction.y
    tymax = ((self.center.y + (self.width*0.5)) - origin.y) / direction.y

    if tymin > tymax:
      tymin, tymax = tymax, tymin

    if tymin > tmin:
      tmin = tymin

    if tymax < tmax:
      tmax = tymax

    if tmin > tmax:
      return False

    tzmin = ((self.center.z - (self.width*0.5)) - origin.z) / direction.z
    tzmax = ((self.center.z + (self.width*0.5)) - origin.z) / direction.z

    if tzmin > tzmax:
      tzmin, tzmax = tzmax, tzmin

    if tzmin > tmin:
      tmin = tzmin

    if tzmax < tmax:
      tmax = tzmax

    if tmin > tmax:
      return False

    if tmin < 0:
      tmin = tmax

      if tmin < 0:
        return False

    impact = (direction * tmin) - origin
    normal = (impact - self.center).norm()

    return Intersect(
      distance = tmin, 
      hit_point = impact, 
      normal = normal,
    )
