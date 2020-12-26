from pynput.keyboard import Listener, Key
import time
from threading import Thread



def on_press(key):
    if hasattr(key, 'char'):  # Write the character pressed if available
      print(key.char)

    elif key == Key.up:  # If space was pressed, write a space
      print('up')
    elif key == Key.down:  # If space was pressed, write a space
      print('down')
    elif key == Key.left:  # If space was pressed, write a space
      print('left')
    elif key == Key.right:  # If space was pressed, write a space
      print('right')


while(1):
  with Listener(on_press=on_press) as ls:
    def time_out(period_sec: int):
        time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
        ls.stop()

    Thread(target=time_out, args=(0.1,)).start()
    ls.join()
  print("works")