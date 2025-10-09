from src.classes.utils.graphic import Graphic
from src.classes.utils.pattern import Pattern
from src.classes.utils.triangle import Triangle
from src.classes.utils.video import Video

# simple example pattern, parameters are segment dimensions of a triangle
triangle_segment_data = (6.5, 6.5, 10.5)
triangle_segment_data = {
    'a-b': 6.5,
    'b-c': 6.5,
    'c-a': 10.5
}

# a triangle is made up of segments and segment lengths, (AB=6.5, BC=6.5, AC=10.5)
# initialize a triangle
g = Graphic()
t = Triangle()
p = Pattern()
v = Video()

# add a segment
for segment in triangle_segment_data:
    print(f"Segment name: {segment}, length: {triangle_segment_data[segment]}")
    #print(triangle_segment_data[segment])
    t.add_segment(segment)

p.add_triangle(triangle_segment_data)

#quit()
try:
    t.calculate_internal_angles(list(triangle_segment_data))
    print(t.angles)
except Exception as e:
    print(e)

# show a turtle window containing the triangle data
g.display_pattern(triangle_segment_data)

#quit()

g.image_height = 3000
g.image_width = 3000
g.iteration_count = g.image_height * g.image_width / 10
g.iteration_count = 100000
g.create_run_id()

print(f"Starting Sierpinski triangle")
g.create_sierpinski_triangle()
print(f"Sierpinski triangle complete")

print(f"Starting FFMPEG conversion")
image_folder = f"C:\\Users\\PC\\Documents\\Source\\two-dimensional-pattern-layout\\src\\output\\images\\{g.run_id}\\"
#image_folder = f"C:\\Users\\PC\\Documents\\Source\\two-dimensional-pattern-layout\\src\\output\\images\\1759952651\\"
v.create_video_with_ffmpeg(
    image_folder,
    "video.mp4",
    24
)
print(f"FFMPEG conversion complete")

quit()
