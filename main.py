from src.classes.utils.compute import Compute
from src.classes.utils.graphic import Graphic
from src.classes.utils.pattern import Pattern
from src.classes.utils.triangle import Triangle
from src.classes.utils.video import Video
from src.classes.utils.vision import ComputerVision
from src.config.config import Config

import datetime
import dotenv
import os

# global variables
debug = False

# simple example pattern, parameters are segment dimensions of a triangle
triangle_segment_data = (6.5, 6.5, 10.5)
triangle_segment_data = ({
    'name': 'a-b', 'length': 6.5
},{
    'name': 'b-c', 'length': 6.5
},{
    'name': 'c-a', 'length': 10.5
})

'''
triangle_segment_data = ({
    'name': 'a-b', 'length': 6.5
},{
    'name': 'b-c', 'length': 6.5
},{
    'name': 'c-a', 'length': 10.5
},{
    'name': 'c-d', 'length': 6.5
},{
    'name': 'd-b', 'length': 10.5
},{
    'name': 'd-e', 'length': 6.5
},{
    'name': 'e-c', 'length': 10.5
})
'''

# a triangle is made up of segments and segment lengths, (AB=6.5, BC=6.5, AC=10.5)
# initialize a triangle
compute = Compute()
c = Config()
g = Graphic()
t = Triangle()
p = Pattern()
v = Video()
vision = ComputerVision()

# display some configuration parameters
if debug:
    print(f"FFMPEG install folder: {c.ffmpeg_install_folder}")
    print(f"FFMPEG version: {v.get_ffmpeg_version()}")
    print(f"OpenCV version: {vision.get_installed_version()}")

# add a segment
for segment in triangle_segment_data:
    t.add_segment(segment)

try:
    t.calculate_internal_angles(list(triangle_segment_data))
    print(t.angles)
    t.calculate_area()
    print(t.area)
    t.calculate_medians()
    print(t.medians)
    t.calculate_heights()
    print(t.heights)
    t.calculate_inner_right_triangles()
    print(t.heights)

    # TODO: how do I properly transform the xy location to apply the next triangle of bcd?
    # If all triangles relate to one point (a: 0,0), orientation is maintained as long as the x axis as segment a-c
    # is used to determine direction of the triangle?
    result = t.rotate_point((7.5, 7.5), (5.25, 3.38), 90)
    print(result)
except Exception as e:
    print(e)

# show a turtle window containing the triangle data
#g.display_pattern(triangle_segment_data)
g.display_pattern(t)

quit()

# TODO: look at using map() to apply a method to a list and list comprehensions

# Using map with a built-in function
result = list(map(str.upper, ["apple", "banana", "cherry"]))

# Using a list comprehension
squares = [x**2 for x in range(1000)]
