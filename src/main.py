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
  rose = Material(Color(255, 15, 90), [0.6, 0.4, 0, 0], 200)
  obsidian = Material(Color(35, 10, 45), [0.7, 0.3, 0.2, 0], 1000)
  portal = Material(Color(240, 160, 255), [0.5, 0.5, 0.1, 0.5], 300, 1.25)
  wither_head = Material(Color(60, 60, 60), [0.8, 0.2, 0, 0], 50)
  wither_body = Material(Color(30, 30, 30), [0.8, 0.2, 0, 0], 50)

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
    Pyramid(((-4.5, 3, -10), (1, 3, -10), (-2.25, -1, -9), (-2.25, 3, -8)), stone),

    # Primer cactus de la escena.
    Cube(Vector(-3, 1.8, -6.5), 0.35, cactus),
    Cube(Vector(-3, 1.45, -6.5), 0.35, cactus),
    Cube(Vector(-3, 1.1, -6.5), 0.35, cactus),
    Cube(Vector(-2.65, 0.85, -6.25), 0.15, rose),
    Cube(Vector(-3.2, 1.3, -6.25), 0.15, rose),

    # Segundo cactus de la escena.
    Cube(Vector(3.25, 1.8, -7), 0.35, cactus),
    Cube(Vector(3.25, 1.45, -7), 0.35, cactus),
    Cube(Vector(3.25, 1.1, -7), 0.35, cactus),
    Cube(Vector(2.9, 0.85, -6.75), 0.15, rose),
    Cube(Vector(3.45, 1.5, -6.75), 0.15, rose),

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

    # Wither volando en el cielo.
    Cube(Vector(8, -8, -20), 1, wither_head),
    Cube(Vector(6.5, -8, -20), 1, wither_head),
    Cube(Vector(5, -8, -20), 1, wither_head),
    Cube(Vector(5, -7.5, -20), 0.25, wither_body),
    Cube(Vector(5.25, -7.5, -20), 0.25, wither_body),
    Cube(Vector(5.5, -7.5, -20), 0.25, wither_body),
    Cube(Vector(5.75, -7.5, -20), 0.25, wither_body),
    Cube(Vector(6, -7.5, -20), 0.25, wither_body),
    Cube(Vector(6.25, -7.5, -20), 0.25, wither_body),
    Cube(Vector(6.5, -7.5, -20), 0.25, wither_body),
    Cube(Vector(6.75, -7.5, -20), 0.25, wither_body),
    Cube(Vector(7, -7.5, -20), 0.25, wither_body),
    Cube(Vector(7.25, -7.5, -20), 0.25, wither_body),
    Cube(Vector(7.5, -7.5, -20), 0.25, wither_body),
    Cube(Vector(7.75, -7.5, -20), 0.25, wither_body),
    Cube(Vector(8, -7.5, -20), 0.25, wither_body),
    Cube(Vector(6.5, -7, -20), 0.5, wither_body),
    Cube(Vector(6.5, -6.5, -20), 0.5, wither_body),
    Cube(Vector(6.5, -6, -20), 0.5, wither_body),
    Cube(Vector(6.5, -5.5, -20), 0.5, wither_body),
    Cube(Vector(6.5, -5, -20), 0.5, wither_body),
    Cube(Vector(5.25, -7, -20), 0.25, wither_body),
    Cube(Vector(5.5, -7, -20), 0.25, wither_body),
    Cube(Vector(5.75, -7, -20), 0.25, wither_body),
    Cube(Vector(6, -7, -20), 0.25, wither_body),
    Cube(Vector(6.25, -7, -20), 0.25, wither_body),
    Cube(Vector(6.5, -7, -20), 0.25, wither_body),
    Cube(Vector(6.75, -7, -20), 0.25, wither_body),
    Cube(Vector(7, -7, -20), 0.25, wither_body),
    Cube(Vector(7.25, -7, -20), 0.25, wither_body),
    Cube(Vector(7.5, -7, -20), 0.25, wither_body),
    Cube(Vector(7.75, -7, -20), 0.25, wither_body),
    Cube(Vector(5.25, -6.5, -20), 0.25, wither_body),
    Cube(Vector(5.5, -6.5, -20), 0.25, wither_body),
    Cube(Vector(5.75, -6.5, -20), 0.25, wither_body),
    Cube(Vector(6, -6.5, -20), 0.25, wither_body),
    Cube(Vector(6.25, -6.5, -20), 0.25, wither_body),
    Cube(Vector(6.5, -6.5, -20), 0.25, wither_body),
    Cube(Vector(6.75, -6.5, -20), 0.25, wither_body),
    Cube(Vector(7, -6.5, -20), 0.25, wither_body),
    Cube(Vector(7.25, -6.5, -20), 0.25, wither_body),
    Cube(Vector(7.5, -6.5, -20), 0.25, wither_body),
    Cube(Vector(7.75, -6.5, -20), 0.25, wither_body),
    Cube(Vector(5.25, -6, -20), 0.25, wither_body),
    Cube(Vector(5.5, -6, -20), 0.25, wither_body),
    Cube(Vector(5.75, -6, -20), 0.25, wither_body),
    Cube(Vector(6, -6, -20), 0.25, wither_body),
    Cube(Vector(6.25, -6, -20), 0.25, wither_body),
    Cube(Vector(6.5, -6, -20), 0.25, wither_body),
    Cube(Vector(6.75, -6, -20), 0.25, wither_body),
    Cube(Vector(7, -6, -20), 0.25, wither_body),
    Cube(Vector(7.25, -6, -20), 0.25, wither_body),
    Cube(Vector(7.5, -6, -20), 0.25, wither_body),
    Cube(Vector(7.75, -6, -20), 0.25, wither_body),
    Cube(Vector(5.25, -5.5, -20), 0.25, wither_body),
    Cube(Vector(5.5, -5.5, -20), 0.25, wither_body),
    Cube(Vector(5.75, -5.5, -20), 0.25, wither_body),
    Cube(Vector(6, -5.5, -20), 0.25, wither_body),
    Cube(Vector(6.25, -5.5, -20), 0.25, wither_body),
    Cube(Vector(6.5, -5.5, -20), 0.25, wither_body),
    Cube(Vector(6.75, -5.5, -20), 0.25, wither_body),
    Cube(Vector(7, -5.5, -20), 0.25, wither_body),
    Cube(Vector(7.25, -5.5, -20), 0.25, wither_body),
    Cube(Vector(7.5, -5.5, -20), 0.25, wither_body),
    Cube(Vector(7.75, -5.5, -20), 0.25, wither_body),
  ]

  # Fondo de pantalla de la imagen generada por el raytracer.
  raytracer.set_envmap(Envmap("./env/desert.bmp"))

  # Renderización y toma de tiempo del programa.
  start = time.time()
  raytracer.render()
  image_path = raytracer.write("./images/scene.bmp")

  # Impresión de resultados.
  print(f"\nRendering process has been finished in {round((time.time() - start), 4)} seconds! Check {image_path}!\n")
