"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías utilizadas para el desarrollo de la clase Cube.
from intersect import Intersect

# Definición de la clase Cube.
class Cube(object):

  # Componentes de un vector a verificar en una intercepción.
  __COMPONENTS = 3

  # Método constructor de la clase Cube.
  def __init__(self, center, width, material):
    self.center = center
    self.width = width
    self.material = material

  # Método que detecta si un rayo interceptó con el cubo.
  def ray_interception(self, origin, direction):

    # Valores iniciales mínimos y máximos para la intercepción.
    min_t_value = -999_999
    max_t_value = 999_999

    # Verificación de máximos para todos los componentes del vector.
    for i in range(self.__COMPONENTS):

      # Cálculo de los valores mínimos y máximos del componente.
      if (direction.values[i] != 0):
        min_tc_value = (((self.center.values[i] - (self.width / 2)) - origin.values[i]) / direction.values[i])
        max_tc_value = (((self.center.values[i] + (self.width / 2)) - origin.values[i]) / direction.values[i])
      else:
        min_tc_value = -999_999
        max_tc_value = 999_999

      # Cambio de valores si el valor mínimo del componente es mayor al máximo.
      if (min_tc_value > max_tc_value):
        min_tc_value, max_tc_value = max_tc_value, min_tc_value

      # Cambio de los valores máximos del cuadrado si algún componente supera el máximo.
      min_t_value = min_tc_value if (min_tc_value > min_t_value) else min_t_value
      max_t_value = max_tc_value if (max_tc_value < max_t_value) else max_t_value

      # Si el valor mínimo fuera mayor al máximo, no hay intercepción.
      if (min_t_value > max_t_value):
        return None

    # Si el valor mínmo fuera menor a cero, debemos utilizar el máximo para comprobar la intercepción.
    if (min_t_value < 0):
      min_t_value = max_t_value

      # Si el valor máximo sigue siendo menor a cero, 
      if (min_t_value < 0):
        return None

    # Cálculo del impacto y la normal de la intercepción.
    hit_point = ((direction * min_t_value) - origin)
    normal = (hit_point - self.center).norm()

    # Retorno de la instancia de la intercepción.
    return Intersect(
      distance=min_t_value, 
      hit_point=hit_point, 
      normal=normal,
    )
