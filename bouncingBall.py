#Max Low
#10-26-17
#bouncingBall.py -- 


from random import randint
from ggame import *

red = Color(0xFF0000,1)
blackOutline = LineStyle(5,black) # (pixels,colors)
Circle = CircleAsset(radius,blackOutline,red) 

Sprite(Circle,(x,y))

App().run()