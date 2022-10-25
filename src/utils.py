"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Módulos necesarios
from color import Color
from vector import Vector
import struct

# Constantes extra utilizadas.
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
ORANGE = Color(225, 135, 65)

# Funciones extra utilizadas.
color = lambda r, g, b: bytes([b, g, r])
char = lambda character: struct.pack("=c", character.encode("ascii"))
word = lambda word: struct.pack("=h", word)
dword = lambda dword: struct.pack("=l", dword)
reflect = lambda I, N: (I - N * 2 * (N @ I)).norm()
unpack = lambda buffer: struct.unpack("=l", buffer)[0]

# Función que refracta un rayo utilizando su normal.
def refract(I, N, roi):

  # Valores eta 1 y 2 iniciales.
  eta_i = 1
  eta_t = roi

  # Coseno i para calcular la refracción.
  cos_i = ((I @ N) * -1)

  # Recálculo de valores si el coseno i es negativo.
  if (cos_i < 0):
    cos_i *= -1
    eta_i *= -1
    eta_t *= -1
    N *= -1

  # Valor eta, resultante de la división de las dos componentes.
  eta = (eta_i / eta_t)

  # Simplificación de la expresión a un valor k para luego obtener su raíz cuadrada.
  k = (1 - ((eta ** 2) * (1 - (cos_i ** 2))))

  # Retorno de un vector nulo si el valor k es negativo.
  if (k < 0):
    return Vector(0, 0, 0)

  # Cálculo del coseno t con la raíz cuadrada del valor k.
  cos_t = (k ** 0.5)

  # Retorno del nuevo vector refractado.
  return ((I * eta) + (N * ((eta * cos_i) - cos_t))).norm()
