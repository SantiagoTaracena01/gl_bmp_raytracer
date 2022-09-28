"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías necesarias importadas.
from raytracer import Raytracer
from vector import Vector
from sphere import Sphere
from material import Material
from light import Light
from color import Color
import utils
import time

# Ejecución del código principal del proyecto.
if __name__ == "__main__":

  # Materiales creados en clase.
  red = Material(Color(255, 0, 0))
  white = Material(Color(255, 255, 255))
  black = Material(Color(0, 0, 0))
  orange = Material(Color(225, 135, 65))

  # Instancia del raytracer y color de fondo.
  raytracer = Raytracer(600, 600)
  raytracer.set_ray_probability(1)
  raytracer.background_color = Color(0, 0, 50)
  raytracer.light = Light(Vector(-5, -5, 0), 1)

  # raytracer.objects = [
  #   Sphere(Vector(-4, 0, -16), 2, red),
  #   Sphere(Vector(2, 0, -10), 2, white)
  # ]

  # Mapeo del muñeco de nieve a dibujar.
  snowman = [
    {
      "color": utils.BLACK,
      "spheres": [
        Sphere(Vector(-0.6, -6, -20), 0.35),
        Sphere(Vector(0.6, -6, -20), 0.35),
        Sphere(Vector(-1, -4.25, -20), 0.2),
        Sphere(Vector(-0.6, -3.85, -20), 0.2),
        Sphere(Vector(0, -3.75, -20), 0.2),
        Sphere(Vector(0.6, -3.85, -20), 0.2),
        Sphere(Vector(1, -4.25, -20), 0.2),
        Sphere(Vector(0, -2, -20), 0.35),
        Sphere(Vector(0, -0.5, -20), 0.35),
        Sphere(Vector(0, 1, -20), 0.35),
      ],
    },
    {
      "color": utils.ORANGE,
      "spheres": [
        Sphere(Vector(0, -5, -20), 0.35),
      ],
    },
    {
      "color": utils.WHITE,
      "spheres": [
        Sphere(Vector(0, -5, -20), 2),
        Sphere(Vector(0, -1, -20), 3),
        Sphere(Vector(0, 4, -20), 4),
      ],
    },
  ]

  # Esferas y colores necesarios para el muñeco de nieve.
  for part in snowman:
    for sphere in part["spheres"]:
      raytracer.objects.append(sphere)  
      raytracer.colors.append(part["color"])

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  # image_path = raytracer.write()
  image_path = raytracer.write("./images/snowman.bmp")

  # Impresión de resultados.
  print(f"\nRendering process has been finished! Check {image_path}!")
  print(f"Finished in {round((time.time() - start), 4)} seconds.\n")
