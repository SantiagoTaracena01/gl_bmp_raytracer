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

  # Método que verifica si un rayo pasa por un objeto del mundo.
  def cast_ray(self, origin, direction):
    for object, color in zip(self.objects, self.colors):
      if (object.ray_interception(origin, direction)):
        return color
    return self.background_color

  # Método setter para la probabilidad del disparo de un rayo.
  def set_ray_probability(self, ray_probability):
    self.ray_probability = ray_probability

  # Método para renderizar una escena.
  def render(self):

    # Constantes importantes para los cálculos del método.
    aspect_ratio = (self.width / self.height)
    field_of_view = int(math.pi / 2)
    tangent = math.tan(field_of_view / 2)

    # Iteración sobre el framebuffer.
    for y in range(self.height):
      for x in range(self.width):

        # Valor aleatorio para simular una probabilidad de disparo.
        random_value = random.random()

        # Disparo del rayo y dibujo de un punto en la pantalla si la condición se cumple.
        if (random_value <= self.ray_probability):
          i = ((((2 * (x + 0.5)) / self.width) - 1) * (tangent * aspect_ratio))
          j = ((1 - ((2 * (y + 0.5)) / self.height)) * tangent)
          origin = Vector(0, 0, 0)
          direction = Vector(i, j, -1).norm()
          color = self.cast_ray(origin, direction)
          self.point(y, x, color)

  # Método para renderizar el raytracer.
  def write(self, filename="./images/image.bmp"):

    # Formateo del nombre del archivo para estar en la carpeta de imágenes.
    bmp_filename = filename if filename.endswith(".bmp") else f"{filename}.bmp"
    actual_filename = bmp_filename if bmp_filename.startswith("./images/") else f"./images/{bmp_filename}"

    # Apertura del archivo.
    file = open(actual_filename, "bw")

    # Escritura preliminar del header del archivo.
    file.write(utils.char("B"))
    file.write(utils.char("M"))
    file.write(utils.dword(self.__HEADER_SIZE + (self.width * self.height * self.__COLORS_PER_PIXEL)))
    file.write(utils.dword(0))
    file.write(utils.dword(self.__HEADER_SIZE))

    # Finalización de la escritura del header del archivo.
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

    # Escritura de cada pixel del archivo mediante los valores del framebuffer.
    for x in range(self.width):
      for y in range(self.height):
        file.write(self.framebuffer[y][x])

    # Cierre del archivo.
    file.close()

    # Retorno del nombre del archivo para futuras operaciones.
    return actual_filename
