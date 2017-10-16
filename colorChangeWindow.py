#Max Low
#10-16-17
#colorChangeWindow.py -- every click changes the color

from ggame import *
from random import randint

red = Color(0xff0000,1)

def mouseClick(event):
    



App().listenMouseEvent('click', mouseClick)
App.(run)