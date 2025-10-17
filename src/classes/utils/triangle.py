from src.config.config import Config
import math
import turtle

'''
A triangle is made up of distance measurements
'''

class Triangle:
    def __init__(self):
        self.angles = []
        self.area = []
        self.radians = []
        self.segments = []
        '''
        self.segments = {
            'a-b': {
                'length': 6.5
            },
            'b-c': {
                'length': 6.5
            },
            'c-a': {
                'length': 10.5
            }
        }
        '''
        #self.segments = {'a-b': 6.5, 'b-c': 6.5, 'c-a': 10.5}
        self.points = {
            'a': {
                'x': 0,
                'y': 0,
                'height': 0
            },
            'b': {
                'x': 0,
                'y': 0,
                'height': 0
            },
            'c': {
                'x': 0,
                'y': 0,
                'height': 0
            },
        }

    def parse_triangle_data(self, triangle):
        #TODO: validate the triangle data
        if type(triangle) is list:
            print(triangle)
        else:
            print(f"Triangle var type is: {type(triangle)}")

    def parse_pattern_data(self, pattern):
        #TODO: validate the pattern data
        if type(pattern) is tuple:
            print(pattern)
        else:
            print(f"Pattern var type is: {type(pattern)}")

    def add_segment_dimension(self, segment_dimension):
        self.segments.append(segment_dimension)
        self.sort_segments()

    def add_segment(self, segment):
        print(segment)
        self.segments.append(segment)
        #self.sort_segments()

    def get_segment_lengths(self, segment):
        return segment['length']

    def get_segments(self):
        print(self.segments)
        return self.segments

    def sort_segments(self):
        self.segments.sort()
        #self.segments.sort(self, None, True)

    def calculate_area(self):
        # area = (side * side * sin(hypotenuse))/2
        # requires self.segments to be populated as a dict
        # TODO: validate the segment data
        if type(self.segments) is dict:
            self.area = (self.segments[0] * self.segments[1] * math.sin(self.radians[2])/2)
            print(self.area)
            return 0
        else:
            print(type(self.segments))
            return 1

    def calculate_heights(self, triangle):
        # hA = (2xArea)/A
        #print(f"Area var type: {type(self.area)}")
        self.heights = [
            ((2*self.area)/self.segments[0]),
            ((2*self.area)/self.segments[1]),
            ((2*self.area)/self.segments[2])
        ]
        #print(f"Heights: {self.heights}")

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