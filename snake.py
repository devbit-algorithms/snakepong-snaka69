from snakePiece import SnakePiece
from canvas import Canvas
class Snake:
  def __init__(self, x, y):
    # head coords
    self._x = x
    self._y = y
    self.tail = []
    self.tail.append(SnakePiece(self._x, self._y))
    self.tail.append(SnakePiece(self._x + 1, self._y))
    self.tail.append(SnakePiece(self._x + 2, self._y))
    self.tail.append(SnakePiece(self._x + 3, self._y))
    self.tail.append(SnakePiece(self._x + 4, self._y))
        
  def up(self):
    self._y -= 1
    self.shiftTail()

  def down(self):
    self._y += 1
    self.shiftTail()

  
  def left(self):
    self._x -= 1
    self.shiftTail()

  
  def right(self):
    self._x += 1
    self.shiftTail()


  def shiftTail(self):
    newTail = []
    newTail.append(SnakePiece(self._x, self._y))
    newTail.append(SnakePiece(self.tail[0]._x,self.tail[0]._y))
    newTail.append(SnakePiece(self.tail[1]._x,self.tail[1]._y))
    newTail.append(SnakePiece(self.tail[2]._x,self.tail[2]._y))
    newTail.append(SnakePiece(self.tail[3]._x,self.tail[3]._y))
    self.tail = newTail

  def drawSnake(self, canvas):
    self.field = canvas
    for i in self.tail:
      self.field.draw(i._x, i._y, "+")
    return canvas

worm = Snake(2,5)
screen = Canvas(10, 10)
screen = worm.drawSnake(screen)
screen.print()
