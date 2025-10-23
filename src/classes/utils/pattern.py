from src.config.config import Config
import math

'''
A pattern is made up of many triangles
a-b
b-c
c-a

c-d
d-e
e-c

f-g
g-h
h-f
'''

class Pattern:
    def __init__(self):
        self.triangles = []
        self.vertices = []

    def add_triangle(self, triangle_data):
        # {'a-b': 6.5, 'b-c': 6.5, 'c-a': 10.5}
        self.triangles.append(triangle_data)
        print(triangle_data)

    def parse_triangle_information(self, data):
        # generate the ancillary data such as vertices from the triangle
        # by splitting the segment names
        vertices = []
        for segment in data:
            vertices.append(segment)
        print(data)

    def plot_pattern_points(self, data):
        # TODO: what's the minimum information needed about the relationship of the triangles to each other
        # to properly plot them preserving their scale and dimension
        print(f"Not enough information to continue...")
        # I need the xy location of C and an angle, or I could use B and C's location somehow shifting the coordinates
        # to calculate the position of D based on (x1+x2)/2?  Does 180-the internal degrees of the C work?


    def parse_points(self, points):
        #data = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h']
        iteration = 0
        while iteration + 2 < len(points):
            print(f"Segment: {points[iteration]} - {points[iteration+1]} - {points[iteration+2]}")
            iteration += 1

    def generate_triangle_segments_from_points(self, points):
        point_count = len(points)
        iteration = 0
        # walk through the points and grab 3 sequentially
        while iteration + 2 < point_count:
            print(f"Segment: {points[iteration]} - {points[iteration + 1]} - {points[iteration + 2]}")
            iteration += 1
        # add a triangle from end to beginning
        print(f"Segment: {points[point_count-2]} - {points[point_count-1]} - {points[0]}")