"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Librerías necesarias importadas.
from raytracer import Raytracer
from vector import Vector
from sphere import Sphere
from plane import Plane
from cube import Cube
from triangle import Triangle
from pyramid import Pyramid
from material import Material
from light import Light
from color import Color
from envmap import Envmap
import time

# Ejecución del código principal del proyecto.
if __name__ == "__main__":

  # Materiales creados en la clase.
  sand = Material(Color(250, 200, 150), [0.9, 0.1, 0, 0], 20)
  water = Material(Color(0, 20, 100), [0.6, 0.4, 0.5, 0,5], 200)
  jump_sphere = Material(Color(200, 200, 50), [0.6, 0.4, 0, 0], 80)

  # Instancia del raytracer y color de fondo.
  raytracer = Raytracer(760, 760)
  raytracer.background_color = Color(0, 190, 255)
  raytracer.light = Light(Vector(0, -5, 5), 25, Color(255, 255, 255))
  raytracer.set_ray_probability(1)

  # Escena definida en clase.
  raytracer.scene = [
    Plane(Vector(0, 0.5, -5), 12, 12, water),
    Sphere(Vector(1, -2, -7.5), 1, jump_sphere),
    # Cube(Vector(-1, 0, -10), 1, gold),
  ]

  # Fondo de pantalla de la imagen generada por el raytracer.
  # raytracer.set_envmap(Envmap("./env/envmap.bmp"))

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  image_path = raytracer.write("./images/scene.bmp")

  # Impresión de resultados.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {image_path}!\n")
