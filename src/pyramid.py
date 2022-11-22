"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías utilizadas para el desarrollo de la clase Pyramid.
from triangle import Triangle

# Definición de la clase Pyramid.
class Pyramid(object):

  # Método constructor de la clase Pyramid.
  def __init__(self, vertices, material):
    self.vertices = vertices
    self.material = material
    self.triangles = self.__get_pyramid_triangles()

  # Método para calcular los triángulos de la pirámide.
  def __get_pyramid_triangles(self):
    first_vertex, second_vertex, third_vertex, fourth_vertex = self.vertices
    first_triangle = Triangle((first_vertex, second_vertex, third_vertex), self.material)
    second_triangle = Triangle((first_vertex, second_vertex, fourth_vertex), self.material)
    third_triangle = Triangle((first_vertex, fourth_vertex, third_vertex), self.material)
    fourth_triangle = Triangle((second_vertex, fourth_vertex, third_vertex), self.material)
    return first_triangle, second_triangle, third_triangle, fourth_triangle

  # Método para calcular la intercepción entre un rayo y la pirámide.
  def ray_interception(self, origin, direction):

    # Valor máximo e intercepto actual (ninguno).
    max_t_value = 999_999
    actual_intersect = None

    # Iteración sobre los triángulos de la pirámide.
    for triangle in self.triangles:

      # Intercepto entre el triángulo iterado y el rayo.
      triangle_intersect = triangle.ray_interception(origin, direction)

      # Si el intercepto no es nulo y la distancia es menor al máximo local, se cambia el intercepto.
      if ((triangle_intersect is not None) and (triangle_intersect.distance < max_t_value)):
        max_t_value = triangle_intersect.distance
        actual_intersect = triangle_intersect

    # Retorno del intercepto hallado, sea None o no.
    return actual_intersect
