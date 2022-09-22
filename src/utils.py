"""
Universidad del Valle de Guatemala
(CC2018) Gráficos por Computadora
Santiago Taracena Puga (20017)
"""

# Módulos necesarios
import struct

# Funciones extra utilizadas.
color = lambda r, g, b: bytes([b, g, r])
char = lambda character: struct.pack("=c", character.encode("ascii"))
word = lambda word: struct.pack("=h", word)
dword = lambda dword: struct.pack("=l", dword)

# Constantes extra utilizadas.
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
RED = color(255, 0, 0)
GREEN = color(0, 255, 0)
BLUE = color(0, 0, 255)
