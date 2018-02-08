#Sam Krimmel
#2/7/18
#graphicsDemo.py - how to use graphics

from ggame import *

red = Color(0xff0000,1) #These are colors
green = Color(0x00ff00,1)
blue = Color(0x0000ff,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200,100,blackOutline,red) #These are shapes
blueCircle = CircleAsset(50,blackOutline,blue)
greenEllipse = EllipseAsset(100,50,blackOutline,green)
blackLine = LineAsset(50,160,blackOutline)
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)],blackOutline,red)

text = TextAsset('BluehEluBEbLhEuHEuh',fill=red, style='bold 40pt Times') #This is text and other options

Sprite(redRectangle) #This is showing them
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,200))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,200))

App().run()