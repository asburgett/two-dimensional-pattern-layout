import math

'''
A pattern is made up of many triangles
'''

class Pattern:
    def __init__(self):
        self.angles = []
        self.arcs = []
        self.points = {}
        self.point_count = 0
        self.segments = []
        self.triangles = []