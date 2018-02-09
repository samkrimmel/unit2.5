#Sam Krimmel
#2/9/18
#germany.py - prints the german flag

from ggame import *

black = Color(0x000000,1)
red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(0,black)

top = RectangleAsset(300,60, blackOutline, black)
middle = RectangleAsset(300,60, blackOutline, red)
bottom = RectangleAsset(300,60, blackOutline, yellow)

Sprite(top,(0,0))
Sprite(middle,(0,60))
Sprite(bottom,(0,120))

App().run()