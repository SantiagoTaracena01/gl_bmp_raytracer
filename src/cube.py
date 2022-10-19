"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías utilizadas para el desarrollo de la clase Sphere.
from intersect import Intersect

class Cube(object):

  def __init__(self, center, radius, material):
    self.center = center
    self.radius = radius
    self.material = material

  def ray_interception(self, origin, direction):
    ...
