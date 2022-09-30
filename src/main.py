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
  first_bear_hair = Material(Color(220, 230, 250), albedo=[0.9, 0.1], spec=5)
  first_bear_skin = Material(Color(180, 200, 210), albedo=[0.6, 0.4], spec=50)
  second_bear_hair = Material(Color(210, 130, 70), albedo=[0.9, 0.1], spec=10)
  second_bear_parts = Material(Color(150, 40, 20), albedo=[0.9, 0.1], spec=5)
  second_bear_skin = Material(Color(220, 20, 10), albedo=[0.6, 0.4], spec=50)
  black_material = Material(Color(0, 0, 0), albedo=[0.5, 0.5], spec=250)

  # Instancia del raytracer y color de fondo.
  raytracer = Raytracer(600, 600)
  raytracer.background_color = Color(255, 255, 255)
  raytracer.light = Light(Vector(8, 2, 0), 1, Color(255, 255, 255))

  # Objetos para renderizar con el raytracer.
  raytracer.scene = [

    # Primer oso.
    Sphere(Vector(-4, -2, -16), 2, first_bear_hair),
    Sphere(Vector(-3, -0.75, -12), 0.75, first_bear_hair),
    Sphere(Vector(-5.75, -3.5, -16), 0.75, first_bear_hair),
    Sphere(Vector(-2.25, -3.5, -16), 0.75, first_bear_hair),
    Sphere(Vector(-4.5, 1, -18), 2.25, first_bear_skin),
    Sphere(Vector(-6.25, 0.25, -17), 1, first_bear_hair),
    Sphere(Vector(-2.25, 0.25, -17), 1, first_bear_hair),
    Sphere(Vector(-5.5, 3, -17), 1, first_bear_hair),
    Sphere(Vector(-3, 3, -17), 1, first_bear_hair),
    Sphere(Vector(-3, -1.5, -10), 0.15, black_material),
    Sphere(Vector(-2, -1.5, -10), 0.15, black_material),
    Sphere(Vector(-2.5, -0.85, -10), 0.15, black_material),

    # Segundo oso.
    Sphere(Vector(4, -2, -16), 2, second_bear_hair),
    Sphere(Vector(3, -0.95, -12), 0.75, second_bear_parts),
    Sphere(Vector(5.75, -3.5, -16), 0.75, second_bear_parts),
    Sphere(Vector(2.25, -3.5, -16), 0.75, second_bear_parts),
    Sphere(Vector(4.5, 1, -18), 2.25, second_bear_skin),
    Sphere(Vector(6.25, 0.25, -17), 1, second_bear_hair),
    Sphere(Vector(2.25, 0.25, -17), 1, second_bear_hair),
    Sphere(Vector(5.5, 3, -17), 1, second_bear_hair),
    Sphere(Vector(3, 3, -17), 1, second_bear_hair),
    Sphere(Vector(3, -1.65, -10), 0.15, black_material),
    Sphere(Vector(2, -1.65, -10), 0.15, black_material),
    Sphere(Vector(2.5, -0.95, -10), 0.15, black_material),
  ]

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  image_path = raytracer.write("./images/bears.bmp")

  # Impresión de resultados.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {image_path}!\n")
