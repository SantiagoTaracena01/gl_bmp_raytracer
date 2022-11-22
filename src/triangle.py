"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de la clase Triangle.
from intersect import Intersect
from vector import Vector

# Definición de la clase Triangle.
class Triangle(object):

  # Método constructor de la clase Triangle.
  def __init__(self, vertices, material):
    self.vertices = vertices
    self.individual_vertices = self.__get_individual_vertices()
    self.material = material

  # Método que obtiene los vértices individuales del triángulo.
  def __get_individual_vertices(self):
    vertices = []
    for vertex in self.vertices:
      individual_vertex = Vector(*vertex)
      vertices.append(individual_vertex)
    return vertices

  # Método que detecta una intercepción entre un rayo y el triángulo.
  def ray_interception(self, origin, direction):

    # Vértices del triángulo.
    first_vertex, second_vertex, third_vertex = self.vertices

    # Bordes necesarios para el cálculo de las coordenadas del triángulo.
    first_edge = (second_vertex - first_vertex)
    second_edge = (third_vertex - first_vertex)

    # Cálculo de las coordenadas iniciales del triángulo.
    rel_height = (direction * second_edge)
    tilt = (first_edge @ rel_height)

    # El rayo no intercepta si el tilt tiende a cero.
    if (-1E-06 < tilt < 1E-06):
      return None

    # Tilt inverso y cálculo de la coordenada u.
    inverse_tilt = (1 / tilt)
    u = inverse_tilt * ((origin - first_vertex) @ rel_height)

    # El rayo tampoco intercepta si la coordenada u no está entre (0, 1).
    if ((u < 0) or (u > 1)):
      return None

    # Cálculo de la coordenada v.
    qvec = ((origin - first_vertex) * first_edge)
    v = inverse_tilt * (direction @ qvec)

    # Si v es menor a cero o (u + v) es mayor a uno, el rayo se sale de las dimensiones del triángulo.
    if ((v < 0) or ((u + v) > 1)):
      return None

    # Cálculo de la variable t de las ecuaciones del triángulo.
    tvec = inverse_tilt * (second_edge @ qvec)

    # Si tvec no tiende a cero por la derecha, se retorna el intercepto.
    if (tvec > 1E-06):

      # Cálculo del impacto y la normal del intercepto.
      hit_point = (origin + (direction * tvec))
      normal = (first_edge * second_edge).norm()

      # Retorno del intercepto calculado.
      return Intersect(
        distance=tvec,
        hit_point=hit_point,
        normal=normal,
      )

    # Si tvec tiende a cero, no existe ningún intercepto.
    else:
      return None
