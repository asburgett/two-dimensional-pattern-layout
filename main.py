from src.classes.utils.graphic import Graphic
from src.classes.utils.pattern import Pattern
from src.classes.utils.triangle import Triangle
from src.classes.utils.video import Video
from src.classes.utils.vision import ComputerVision
from src.config.config import Config

import datetime
import numpy
import os

# simple example pattern, parameters are segment dimensions of a triangle
triangle_segment_data = (6.5, 6.5, 10.5)
triangle_segment_data = {
    'name': 'a-b', 'length': 6.5
},{
    'name': 'b-c', 'length': 6.5
},{
    'name': 'c-a', 'length': 10.5
}

# a triangle is made up of segments and segment lengths, (AB=6.5, BC=6.5, AC=10.5)
# initialize a triangle
c = Config()
g = Graphic()
t = Triangle()
p = Pattern()
v = Video()
vision = ComputerVision()

# TODO: find edges on a test image
#vision.process_image_for_edges("src/input/shift_detent.JPG")

# TODO: test looping over text lists with numpy
# https://www.geeksforgeeks.org/python/python-iterate-through-list-without-using-the-increment-variable/
# Initializing the list
List = ["Geeks", 4, 'Geeks!']
numpy_list = numpy.random.randint(0, 100, size=1_000_000).tolist()
processing_times = []
# Using enumerate()
start_time = datetime.datetime.now().timestamp()
for ele in enumerate(numpy_list):
    print(ele[1], end=" ")
processing_time = datetime.datetime.now().timestamp()-start_time
processing_times.append(processing_time)
print(f"Enumerate completed in: {processing_time}(s)")

# using numpy
start_time = datetime.datetime.now().timestamp()
Array = numpy.array(numpy_list)
for ele in numpy.nditer(Array):
    print(ele, end=" ")
processing_time = datetime.datetime.now().timestamp()-start_time
processing_times.append(processing_time)
print(f"Numpy completed in: {processing_time}(s)")

print(processing_times)
quit()
# display the configuration parameters
print(c.ffmpeg_install_folder)

# add a segment
for segment in triangle_segment_data:
    t.add_segment(segment)

p.add_triangle(triangle_segment_data)

#quit()
try:
    t.calculate_internal_angles(list(triangle_segment_data))
    print(t.angles)
    t.calculate_area()
    print(t.area)
    t.calculate_heights()
    print(t.heights)
except Exception as e:
    print(e)

# show a turtle window containing the triangle data
g.display_pattern(triangle_segment_data)

#quit()

g.image_height = 30000
g.image_width = 30000
g.iteration_count = g.image_height * g.image_width / 10
g.iteration_count = 7500000
g.create_run_id()

# image output vars
image_folder = f"C:\\Users\\PC\\Documents\\Source\\two-dimensional-pattern-layout\\src\\output\\images\\{g.run_id}\\"
video_folder = f"C:\\Users\\PC\\Documents\\Source\\two-dimensional-pattern-layout\\src\\output\\videos\\{g.run_id}\\"

# create the output directories
os.makedirs(image_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)

print(f"Starting Sierpinski triangle")
g.create_sierpinski_triangle(image_folder)
print(f"Sierpinski triangle complete")

print(f"Starting FFMPEG conversion")
#image_folder = f"C:\\Users\\PC\\Documents\\Source\\two-dimensional-pattern-layout\\src\\output\\images\\1759952651\\"
v.create_video_with_ffmpeg(
    image_folder,
    os.path.join(video_folder, "video.mp4"),
    96
)
print(f"FFMPEG conversion complete")

#quit()

# TODO: look at using map() to apply a method to a list and list comprehensions

# Using map with a built-in function
result = list(map(str.upper, ["apple", "banana", "cherry"]))

# Using a list comprehension
squares = [x**2 for x in range(1000)]
