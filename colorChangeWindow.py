#Max Low
#10-16-17
#colorChangeWindow.py -- every click changes the color

from ggame import *
from random import randint

blue = Color(0x0000FF,1)
yellow =Color(0xFFFF00,1)
green = Color(0x00FF00,1)
red = Color(0xff0000,1)
blueOutline = LineStyle(5,blue)




def mouseClick(event):
    color = randint(1,4)
    if color == 1: 
        Rectangle = RectangleAsset(200,100,blueOutline,blue)
    if color == 2: 
        Rectangle = RectangleAsset(200,100,blueOutline,yellow)
    if color == 3: 
        Rectangle = RectangleAsset(200,100,blueOutline,green)
    if color == 4: 
        Rectangle = RectangleAsset(200,100,blueOutline,red)
    
        
    
        


    Sprite(Rectangle,(75,100))


App().listenMouseEvent('click', mouseClick)
App().run()