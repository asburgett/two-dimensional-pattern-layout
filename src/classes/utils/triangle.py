import math
import turtle

'''
A triangle is made up of distance measurements
'''

class Triangle:
    def __init__(self):
        self.angles = []
        self.radians = []
        self.segments = []

    def parse_triangle_data(self, triangle):
        if type(triangle) is list:
            print(triangle)

    def add_segment_dimension(self, segment_dimension):
        self.segments.append(segment_dimension)
        self.sort_segments()

    def add_segment(self, segment):
        self.segments.append(segment)
        self.sort_segments()

    def get_segments(self):
        print(self.segments)
        return self.segments

    def sort_segments(self):
        self.segments.sort()

    def calculate_internal_angles(self, triangle):
        if type(triangle) is list:
            a = math.acos(((pow(float(triangle[1]), 2) + pow(float(triangle[2]), 2) - pow(float(triangle[0]), 2)) / (
                    2 * float(triangle[1]) * float(triangle[2]))))
            b = math.acos(((pow(float(triangle[0]), 2) + pow(float(triangle[2]), 2) - pow(float(triangle[1]), 2)) / (
                    2 * float(triangle[0]) * float(triangle[2]))))
            c = math.acos(((pow(float(triangle[0]), 2) + pow(float(triangle[1]), 2) - pow(float(triangle[2]), 2)) / (
                    2 * float(triangle[0]) * float(triangle[1]))))
            self.radians = [a, b, c]
        else:
            print("Invalid data in triangle definition")

        if self.radians:
            self.angles = [math.degrees(a), math.degrees(b), math.degrees(c)]
            return 0
        else:
            return 1