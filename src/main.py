"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

from ray import Raytracer
from vector import Vector
from sphere import Sphere
import utils
import time

if __name__ == "__main__":

  raytracer = Raytracer(600, 600)
  raytracer.background_color = utils.color(0, 0, 50)

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

  for part in snowman:
    for sphere in part["spheres"]:
      raytracer.objects.append(sphere)  
      raytracer.colors.append(part["color"])

  start = time.time()
  raytracer.render()
  raytracer.write("./images/snowman.bmp")

  print("\nRendering process has been finished! Check ./images/<your result>.bmp!")
  print(f"Finished in {round((time.time() - start), 4)} seconds.\n")
