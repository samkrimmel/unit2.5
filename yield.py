#Sam Krimmel
#3/7/18
#yield.py - displays yield sign

from ggame import *

black = Color(0x000000,1)
yellow = Color(0xffe500,1)

yellowOutline = LineStyle(1,yellow)

triangle = PolygonAsset([(50,50),(100,50),(75,100)], yellowOutline, yellow)

Sprite(triangle,(200,200))

App().run()
