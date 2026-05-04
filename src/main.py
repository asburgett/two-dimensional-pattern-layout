from src.classes.utils.compute import Compute
from src.classes.utils.graphic import Graphic
from src.classes.utils.pattern import Pattern
from src.classes.utils.point import Point
from src.classes.utils.triangle import Triangle
from src.classes.utils.video import Video
from src.classes.utils.vision import ComputerVision
from src.config.config import Config
import src.data.pattern_data as ExamplePatternData

# TODO:  BIG TODO: how can I implement a method of tracking 4 link suspension travel?  Two triangles?

import datetime
import dotenv
import math
import os

# global variables
debug = False

# TODO: how do I use the A, B, and C point slots for guidance on the directionality of the triangle
# EG: 3, 4, 5 is the same triangle in any order, just different orientations

# Thought assumptions:
# A-B is always the base, A-B is determined by observer to be a good semi-symmetrical segment that facilitates the
# measurement process
#
# Scenarios:
# A:    C is outside of base to left
#           A-C is greater than A-B and B-C is greater than A-B and B-C is greater than A-C
scenario_a_triangle = (5, 10, 6)
# B:    C is outside of base to right
#           A-C is greater than A-B and B-C is greater than A-B and B-C is less than A-C
scenario_b_triangle = (5, 6, 10)
# C:    C is inside the base with left orientation
#           A-C is less than A-B and A-C is less than B-C
scenario_c_triangle = (10, 6, 5)
# D:    C is inside the base with right orientation
#           A-C is less than A-B and B-C is less than A-C
scenario_d_triangle = (10, 5, 6)
#
x = (6,10,5) # outside left
y = (6, 5, 10) # outside right


# If C is outside the base to the right, how do I calculate the XY of it?  Heights?  Rotate/Transform?
# If C is outside the base to the left, how do I calculate the XY of it?  Heights?  Rotate/Transform?
# If C is within the base, calculate the point with the normal height calculation method

# Questions:
# How do I do rotations and transformations on the xy plane easily?
p = Point(4.0, 3.0)
q = Point(2.0, 2.0)
theta = math.pi / 2
p_rotated =  p.rotate(p, q, theta)
p.display_point(p_rotated)
quit()

# simple example pattern, parameters are segment dimensions of a triangle
triangle_data = {}
triangle_data['triangle_abc'] = {'a-b': 4+(9/16), 'b-c': 2+(3/4), 'a-c': 3+(17/32)}
triangle_data['triangle_abd'] = {'a-b': 4+(9/16), 'b-d': 2+(3/4), 'a-d': 3+(17/32)}

#print(ExamplePatternData.oil_filter_gasket_pattern.values())
data = []
for triangle in ExamplePatternData.oil_filter_gasket_pattern.values():
    for arc in triangle.values():
        print(f"Angle: {arc}")
        for segment in arc['segments'].keys():
            #print(segment )
            #print(arc['segments'])
            #print(arc['segments'][segment])
            data.append(arc['segments'][segment])
print(data)
#quit()

# do the triangle calculations
for triangle in triangle_data:
    # pull the point labels from the triangle name, eg triangle_abd = points(a, b, d), segments(a-b, b-d, a-d)
    # calculate the angles and save the data
    # calculate the area and save the data
    # calculate the medians and save the data
    # calculate the heights and save the data
    # calculate the inner right triangles and save the data
    print(triangle)
#quit()

# combine the triangles into a pattern

# do the pattern calculations

# display the pattern
#print(triangle_data['triangle_abd']['b-c'])
#quit()

triangle_segment_data = ExamplePatternData.oil_filter_gasket_pattern
for triangle in triangle_data:
    # calculate the angles and save the data
    # calculate the area and save the data
    # calculate the medians and save the data
    # calculate the heights and save the data
    # calculate the inner right triangles and save the data
    print(type(triangle))
#quit()

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
