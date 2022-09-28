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
  raytracer.background_color = Color(0, 0, 50)
  raytracer.light = Light(Vector(-8, -8, 0), 1)

  # Objetos para renderizar con el raytracer.
  raytracer.scene = [
    Sphere(Vector(-4, 0, -16), 2, red),
    Sphere(Vector(2, 0, -10), 2, white),
  ]

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  image_path = raytracer.write()

  # Impresión de resultados.
  print(f"\nRendering process has been finished! Check {image_path}!")
  print(f"Finished in {round((time.time() - start), 4)} seconds.\n")
