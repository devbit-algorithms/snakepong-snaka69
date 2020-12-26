from canvas import Canvas

class Ball:
  def __init__(self,x ,y):
    self.direction = "bottomLeft"
    self._x = x
    self._y = y

  def x(self):
    return self._x
  
  def y(self):
    return self._y
  

  
  def move(self):
    if(self.direction == "bottomRight"):
      self._x += 1
      self._y += 1   

    elif(self.direction == "bottomLeft"):
      self._x -= 1
      self._y += 1  

    elif(self.direction == "topLeft"):
      self._x -= 1
      self._y -= 1  
    
    elif(self.direction == "topRight"):
      self._x += 1
      self._y -= 1  

  def print(self, canvas):
    canvas.draw(self._x, self._y, "o")
    return canvas
  
  def wallCollision(self, canvas):
    if(canvas.getPixel(self._x + 1, self._y) == "#" and canvas.getPixel(self._x , self._y + 1) == "#"):
      self.direction = "topLeft"

    elif(canvas.getPixel(self._x - 1, self._y) == "#" and canvas.getPixel(self._x , self._y - 1) == "#"):
      self.direction = "bottomRight"

    elif(canvas.getPixel(self._x -1, self._y) == "#" and canvas.getPixel(self._x , self._y + 1) == "#"):
      self.direction = "topRight"

    elif(canvas.getPixel(self._x + 1, self._y) == "#" and canvas.getPixel(self._x , self._y - 1) == "#"):
      self.direction = "bottomLeft"
    