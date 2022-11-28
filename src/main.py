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
  stone = Material(Color(100, 100, 100), [0.9, 0.1, 0, 0], 0)
  cactus = Material(Color(0, 150, 40), [0.7, 0.3, 0, 0], 150)
  obsidian = Material(Color(35, 10, 45), [0.7, 0.3, 0.2, 0], 1000)
  portal = Material(Color(240, 160, 255), [0.5, 0.5, 0.1, 0.5], 300, 1.25)

  # Instancia del raytracer y color de fondo.
  raytracer = Raytracer(1000, 1000)
  raytracer.background_color = Color(0, 190, 255)
  raytracer.light = Light(Vector(5, -5, 5), 25, Color(255, 255, 255))
  raytracer.set_ray_probability(1)

  # Escena definida en clase.
  raytracer.scene = [

    # Suelo de la escena.
    Plane(Vector(0, 2, -5), 12, 12, sand),

    # Pirámide de la escena.
    Pyramid(((-3.5, 2.5, -10), (-1.5, 2.5, -10), (-2.5, 0, -9), (-2.5, 2.5, -8)), stone),

    # Primer cactus de la escena.
    Cube(Vector(-3, 1.75, -6.5), 0.5, cactus),
    Cube(Vector(-3, 1.25, -6.5), 0.5, cactus),
    Cube(Vector(-3, 0.75, -6.5), 0.5, cactus),

    # Segundo cactus de la escena.
    Cube(Vector(3.25, 1.75, -7), 0.5, cactus),
    Cube(Vector(3.25, 1.25, -7), 0.5, cactus),
    Cube(Vector(3.25, 0.75, -7), 0.5, cactus),

    # Portal al Nether (Exterior).
    Cube(Vector(1, 1.75, -8), 0.5, obsidian),
    Cube(Vector(1, 1.25, -8), 0.5, obsidian),
    Cube(Vector(1, 0.75, -8), 0.5, obsidian),
    Cube(Vector(1, 0.25, -8), 0.5, obsidian),
    Cube(Vector(1, -0.25, -8), 0.5, obsidian),
    Cube(Vector(1.5, 1.75, -8), 0.5, obsidian),
    Cube(Vector(2, 1.75, -8), 0.5, obsidian),
    Cube(Vector(2.5, 1.75, -8), 0.5, obsidian),
    Cube(Vector(1.5, -0.25, -8), 0.5, obsidian),
    Cube(Vector(2, -0.25, -8), 0.5, obsidian),
    Cube(Vector(2.5, -0.25, -8), 0.5, obsidian),
    Cube(Vector(2.5, 1.25, -8), 0.5, obsidian),
    Cube(Vector(2.5, 0.75, -8), 0.5, obsidian),
    Cube(Vector(2.5, 0.25, -8), 0.5, obsidian),

    # Portal al Nether (Interior).
    Cube(Vector(1.5, 1.25, -8), 0.5, portal),
    Cube(Vector(1.5, 0.75, -8), 0.5, portal),
    Cube(Vector(1.5, 0.25, -8), 0.5, portal),
    Cube(Vector(2, 1.25, -8), 0.5, portal),
    Cube(Vector(2, 0.75, -8), 0.5, portal),
    Cube(Vector(2, 0.25, -8), 0.5, portal),
  ]

  # Fondo de pantalla de la imagen generada por el raytracer.
  raytracer.set_envmap(Envmap("./env/desert.bmp"))

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  image_path = raytracer.write("./images/scene.bmp")

  # Impresión de resultados.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {image_path}!\n")
