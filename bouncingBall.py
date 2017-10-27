#Max Low
#10-26-17
#bouncingBall.py -- 


from random import randint
from ggame import *

red = Color(0xFF0000,1)
black = Color(0xFFFFFF,1)
blackOutline = LineStyle(5,black) # (pixels,colors)
Circle = CircleAsset(50,blackOutline,red) \

def movecircle():
    x = step
    y = step
    Sprite(Circle,(x,y))
    
while True:
    movecircle()

App().run(step)