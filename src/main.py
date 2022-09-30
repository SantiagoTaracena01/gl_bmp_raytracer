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
  rubber = Material(Color(80, 0, 0), albedo=[0.9, 0.1], spec=5)
  ivory = Material(Color(100, 100, 80), albedo=[0.6, 0.3], spec=70)

  # Instancia del raytracer y color de fondo.
  raytracer = Raytracer(600, 600)
  raytracer.background_color = Color(0, 0, 50)
  raytracer.light = Light(Vector(-8, -8, 0), 1, Color(255, 255, 255))

  # Objetos para renderizar con el raytracer.
  raytracer.scene = [
    Sphere(Vector(-4.25, 0, -16), 2, rubber),
    Sphere(Vector(1.75, 0, -10), 2, ivory),
  ]

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  image_path = raytracer.write()

  # Impresión de resultados.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {image_path}!\n")
