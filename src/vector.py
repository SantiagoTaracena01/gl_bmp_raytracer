"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Definición de la clase Vector.
class Vector(object):

  # Método constructor de la clase Vector.
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.values = (x, y, z)

  # Sobreescritura de la suma de vectores.
  def __add__(self, other):
    return Vector((self.x + other.x), (self.y + other.y), (self.z + other.z))

  # Sobreescritura de la resta de vectores.
  def __sub__(self, other):
    return Vector((self.x - other.x), (self.y - other.y), (self.z - other.z))

  # Sobreescritura de la multiplicación de vectores.
  def __mul__(self, other):

    # Si se multiplica un vector por un número real, el vector cambia sus dimensiones.
    if ((type(other) == int) or (type(other) == float)):
      return Vector((other * self.x), (other * self.y), (other * self.z))

    # Si se multiplican dos vectores, se ejecuta un producto cruz.
    return Vector(
      ((self.y * other.z) - (self.z * other.y)),
      ((self.z * other.x) - (self.x * other.z)),
      ((self.x * other.y) - (self.y * other.x)),
    )

  # Producto punto entre vectores.
  def __matmul__(self, other):
    return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))

  # Método que retorna la longitud de un vector.
  def length(self):
    return (((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5)

  # Método que retorna el vector normalizado.
  def norm(self):
    return ((self * (1 / self.length())) if (self.length() != 0) else Vector(1, 1, 1))

  # Representación textual del vector.
  def __repr__(self):
    return f"<{self.x}, {self.y}, {self.z}>"
