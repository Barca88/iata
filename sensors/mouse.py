
from pynput.mouse import Listener

import math


# detect mouse move
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


# detect mouse click

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))


# detect mouse scroll
def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0},  {1})({2},  {3})'.format(x, y, dx, dy))


# Collect events
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
