#Sam Krimmel
#2/8/18
#house.py - makes a house

from ggame import *

red = Color(0xff0000,1) #These are colors
green = Color(0x00ff00,1)
blue = Color(0x0000ff,1)
black = Color(0x000000,1)
purple = Color(0xF308F3,1)
badcolor = Color(0x8D6006,1)

blackOutline = LineStyle(1,black)
thicc = LineStyle(4,black)

houseBase = RectangleAsset(200,150, blackOutline,red)
houseRoof = PolygonAsset([(0,60), (250,60), (125,0)], blackOutline, green)
houseDoor = RectangleAsset(20,40, blackOutline, purple)
gdoor = RectangleAsset(60,60, blackOutline, purple)
window = RectangleAsset(30,30, thicc, badcolor)

Sprite(houseBase,(250,200))
Sprite(houseRoof,(225,140))
Sprite(houseDoor,(300,310))
Sprite(gdoor,(360,290))
Sprite(window,(280,230))
Sprite(window,(330,230))
Sprite(window,(380,230))

App().run()
