"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Módulos necesarios.
from vector import Vector
import math
import utils
import random

# Definición de la clase Raytracer.
class Raytracer(object):

  # Constantes del raytracer.
  __FILE_HEADER_SIZE = 14
  __IMAGE_HEADER_SIZE = 40
  __HEADER_SIZE = (__FILE_HEADER_SIZE + __IMAGE_HEADER_SIZE)
  __COLORS_PER_PIXEL = 3

  # Método constructor del raytracer.
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.background_color = utils.BLACK
    self.current_color = utils.WHITE
    self.framebuffer = []
    self.ray_probability = 1
    self.objects = []
    self.colors = []
    self.clear()

  # Método para limpiar la pantalla del raytracer.
  def clear(self):
    self.framebuffer = [[self.background_color for x in range(self.width)] for y in range(self.height)]

  # Método para cambiar fácilmente el color de fondo.
  def set_background_color(self, r, g, b):
    self.background_color = utils.color(r, g, b)
  
  # Método para cambiar fácilmente el color del dibujo.
  def set_current_color(self, r, g, b):
    self.current_color = utils.color(r, g, b)

  # Método para dibujar un punto en la pantalla del raytracer.
  def point(self, x, y, color=None):
    if ((0 <= y <= self.height) and (0 <= x <= self.width)):
      self.framebuffer[y][x] = color or self.current_color

  def cast_ray(self, origin, direction):
    for object, color in zip(self.objects, self.colors):
      if (object.ray_interception(origin, direction)):
        return color
    return self.background_color

  def set_ray_probability(self, ray_probability):
    self.ray_probability = ray_probability

  def render(self):
    
    field_of_view = int(math.pi / 2)
    aspect_ratio = (self.width / self.height)
    tangent = math.tan(field_of_view / 2)
    
    for y in range(self.height):
      for x in range(self.width):
        
        random_value = random.random()

        if (random_value <= self.ray_probability):
          
          i = ((((2 * (x + 0.5)) / self.width) - 1) * (tangent * aspect_ratio))
          j = ((1 - ((2 * (y + 0.5)) / self.height)) * tangent)
          origin = Vector(0, 0, 0)
          direction = Vector(i, j, -1).norm()
          color = self.cast_ray(origin, direction)
          self.point(y, x, color)

  # Método para renderizar el raytracer.
  def write(self, filename="./images/image.bmp"):

    bmp_filename = filename if filename.endswith(".bmp") else f"{filename}.bmp"
    actual_filename = bmp_filename if bmp_filename.startswith("./images/") else f"./images/{bmp_filename}"

    file = open(actual_filename, "bw")

    file.write(utils.char("B"))
    file.write(utils.char("M"))
    file.write(utils.dword(self.__HEADER_SIZE + (self.width * self.height * self.__COLORS_PER_PIXEL)))
    file.write(utils.dword(0))
    file.write(utils.dword(self.__HEADER_SIZE))

    file.write(utils.dword(self.__IMAGE_HEADER_SIZE))
    file.write(utils.dword(self.width))
    file.write(utils.dword(self.height))
    file.write(utils.word(1))
    file.write(utils.word(24))
    file.write(utils.dword(0))
    file.write(utils.dword(self.width * self.height * self.__COLORS_PER_PIXEL))
    file.write(utils.dword(0))
    file.write(utils.dword(0))
    file.write(utils.dword(0))
    file.write(utils.dword(0))

    for x in range(self.width):
      for y in range(self.height):
        file.write(self.framebuffer[y][x])

    file.close()
