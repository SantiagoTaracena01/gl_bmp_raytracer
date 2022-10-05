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

  # Materiales creados en la clase.
  ivory = Material(diffuse=Color(100, 100, 80), albedo=[0.6,  0.3], spec=50)
  rubber = Material(diffuse=Color(80, 0, 0), albedo=[0.9,  0.1], spec=10)

  # Instancia del raytracer y color de fondo.
  raytracer = Raytracer(1000, 1000)
  raytracer.background_color = Color(0, 0, 0)
  raytracer.light = Light(Vector(-20, 20, 20), 1.5, Color(255, 255, 255))

  # Escena definida en clase.
  raytracer.scene = [
    Sphere(Vector(0, -1.5, -10), 1.5, ivory),
    Sphere(Vector(-2, -1, -12), 2, rubber),
    Sphere(Vector(1, 1, -8), 1.7, rubber),
    Sphere(Vector(-2, 2, -10), 2, ivory),
  ]

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  image_path = raytracer.write()

  # Impresión de resultados.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {image_path}!\n")
