from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

tree.brightness = 0.1
colors = [Color('green')] # add more if you like

try:
    while True:
        for color in colors:
            for pixel in tree:
                pixel.color = color
except KeyboardInterrupt:
    tree.close()
