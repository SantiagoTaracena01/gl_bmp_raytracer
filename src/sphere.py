"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías utilizadas para el desarrollo de la clase Sphere.
from intersect import Intersect

# Definición de la clase Sphere.
class Sphere(object):

  # Método constructor de la clase Sphere. AGREGAR material
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius
    # self.material = material

  # Método que calcula si un rayo atraviesa la esfera.
  def ray_interception(self, origin, direction):

    # Vectores y datos necesarios para la realización del cálculo.
    L = self.center - origin
    tca = L @ direction
    l = L.length()
    d2 = ((l ** 2) - (tca ** 2))
    squared_radius = (self.radius ** 2)

    # Si d2 es mayor que el radio al cuadrado, el rayo definitivamente no pasa por la esfera.
    if (d2 > squared_radius):
      # return None
      return False

    # Datos extra necesarios para la corroboración.
    thc = ((squared_radius - d2) ** 0.5)
    t0 = (tca - thc)
    t1 = (tca + thc)

    # if (t0 < 0):
    #   t0 = t1
    # if (t0 < 0):
    #   return None

    # hit_point = ((direction * t0) + origin)
    # normal = (hit_point - self.center).norm()

    # Cambio de la variable t0 si es menor a cero.
    t0 = t1 if (t0 < 0) else t0

    # return None
    # return Intersect(distance=t0)

    # return Intersect(t0, hit_point, normal)

    # Retorno del resultado definitivo de la intercepción.
    return (t0 > 0)

  # Representación textual de la esfera.
  def __repr__(self):
    return f"({self.center}, {self.radius})"
