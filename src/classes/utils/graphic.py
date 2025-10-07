from PIL import Image, ImageDraw
from datetime import datetime
import random

'''
A pattern is made up of many triangles
'''

class Graphic:
    def __init__(self):
        self.angles = []
        self.arcs = []
        self.points = {}
        self.point_count = 0
        self.segments = []
        self.triangles = []

    def run(self):
        # Create a new blank image (RGB mode, 200x200 pixels, white background)
        img = Image.new('RGB', (200, 200), color='white')

        # Get a drawing object
        draw = ImageDraw.Draw(img)

        # Draw a red rectangle
        draw.rectangle((50, 50, 150, 150), fill='yellow')

        # create an output filename
        directory = 'src/output/images'
        file = 'generated_image'
        timestamp = datetime.now().timestamp()
        filetype = 'png'
        output_file = "{}/{}_{}.{}".format(directory, file, timestamp, filetype)

        # Save the image
        img.save(output_file)

    def create_sierpinski_triangle(self):
        # TODO: generate a sierpinski triangle and save to a file
        image_width = 2000
        image_height = 2000
        iteration_count = 1000000
        vertices = [
            (random.randint(0, image_width), random.randint(0, image_height)),
            (random.randint(0, image_width), random.randint(0, image_height)),
            (random.randint(0, image_width), random.randint(0, image_height))
        ]
        current_location = (0,0)

        # initialize an image and draw
        img = Image.new('RGB', (image_width, image_height), color='white')
        draw = ImageDraw.Draw(img)

        # loop through splitting the difference between current_location and any vertex
        while iteration_count > 0:
            # pick a random vertex
            random_vertex = random.randint(0,len(vertices)-1)

            # calculate new location from current position and random_vertex
            new_location_x = (current_location[0] + vertices[random_vertex][0]) / 2
            new_location_y = (current_location[1] + vertices[random_vertex][1]) / 2

            # draw a point
            draw.point((new_location_x, new_location_y), fill='black')

            # set the current location
            current_location = (new_location_x, new_location_y)

            # decrement the iteration_count var
            iteration_count -= 1

        # create an output filename
        directory = 'src/output/images'
        file = 'generated_image'
        timestamp = datetime.now().timestamp()
        filetype = 'png'
        output_file = "{}/{}_{}.{}".format(directory, file, timestamp, filetype)

        # Save the image
        img.save(output_file)

        # Display the image
        img.show()