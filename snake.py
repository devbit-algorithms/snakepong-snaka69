from entity import Entity
from canvas import Canvas
class Snake:
  def __init__(self, x, y):
    # head coords
    self.direction = "left"
    self.prevDirection = "left"
    self.moveCount = 0
    self._x = x
    self._y = y
    self.tail = []
    self.tail.append(Entity(self._x, self._y))
    self.tail.append(Entity(self._x + 1, self._y))
    self.tail.append(Entity(self._x + 2, self._y))
    self.tail.append(Entity(self._x + 3, self._y))
    self.tail.append(Entity(self._x + 4, self._y))
    self.tail.append(Entity(self._x + 5, self._y))
    self.tail.append(Entity(self._x + 6, self._y))
    self.oldTail = self.tail
        
  def up(self):
    if(self.prevDirection != "down"):
      self.direction = "up"

  def down(self):
    if(self.prevDirection != "up"):
      self.direction = "down"

  
  def left(self):
    if(self.prevDirection != "right"):
      self.direction = "left"

  def right(self):
    if(self.prevDirection != "left"):
      self.direction = "right"


  def shiftTail(self):
    newTail = []
    newTail.append(Entity(self._x, self._y))
    newTail.append(Entity(self.tail[0]._x,self.tail[0]._y))
    newTail.append(Entity(self.tail[1]._x,self.tail[1]._y))
    newTail.append(Entity(self.tail[2]._x,self.tail[2]._y))
    newTail.append(Entity(self.tail[3]._x,self.tail[3]._y))
    newTail.append(Entity(self.tail[4]._x,self.tail[4]._y))
    newTail.append(Entity(self.tail[5]._x,self.tail[5]._y))
    self.oldTail = self.tail
    self.oldTail.pop(0)
    self.tail = newTail
    

  def drawSnake(self, canvas):
    self.field = canvas
    for i in self.tail:
      self.field.draw(i._x, i._y, "+")
    return canvas

  def move(self):

    if(self.direction == "right"):
      self._x += 1
      self.prevDirection = "right"

    elif(self.direction == "left"):
      self._x -= 1
      self.prevDirection = "left"


    elif(self.direction == "up"):
      self._y -= 1
      self.prevDirection = "up"


    elif(self.direction == "down"):
      self._y += 1
      self.prevDirection = "down"
    self.shiftTail()
  
  def detectColission(self, canvas):
    if(canvas.getPixel(self._x, self._y) == "#" or (self.tailCollission())):
      return True
    return False
  
  def tailCollission(self):
    for i in self.oldTail:
      if(self._x == i._x and self._y == i._y ):

        return True
    return False