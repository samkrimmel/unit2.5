#Sam Krimmel
#2/8/18
#house.py - makes a house

from ggame import *

red = Color(0xff0000,1) #These are colors
green = Color(0x00ff00,1)
blue = Color(0x0000ff,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

houseBase = RectangleAsset(200,200, blackOutline,red)
houseRoof = PolygonAsset([(0,10), (40,10), (20,0)], blackOutline, green)

Sprite(houseBase,(100,200))
Sprite(houseRoof,(80,190))

App().run()
