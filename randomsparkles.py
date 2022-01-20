from tree import RGBXmasTree
import random

tree = RGBXmasTree()

tree.brightness = 0.1
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

try:
    while True:
        pixel = random.choice(tree)
        pixel.color = random_color()
except KeyboardInterrupt:
    tree.close()
