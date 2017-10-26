#Max Low
#10-26-17
#bubbles.py -- random location and radius for bubbles

from random import randint
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
yellow =Color(0xFFFF00,1)
black = Color(0x000000,1)
blackOutline = LineStyle(5,black) # (pixels,colors)


def mouseClick(event):
    bubbles = randint(5,20)
    for i in range(bubbles):
        radius = randint(10,100)
        randcolor = randint(1,5)
        if randcolor == 1:
            Circle = CircleAsset(radius,blackOutline,red) 
        if randcolor == 2:
            Circle = CircleAsset(radius,blackOutline,green)
        if randcolor == 3:
            Circle = CircleAsset(radius,blackOutline,blue)
        if randcolor == 4:
            Circle = CircleAsset(radius,blackOutline,yellow)
        if randcolor == 5:
            Circle = CircleAsset(radius,blackOutline,black)
        x = randint(100,900)
        y = randint(100,400)
        Sprite(Circle,(x,y))


App().listenMouseEvent('click', mouseClick)
App().run()