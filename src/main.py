from src.classes.utils.pattern import Pattern
from src.classes.utils.triangle import Triangle


# simple example pattern, parameters are segment dimensions of a triangle
pattern = (6.5, 6.5, 10.5)

# a triangle is made up of segments and segment lengths, (AB=6.5, BC=6.5, AC=10.5)
t = Triangle

# a pattern is made up of one or more triangles
p = Pattern

pattern = {
    'segments': {
        '1': {
            'from': 'a',
            'to': 'b',
            'length': 6.5
        },
        '2': {
            'from': 'b',
            'to': 'c',
            'length': 6.5
        },
        '3': {
            'from': 'c',
            'to': 'a',
            'length': 10.5
        }
    }
}

patterns = [pattern]

# define keys for point names
keys = ('a', 'b', 'c')

# loop through the patterns
for data in patterns:
    for value in data:
        print(value)
    #print(data)
