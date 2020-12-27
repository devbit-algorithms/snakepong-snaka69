from canvas import Canvas

class Ball:
  def __init__(self,x ,y):
    self.direction = "bottomLeft"
    self._x = x
    self._y = y
    self.score = 0
    self.gameOver = False

  def x(self):
    return self._x
  
  def y(self):
    return self._y
  
  def getScore(self):
    return self.score
  
  def getgameOver(self):
    return self.gameOver
  
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
  

  def collision(self, canvas):
    self.wallCollision(canvas)
    self.pedalCollision(canvas)
    self.snakeCollision(canvas)

  def wallCollision(self, canvas):
    if(canvas.getPixel(self._x + 1, self._y) == "#" and canvas.getPixel(self._x , self._y + 1) == "#"):
      self.direction = "topLeft"
      self.gameOver = True

    elif(canvas.getPixel(self._x - 1, self._y) == "#" and canvas.getPixel(self._x , self._y - 1) == "#"):
      self.direction = "bottomRight"
      self.score += 1

    elif(canvas.getPixel(self._x -1, self._y) == "#" and canvas.getPixel(self._x , self._y + 1) == "#"):
      self.direction = "topRight"
      self.score += 1

    elif(canvas.getPixel(self._x + 1, self._y) == "#" and canvas.getPixel(self._x , self._y - 1) == "#"):
      self.direction = "bottomLeft"
      self.gameOver = True

    #sides
    #bottom
    elif(canvas.getPixel(self._x, self._y + 1) == "#"):
      if(self.direction == "bottomLeft"):
        self.direction = "topLeft"
      else:
        self.direction = "topRight"
    #top
    elif(canvas.getPixel(self._x, self._y - 1) == "#"):
      if(self.direction == "topLeft"):
        self.direction = "bottomLeft"
      else:
        self.direction = "bottomRight"

    #left
    elif(canvas.getPixel(self._x - 1, self._y) == "#"):
      self.score += 1
      if(self.direction == "bottomLeft"):
        self.direction = "bottomRight"
      else:
        self.direction = "topRight"
    #right
    elif(canvas.getPixel(self._x + 1, self._y) == "#"):
      self.gameOver = True
      if(self.direction == "bottomRight"):
        self.direction = "bottomLeft"
      else:
        self.direction = "topLeft"

  def pedalCollision(self, canvas):
    if(canvas.getPixel(self._x - 1, self._y - 1) == "|"):
      self.direction = "topRight"
    elif(canvas.getPixel(self._x - 1, self._y + 1) == "|"):
      self.direction = "bottomRight"

  def snakeCollision(self, canvas):
    if(self.direction == "bottomRight" and (canvas.getPixel(self._x + 1, self._y + 1) == "+")):
      if((canvas.getPixel(self._x, self._y + 1) == "+") or (canvas.getPixel(self._x + 2 , self._y + 1)) == "+"):
        #horizontal
        self.direction = "topRight"
      elif(canvas.getPixel(self._x + 1, self._y) == "+"  or (canvas.getPixel(self._x + 1 , self._y + 2)) == "+"):
        self.direction = "bottomLeft"
      else:
        self.direction = "topLeft"
    
    elif(self.direction == "topLeft" and (canvas.getPixel(self._x - 1, self._y - 1) == "+")):
      if((canvas.getPixel(self._x, self._y - 1) == "+") or (canvas.getPixel(self._x - 2 , self._y - 1)) == "+"):
        self.direction = "bottomLeft"
      elif(canvas.getPixel(self._x - 1, self._y) == "+"  or (canvas.getPixel(self._x - 1 , self._y - 2)) == "+"):
        self.direction = "topRight"
      else:
        self.direction = "bottomRight"
    
    elif(self.direction == "topRight" and (canvas.getPixel(self._x + 1, self._y - 1) == "+")):
      if((canvas.getPixel(self._x, self._y - 1) == "+") or (canvas.getPixel(self._x + 2 , self._y - 1)) == "+"):
        self.direction = "bottomRight"
      elif(canvas.getPixel(self._x + 1 , self._y) == "+"  or (canvas.getPixel(self._x + 1 , self._y - 2)) == "+"):
        self.direction = "topLeft"
      else:
        self.direction = "bottomLeft"
    
    elif(self.direction == "bottomLeft" and (canvas.getPixel(self._x - 1, self._y + 1) == "+")):
      if((canvas.getPixel(self._x, self._y + 1) == "+") or (canvas.getPixel(self._x - 2 , self._y + 1)) == "+"):
        self.direction = "topLeft"
      elif(canvas.getPixel(self._x - 1 , self._y) == "+"  or (canvas.getPixel(self._x - 1 , self._y - 2)) == "+"):
        self.direction = "bottomRight"
      else:
        self.direction = "topRight"




  


