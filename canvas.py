import os

class Canvas:
  def __init__(self, height, width):
    self.height = height
    self.width = width
    self.canvas = [[' ' for x in range(width)] for y in range(height)]
    self.clear()

  def clear(self):
    for y in range(self.height):
      for x in range(self.width):
        self.canvas[y][x] = ' '

  def draw(self, x, y, value):
    self.canvas[y][x] = value

  def print(self):
    os.system('clear')
    field = ""
    for y in range(self.height):
      for x in range(self.width):
        field += self.canvas[y][x]
      field += "\n"
    print(field)
  
  def getCanvas(self):
    os.system('clear')
    field = ""
    for y in range(self.height):
      for x in range(self.width):
        field += self.canvas[y][x]
      field += "\n"
    return field
  
  def createBorder(self):
    for y in range(self.height):
      for x in range(self.width):
        if (x == 0 or y == 0 or x == self.width-1 or y == self.height-1):
          self.draw(x,y, "#")

  def getPixel(self, x, y):
    return self.canvas[y][x]

  def getHeight(self):
    return self.height

  def getWidth(self):
    return self.width