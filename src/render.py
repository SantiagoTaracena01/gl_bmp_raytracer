"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Módulos necesarios.
import math
import utils

# Definición de la clase Render.
class Render(object):

  # Propiedades variables del Render.
  __width = 0
  __height = 0
  __framebuffer = []
  __viewport_width = 0
  __viewport_height = 0
  __viewport_x_coordinate = 0
  __viewport_y_coordinate = 0

  # Constantes del render.
  __MAX_DIMENSION = 2147483647
  __FILE_HEADER_SIZE = 14
  __IMAGE_HEADER_SIZE = 40
  __HEADER_SIZE = (__FILE_HEADER_SIZE + __IMAGE_HEADER_SIZE)
  __COLORS_PER_PIXEL = 3

  # Constructor de la clase Render.
  def __init__(self):
    self.__current_color = utils.BLACK
    self.__viewport_color = utils.WHITE
    self.__vertex_color = utils.RED

  # Función que se encarga de crear una ventana.
  def gl_create_window(self, width, height):
    self.__width = width
    self.__height = height
    self.gl_clear()

  # Función que cambia el color de gl_viewport().
  def gl_viewport_color(self, r, g, b):
    self.__viewport_color = utils.color(
      math.ceil(r * 255),
      math.ceil(g * 255),
      math.ceil(b * 255),
    )

  # Función que crea un viewport sobre el cuál dibujar.
  def gl_viewport(self, x, y, width, height):
    self.__viewport_x_coordinate = x
    self.__viewport_y_coordinate = y
    self.__viewport_width = width
    self.__viewport_height = height
    for w in range(self.__viewport_width + 1):
      for h in range(self.__viewport_height + 1):
        self.__framebuffer[self.__viewport_y_coordinate + h][self.__viewport_x_coordinate + w] = self.__viewport_color

  # Función que limpia la ventana a un sólo color.
  def gl_clear(self):
    self.__framebuffer = [[(self.__current_color) for x in range(self.__width)] for y in range(self.__height)]

  # Función que cambia el color de gl_clear().
  def gl_clear_color(self, r, g, b):
    self.__current_color = utils.color(
      math.ceil(r * 255),
      math.ceil(g * 255),
      math.ceil(b * 255),
    )

  # Función que coloca un punto en la pantalla con coordenadas absolutas.
  def gl_vertex(self, x, y):
    self.__framebuffer[y + self.__viewport_y_coordinate][x + self.__viewport_x_coordinate] = self.__vertex_color

  # Función que convierte coordenadas absolutas a relativas.
  def __relative_to_absolute_conversion(self, x, y):
    cx, cy = (self.__viewport_width // 2), (self.__viewport_height // 2)
    px, py = ((cx * x) + cx + self.__viewport_x_coordinate), ((cy * y) + cy + self.__viewport_y_coordinate)
    return (px, py)

  # Función que coloca un punto en la pantalla con coordenadas relativas.
  def gl_relative_vertex(self, x, y):
    px, py = self.__relative_to_absolute_conversion(x, y)
    self.__framebuffer[round(px)][round(py)] = self.__vertex_color

  # Función que cambia el color de gl_point() y gl_vertex().
  def gl_color(self, r, g, b):
    self.__vertex_color = utils.color(
      math.ceil(r * 255),
      math.ceil(g * 255),
      math.ceil(b * 255),
    )

  # Función que escribe el archivo .bmp con la imagen finalizada.
  def gl_finish(self, filename="./images/image.bmp"):

    bmp_filename = filename if filename.endswith(".bmp") else f"{filename}.bmp"
    actual_filename = bmp_filename if bmp_filename.startswith("./images/") else f"./images/{bmp_filename}"

    file = open(actual_filename, "bw")

    file.write(utils.char("B"))
    file.write(utils.char("M"))
    file.write(utils.dword(self.__HEADER_SIZE + (self.__width * self.__height * self.__COLORS_PER_PIXEL)))
    file.write(utils.dword(0))
    file.write(utils.dword(self.__HEADER_SIZE))

    file.write(utils.dword(self.__IMAGE_HEADER_SIZE))
    file.write(utils.dword(self.__width))
    file.write(utils.dword(self.__height))
    file.write(utils.word(1))
    file.write(utils.word(24))
    file.write(utils.dword(0))
    file.write(utils.dword(self.__width * self.__height * self.__COLORS_PER_PIXEL))
    file.write(utils.dword(0))
    file.write(utils.dword(0))
    file.write(utils.dword(0))
    file.write(utils.dword(0))

    for x in range(self.__width):
      for y in range(self.__height):
        file.write(self.__framebuffer[y][x])

    file.close()
