from src.classes.utils.pattern import Pattern
from src.classes.utils.triangle import Triangle


# simple example pattern, parameters are segment dimensions of a triangle
pattern_data = (6.5, 6.5, 10.5)

# a triangle is made up of segments and segment lengths, (AB=6.5, BC=6.5, AC=10.5)
# initialize a triangle
t = Triangle()
p = Pattern()

# add a segment
for segment in pattern_data:
    print(segment)
    t.add_segment(segment)

try:
    t.calculate_internal_angles(list(pattern_data))
    print(t.angles)
except Exception as e:
    print(e)

quit()
