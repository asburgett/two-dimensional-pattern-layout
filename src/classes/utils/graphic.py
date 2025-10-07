from PIL import Image, ImageDraw
from datetime import datetime
import os
import random

'''
A pattern is made up of many triangles
'''

class Graphic:
    def __init__(self):
        self.create_run_folder = True
        self.image_height = 0
        self.image_width = 0
        self.iteration_count = 0
        self.run_id = 0
        self.save_sierpinski_iterations = True

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

    def create_run_id(self):
        self.run_id = int(datetime.now().timestamp())

    def create_sierpinski_triangle(self):
        vertices = [
            (random.randint(0, self.image_width), random.randint(0, self.image_height)),
            (random.randint(0, self.image_width), random.randint(0, self.image_height)),
            (random.randint(0, self.image_width), random.randint(0, self.image_height))
        ]
        current_location = (0,0)

        # initialize an image and draw
        img = Image.new('RGB', (self.image_width, self.image_height), color='white')
        draw = ImageDraw.Draw(img)
        directory = 'src/output/images'
        if self.run_id > 0:
            directory += "/" + str(self.run_id)
            os.makedirs(directory, exist_ok=True)
        file = 'generated_image'
        timestamp = datetime.now().timestamp()
        filetype = 'png'
        output_file = "{}/{}_{}.{}".format(directory, file, timestamp, filetype)

        # loop through splitting the difference between current_location and any vertex
        loops = self.iteration_count
        while loops > 0:
            # pick a random vertex
            random_vertex = random.randint(0,len(vertices)-1)

            # calculate new location from current position and random_vertex
            new_location_x = (current_location[0] + vertices[random_vertex][0]) / 2
            new_location_y = (current_location[1] + vertices[random_vertex][1]) / 2

            # draw a point
            draw.point((new_location_x, new_location_y), fill='black')

            # save the image
            if self.save_sierpinski_iterations and loops % 50 == 0:
                #timestamp = datetime.now().timestamp()
                output_file = "{}/{}_{}.{}".format(directory, file, str(self.iteration_count-loops).zfill(25), filetype)
                #print(output_file)
                img.save(output_file)

            # set the current location
            current_location = (new_location_x, new_location_y)

            # output information at an interval
            if loops % 500 == 0:
                print(f"Loops completed: {loops}")

            # decrement the iteration_count var
            loops -= 1
