#Max Low
#10-16-17
#colorChangeWindow.py -- every click changes the color

from ggame import *
from random import randint

1 = Color(0x0000FF,1)
2 =Color(0xFFFF00,1)
3 = Color(0x00FF00,1)
4 = Color(0xff0000,1)

def mouseClick(event):
    color = randint(1,4)
    Rectangle = RectangleAsset(200,100,blackOutline,randint)
        


Sprite(Rectangle,(75,100))


App().listenMouseEvent('click', mouseClick)
App().(run)