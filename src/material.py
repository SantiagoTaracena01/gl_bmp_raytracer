"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Definición de la clase Material.
class Material(object):

  # Método constructor de la clase Material.
  def __init__(self, diffuse, albedo, spec, refractive_index=0):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec
    self.refractive_index = refractive_index

  def __repr__(self):
    return f"Color {self.diffuse}, Albedo {self.albedo}, Spec {self.spec}, Refractive index {self.refractive_index}"
