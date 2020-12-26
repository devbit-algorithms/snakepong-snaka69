from entity import Entity
from canvas import Canvas

class Pedal:
  def __init__(self,x ,y):
    self.direction = "up"
    self.pedal = []
    self._x = x
    self._y = y
    self.pedal.append(Entity(self._x, self._y))
    self.pedal.append(Entity(self._x, self._y-1))
    self.pedal.append(Entity(self._x, self._y-2))
    self.pedal.append(Entity(self._x, self._y+1))
    self.pedal.append(Entity(self._x, self._y+2))


  def up(self):
    for i in self.pedal:
      i.setY(i.y() - 1)
    self._y -= 1

  def down(self):
    for i in self.pedal:
      i.setY(i.y() + 1)
    self._y += 1
  
  def print(self, canvas):

    for i in self.pedal:
      canvas.draw(i.x(), i.y(), "|")
    return canvas
  
  def move(self, canvas):
    print(self._y)
    print(canvas.getHeight())
    if(canvas.getPixel(self._x, self._y + 3) == "#"):
      
      self.direction = "up"
    elif(self._y - 3 <=0):
      self.direction = "down"

    if(self.direction == "up"):
      self.up()
    else:
      self.down()

