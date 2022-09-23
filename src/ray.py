"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Módulos necesarios.
import utils

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
    self.clear_color = utils.BLACK
    self.current_color = utils.WHITE
    self.framebuffer = []
    self.clear()

  # Método para limpiar la pantalla del raytracer.
  def clear(self):
    self.framebuffer = [[self.clear_color for x in range(self.width)] for y in range(self.height)]

  # Método para dibujar un punto en la pantalla del raytracer.
  def point(self, x, y, color=None):
    if ((0 < y < self.height) and (0 < x < self.width)):
      self.framebuffer[y][x] = color or self.current_color

  # Método para renderizar el raytracer.
  def render(self, filename="./images/image.bmp"):

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
