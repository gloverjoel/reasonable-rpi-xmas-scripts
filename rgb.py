from tree import RGBXmasTree
from colorzero import Color
from time import sleep

tree = RGBXmasTree()

tree.brightness = 0.1
colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

try:
    while True:
        for color in colors:
            tree.color = color
            sleep(1)
except KeyboardInterrupt:
    tree.close()
