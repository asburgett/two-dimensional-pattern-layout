from src.config.config import Config
import math
import turtle

'''
A triangle is made up of distance measurements
'''

class Triangle:
    def __init__(self):
        self.medians = []
        self.heights = []
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
        if type(self.segments) is list:
            self.area = (self.segments[0]['length'] * self.segments[1]['length'] * math.sin(self.radians[2])/2)
            return 0
        else:
            print(f"'segment' type error: {type(self.segments)}")
            return 1

    def calculate_heights(self):
        # hA = (2xArea)/A
        #print(f"Area var type: {type(self.area)}")
        if len(self.segments) == 3:
            self.heights = [
                ((2 * self.area) / self.segments[0]['length']),
                ((2 * self.area) / self.segments[1]['length']),
                ((2 * self.area) / self.segments[2]['length'])
            ]
            print(f"Heights: {self.heights}")
            return 0
        else:
            print(f"'triangle' type error")
            return 1

    def calculate_internal_angles(self, triangle):
        if type(triangle) is list:
            a = math.acos(((pow(float(triangle[1]['length']), 2) + pow(float(triangle[2]['length']), 2) - pow(float(triangle[0]['length']), 2)) / (
                    2 * float(triangle[1]['length']) * float(triangle[2]['length']))))
            b = math.acos(((pow(float(triangle[0]['length']), 2) + pow(float(triangle[2]['length']), 2) - pow(float(triangle[1]['length']), 2)) / (
                    2 * float(triangle[0]['length']) * float(triangle[2]['length']))))
            c = math.acos(((pow(float(triangle[0]['length']), 2) + pow(float(triangle[1]['length']), 2) - pow(float(triangle[2]['length']), 2)) / (
                    2 * float(triangle[0]['length']) * float(triangle[1]['length']))))
            self.radians = [a, b, c]
        else:
            print("Invalid data in triangle definition")

        if self.radians:
            self.angles = [math.degrees(a), math.degrees(b), math.degrees(c)]
            return 0
        else:
            return 1
    
    def calculate_medians(self):
        median_a = math.sqrt(
                pow((self.segments[0]['length'] / 2), 2) +
                pow(self.segments[2]['length'], 2) - (
                    (self.segments[0]['length'] * self.segments[2]['length']) * math.cos(self.radians[1])
                )
        )

        median_b = math.sqrt(
            pow((self.segments[1]['length'] / 2), 2) +
            pow(self.segments[0]['length'], 2) - (
                    (self.segments[0]['length'] * self.segments[1]['length']) * math.cos(self.radians[2])
            )
        )

        median_c = math.sqrt(
            pow((self.segments[2]['length'] / 2), 2) +
            pow(self.segments[1]['length'], 2) - (
                    (self.segments[1]['length'] * self.segments[2]['length']) * math.cos(self.radians[0])
            )
        )

        self.medians = [median_a, median_b, median_c]
        print(f"Medians: {self.medians}")

    def calculate_inner_right_triangles(self):
        # total length on x = segment c, aka the left of the base to the 3rd vertex along x axis
        #A = self.heights[2]
        #C = self.segments[2]
        b = math.sqrt(pow(self.segments[1]['length'], 2) - pow(self.heights[2], 2))
        self.heights.append(b)
        print(f"Height of 3rd point from x-axis: {b}")
        print(f"Remainder: {self.segments[2]['length'] - b}")
        return b