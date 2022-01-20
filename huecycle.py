from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree()

tree.brightness = 0.1
tree.color = Color('red')

try:
    while True:
        tree.color += Hue(deg=1)
except KeyboardInterrupt:
    tree.close()
