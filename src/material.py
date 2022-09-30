"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Definición de la clase Material.
class Material(object):

  # Método constructor de la clase Material.
  def __init__(self, diffuse, albedo, spec):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec
