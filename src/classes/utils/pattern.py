import math

'''
A pattern is made up of many triangles
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