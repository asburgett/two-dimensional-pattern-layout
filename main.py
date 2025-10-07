from src.classes.utils.graphic import Graphic
from src.classes.utils.pattern import Pattern
from src.classes.utils.triangle import Triangle
from src.classes.utils.video import Video



# simple example pattern, parameters are segment dimensions of a triangle
pattern_data = (6.5, 6.5, 10.5)

# a triangle is made up of segments and segment lengths, (AB=6.5, BC=6.5, AC=10.5)
# initialize a triangle
g = Graphic()
t = Triangle()
p = Pattern()
v = Video()

# add a segment
for segment in pattern_data:
    print(segment)
    t.add_segment(segment)

try:
    t.calculate_internal_angles(list(pattern_data))
    print(t.angles)
except Exception as e:
    print(e)

g.iteration_count = 1000000
g.image_height = 3000
g.image_width = 3000
g.create_run_id()

print(f"Starting Sierpinski triangle")
g.create_sierpinski_triangle()
print(f"Sierpinski triangle complete")

print(f"Starting FFMPEG conversion")
image_folder = f"C:\\Users\\PC\\Documents\\Source\\two-dimensional-pattern-layout\\src\\output\\images\\{g.run_id}\\"
#image_folder = f"C:\\Users\\PC\\Documents\\Source\\two-dimensional-pattern-layout\\src\\output\\images\\1759858245\\"
v.create_video_with_ffmpeg(
    image_folder,
    "video.mp4",
    1024
)
print(f"FFMPEG conversion complete")

quit()
