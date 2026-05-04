# two-dimensional-pattern-layout
performs various visualization operations on physical pattern datasets made up of point to point dimensional data in the
form of segments and arcs (a-b, b-c, a-c) -> ∠abc

If I plot the pattern triangles with xy, but a tracking triangle on yx, I can plot the pattern?

Their relation to each other doesn't matter at all?  If I have to track an additional triangle to a stationary point,
why not just track all the points from two stationary points?  Eg: measure the distance from 0,0 to the point, then the
distance from 100,0 to the point.  In the field, lay an appropriate sized square along an edge of a pattern, choose two
points on an axis to measure from (0,0 and 100,0 in the example), using a compass measure the distance from each of
those points to the point in question.  Knowledge of the axis being measured from will allow graphic recreations.

a=0,0
b=10,0

a-b=10
a-c=6.5
b-c=4.5

∠abc = 
data = {
    'triangles': {
        'abc': {
            segments:
                {
                    'a-b': 10,
                    'b-c': 4.5,
                    'a-c': 6.5
                },
            angles:
                {
                    'a-b': 128,
                    'b-c': 101,
                    'a-c': 101
                },
            points:
                {
                    'a': (0,0),
                    'b': (10,0),
                    'c': (?,?) // calculated
            }
        }
    }
}
