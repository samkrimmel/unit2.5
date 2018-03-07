#Sam Krimmel
#3/7/18
#yield.py - displays yield sign

from ggame import *

black = Color(0x000000,1)
yellow = Color(0xffe500,1)

yellowOutline = LineStyle(1,yellow)
blackOutline = LineStyle(4,black)
triangle = PolygonAsset([(0,0),(300,0),(150,250)], yellowOutline, yellow)
triangle2 = PolygonAsset([(50,50),(250,50),(150,200)], blackOutline, yellow)

Sprite(triangle,(200,150))
Sprite(tirangle2,(200,150))
App().run()
