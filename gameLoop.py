from pynput.keyboard import Listener, Key
import time
from threading import Thread
from canvas import Canvas
from snake import Snake
import os


def on_press(key):
    if hasattr(key, 'char'):  # Write the character pressed if available
      print(key.char)

    elif key == Key.up:  # If space was pressed, write a space
      print('up')
      snake.up()
    elif key == Key.down:  # If space was pressed, write a space
      print('down')
      snake.down()

    elif key == Key.left:  # If space was pressed, write a space
      print('left')
      snake.left()

    elif key == Key.right:  # If space was pressed, write a space
      print('right')
      snake.right()
    

canvas = Canvas(20, 30)
snake = Snake(10, 5)    
snake.left()
while(1):
  with Listener(on_press=on_press) as ls:
    def time_out(period_sec: int):
        time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
        ls.stop()
        os.system('cls' if os.name == 'nt' else 'clear')


    Thread(target=time_out, args=(1,)).start()
    ls.join()
    snake.move()
    canvas.clear()
    canvas.createBorder()
    canvas = snake.drawSnake(canvas)
    canvas.print()
    

    
