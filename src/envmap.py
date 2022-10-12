from color import Color
import numpy
import mmap
import struct
import math

class Envmap(object):
  def __init__(self, path):
    self.path = path
    self.__read()
    
  def __read(self):
    with open(self.path) as image:
      m = mmap.mmap(image.fileno(), 0, access=mmap.ACCESS_READ)
      ba = bytearray(m)
      header_size = struct.unpack("=l", ba[10 : 14])[0]
      self.width = struct.unpack("=l", ba[18 : 22])[0]
      self.height = struct.unpack("=l", ba[22 : 26])[0]
      all_bytes = ba[header_size::]
      self.pixels = numpy.frombuffer(all_bytes, dtype="uint8")
      
  def get_color(self, direction):
    direction = direction.norm()
    x = (round(math.atan2(direction.z, direction.x) / (2 * math.pi) + 0.5) * self.width)
    y = (round(math.acos((-1 * direction.y)) / math.pi) * self.height)
    index = ((y * self.width + x) * 3) % len(self.pixels)
    c = self.pixels[index:(index + 3)].astype(numpy.uint8)
    return Color(c[2], c[1], c[0])
