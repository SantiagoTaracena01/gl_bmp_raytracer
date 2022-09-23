"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

from ray import Raytracer

if __name__ == "__main__":
  raytracer = Raytracer(800, 600)
  raytracer.point(400, 300)
  raytracer.render()
  print("Hello Raytracer!")
