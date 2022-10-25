"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías y módulos necesarios para la clase Envmap.
import bmp
import math

# Definición de la clase Envmap.
class Envmap(object):

  # Método constructor de la clase Envmap.
  def __init__(self, path):
    self.path = path
    self.width, self.height, self.pixels = bmp.read_bmp(path)

  # Método para obtener el color de un pixel del Envmap.
  def get_color(self, direction):

    # Obtención de los valores de x e y para pintar.
    normalized_direction = direction.norm()
    x = round(((math.atan2(normalized_direction.z, normalized_direction.x) / (2 * math.pi)) + 0.5) * self.width)
    y = (-1 * round((math.acos((-1 * normalized_direction.y)) / math.pi) * self.height))

    # Arreglo de problemas con índices.
    x -= 1 if (x > 0) else 0
    y -= 1 if (y > 0) else 0

    # Retorno del color encontrado.
    return self.pixels[y][x]
