"""
Universidad del Valle de Guatemala
(CC2018) Gráficas por Computadora
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el archivo.
from vector import Vector
from light import Light
from color import Color
import math
import utils
import random

MAX_RECURSION_DEPTH = 3

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
    self.ray_probability = 1
    self.framebuffer = []
    self.scene = []
    self.colors = []
    self.light = Light(Vector(0, 0, 0), 1, Color(255, 255, 255))
    self.clear()

  # Método para limpiar la pantalla del raytracer.
  def clear(self):
    self.framebuffer = [[self.background_color for x in range(self.width)] for y in range(self.height)]

  # Método para cambiar fácilmente el color de fondo.
  def set_background_color(self, r, g, b):
    self.background_color = Color(r, g, b)
  
  # Método para cambiar fácilmente el color del dibujo.
  def set_current_color(self, r, g, b):
    self.current_color = Color(r, g, b)

  # Método para dibujar un punto en la pantalla del raytracer.
  def point(self, x, y, color=None):
    if ((0 <= y <= self.height) and (0 <= x <= self.width)):
      self.framebuffer[y][x] = color or self.current_color

  # Método que verifica si un rayo pasa por un objeto del mundo.
  def cast_ray(self, origin, direction, recursion_counter=0):

    # Contador de la recursividad del método.
    if (recursion_counter >= MAX_RECURSION_DEPTH):
      return self.background_color

    # Material e intercepto hallados mediante la función para encontrar el intercepto de la escena.
    material, intersect = self.scene_intersect(origin, direction)

    # Retorno del color de fondo si el material no se ha encontrado.
    if (material is None):
      return self.background_color

    # Cálculo de la dirección de la luz y la intensidad del color.
    light_direction = (self.light.position - intersect.hit_point).norm()

    # Cálculo del material e intercepto de la sombra.
    shadow_bias = 1.1
    shadow_origin = (intersect.hit_point + (intersect.normal * shadow_bias))
    shadow_material, _ = self.scene_intersect(shadow_origin, light_direction)
    shadow_intensity = 0.75 if (shadow_material is not None) else 0

    # Componente del difuso a pintar en el pixel del framebuffer.
    diffuse_intensity = (light_direction @ intersect.normal)
    actual_diffuse = (material.diffuse * diffuse_intensity * material.albedo[0] * (1 - shadow_intensity))

    # Cálculo de componentes especulares de la figura.
    light_reflection = utils.reflect(light_direction, intersect.normal)
    reflection_intensity = max(0, (light_reflection @ direction))
    specular_intensity = (self.light.intensity * (reflection_intensity ** material.spec))

    # Cálculo del componente especular.
    specular_component = (self.light.color * specular_intensity * material.albedo[1])

    # Cálculo de la reflexión del material.
    if (material.albedo[2] > 0):
      reverse_direction = (direction * -1)
      reflection_direction = utils.reflect(reverse_direction, intersect.normal)
      reflection_bias = -0.5 if ((reflection_direction @ intersect.normal) < 0) else 0.5
      reflection_origin = (intersect.hit_point + (intersect.normal * reflection_bias))
      reflection_color = self.cast_ray(reflection_origin, reflection_direction, (recursion_counter + 1))
    else:
      reflection_color = Color(0, 0, 0)

    # Cálculo de la refracción del material.
    if (material.albedo[3] > 0):
      refraction_direction = utils.refract(direction, intersect.normal, material.refractive_index)
      refraction_bias = -0.5 if ((refraction_direction @ intersect.normal) < 0) else 0.5
      refraction_origin = (intersect.hit_point + (intersect.normal * refraction_bias))
      refract_color = self.cast_ray(refraction_origin, refraction_direction, (recursion_counter + 1))
    else:
      refract_color = Color(0, 0, 0)

    # Valores finales de la reflexión y la refracción.
    reflection = (reflection_color * material.albedo[2])
    refraction = (refract_color * material.albedo[3])

    # Retorno del color a pintar.
    return (actual_diffuse + specular_component + reflection + refraction)

  # Método que halla la intersección del rayo con un objeto.
  def scene_intersect(self, origin, direction):

    # Variables importantes para el cálculo del intercepto del raytracer.
    z_buffer = 999_999
    material = None
    intersect = None

    # Iteración sobre todos los objetos de la escena.
    for object in self.scene:

      # Cálculo de la intersección del rayo con el objeto.
      object_intersect = object.ray_interception(origin, direction)

      # Condicional que se ejecuta si el rayo interceptó un objeto y su distancia es menor al z buffer.
      if (object_intersect and (object_intersect.distance < z_buffer)):

        # Reinstancia de las variables para calcular los colores.
        z_buffer = object_intersect.distance
        material = object.material
        intersect = object_intersect

    # Retorno del material y den itercepto dónde pintarlo.
    return material, intersect

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
        file.write(self.framebuffer[y][x].to_bytes())

    # Cierre del archivo.
    file.close()

    # Retorno del nombre del archivo para futuras operaciones.
    return actual_filename
