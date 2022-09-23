"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

from ray import Raytracer
from vector import Vector
from sphere import Sphere

if __name__ == "__main__":

  raytracer = Raytracer(600, 600)
  raytracer.set_ray_probability(0.1)

  raytracer.objects = [
    Sphere(Vector(0, -4, -20), 2),
    Sphere(Vector(0, 0, -20), 3),
  ]

  raytracer.render()
  raytracer.write()

  print("\nRendering process has been finished! Check ./images/<your result>.bmp!\n")
