"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Definición de la clase Color.
class Color(object):

  # Método constructor de la clase Color.
  def __init__(self, r, g, b):
    self.r = min(255, max(r, 0))
    self.g = min(255, max(g, 0))
    self.b = min(255, max(b, 0))

  # Definición de multiplicación entre colores.
  def __mul__(self, other):

    # Valores actuales del objeto color.
    r, g, b = self.r, self.g, self.b

    # Los colores multiplicados por números aumentan o disminuyen en función del número.
    if ((type(other) == int) or (type(other) == float)):
      r *= other
      g *= other
      b *= other

    # Si el color se multiplica por otro, se multiplican sus tres valores.
    else:
      r *= other.r
      g *= other.g
      b *= other.b

    # Nuevos valores entre el rango [0 - 255].
    r = min(255, max(r, 0))
    g = min(255, max(g, 0))
    b = min(255, max(b, 0))

    # Retorno de un nuevo color.
    return Color(r, g, b)

  # Conversión del color a bytes.
  def to_bytes(self):
    return bytes([int(self.b), int(self.g), int(self.r)])

  # Representación del color como string o texto.
  def __repr__(self):
    return f"Color: {self.r}, {self.g}, {self.b}"
