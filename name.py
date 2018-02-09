#Sam Krimmel
#2/9/18
#name.py - displays name in color with background

from ggame import *

name = input('What is your name my friend?')
color = input('Waht is your favourite colour my lad?')
black = Color(0x000000,1)


text = TextAsset(name,fill=, style='bold 60pt Times')

Sprite(text,(450,250))
