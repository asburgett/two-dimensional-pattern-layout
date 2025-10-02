from src.classes.utils.pattern import Pattern
from src.classes.utils.triangle import Triangle


# simple example pattern, parameters are segment dimensions of a triangle
pattern = (6.5, 6.5, 10.5)

# a triangle is made up of segments and segment lengths, (AB=6.5, BC=6.5, AC=10.5)
# initialize a triangle
t = Triangle()

# add a segment
for segment in pattern:
    print(segment)
    t.add_segment(segment)

t.calculate_internal_angles(list(pattern))
print(t.angles)
quit()
