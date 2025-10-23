front_hub_triangle = (6.5, 6.5, 10.5)
rear_hub_triangle = (7.3125, 7.3125, 11.875)
steering_box_triangle = (2+(9/16), 4+(1/8), 5+(9/16))
front_spindle_pattern = (
    {'a-b': 0, 'b-c': 0, 'c-a': 0},
    {'c-d': 0, 'd-e': 0, 'e-c': 0},
    {'d-e': 0, 'e-f': 0, 'f-d': 0}
)
front_timing_cover_pattern = (
    { 'segment': 'a-b', 'length': 7.25 },
    { 'segment': 'b-c', 'length': 8.25 },
    { 'segment': 'c-a', 'length': 3 + (29/32) },

    { 'segment': 'b-c', 'length': 8.25 },
    { 'segment': 'c-d', 'length': 7.25 },
    { 'segment': 'b-d', 'length': 3 + (29/32) },

    { 'segment': 'e-d', 'length': 3 + (3/16) },
    { 'segment': 'e-c', 'length': 5 + (15/16) },
    { 'segment': 'c-d', 'length': 7.25 },

    { 'segment': 'e-c', 'length': 5 + (15 / 16) },
    { 'segment': 'e-f', 'length': 5 + (1/16) },
    { 'segment': 'f-c', 'length': 5 + (15/16) },

    { 'segment': 'f-g', 'length': 5 + (7/8) },
    { 'segment': 'e-g', 'length': 4 + (1/8) },
    { 'segment': 'e-f', 'length': 5 + (1/16) },

    { 'segment': 'f-g', 'length': 5 + (7/8) },
    { 'segment': 'g-h', 'length': 6 },
    { 'segment': 'h-f', 'length': 1 + (1/16) },

    {'segment': 'g-h', 'length': 6 },
    {'segment': 'h-i', 'length': 2 + (5/8) },
    {'segment': 'i-g', 'length': 7 + (5/8) },

    { 'segment': 'g-i', 'length': 7 + (5/8) },
    { 'segment': 'i-j', 'length': 9 + (13/32) },
    { 'segment': 'g-j', 'length': 8 + (1/16) },

    {'segment': 'j-k', 'length': 2 + (5/8) },
    {'segment': 'k-g', 'length': 6 + (7/32) },
    {'segment': 'g-j', 'length': 8 + (1/16) },

    {'segment': 'k-l', 'length': 1 + (1/16)},
    {'segment': 'l-g', 'length': 6 + (7/32)},
    {'segment': 'g-k', 'length': 6 + (7/32) },

    {'segment': 'l-m', 'length': 5 + (7 / 8)},
    {'segment': 'm-k', 'length': 6 + (7 / 16)},
    {'segment': 'k-l', 'length': 1 + (1/16)},

    {'segment': 'l-m', 'length': 5 + (7 / 8)},
    {'segment': 'm-o', 'length': 4 + (1 / 16)},
    {'segment': 'o-l', 'length': 8 + (1 / 16)},

    {'segment': 'm-n', 'length': 5 + (7 / 8)},
    {'segment': 'n-o', 'length': 4 + (1 / 16)},
    {'segment': 'o-m', 'length': 8 + (1 / 16)},

    {'segment': 'n-p', 'length': 3 + (15 / 16)},
    {'segment': 'p-o', 'length': 8 + (1 / 4)},
    {'segment': 'o-n', 'length': 8 + (1 / 16)},

    {'segment': 'p-q', 'length': 5 + (7 / 8)},
    {'segment': 'q-o', 'length': 4 + (1 / 16)},
    {'segment': 'o-p', 'length': 8 + (1 / 16)},

    {'segment': 'n-q', 'length': 8 + (3 / 8)},
    {'segment': 'q-o', 'length': 4 + (1 / 16)},
    {'segment': 'o-n', 'length': 8 + (1 / 16)},

    {'segment': 'a-q', 'length': 20 + (1 / 8)}
)