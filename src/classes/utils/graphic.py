from datetime import datetime
from PIL import Image, ImageDraw

import src
from src.classes.utils.triangle import Triangle
from src.config.config import Config
import os
import random
import turtle

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
        img = Image.new('RGB', (10, 10), color='white')

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

    def sort_pattern_data_by_value(self, pattern_data, sort_reverse=False):
        sorted_items = sorted(pattern_data.items(), key=lambda item: item[1], reverse=sort_reverse)
        return dict(sorted_items)

    def display_pattern(self, pattern_data):
        # setup the turtle instance, screen dimensions, and pen settings
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setup(.5, .5)
        t.pensize(2)
        t.pencolor("red")

        # test data type or assert
        if type(pattern_data) is dict:
            # sort the sides descending or work backwords when sorted ascending
            pattern_data = self.sort_pattern_data_by_value(pattern_data, True)

            # layout the pattern on the screen with long side at base
            # Long segment: (0,0)(10.5,0)
            # Next segment: (10.5,0)(?, ?)
            # Last segment: (10.5,0)(?, ?)
        elif type(pattern_data) is src.classes.utils.triangle.Triangle:
            print(pattern_data.angles)
        else:
            print(f"Error with pattern_data var type: {type(pattern_data)}")

        # TODO: update the pattern data with some new information
        #pattern_data['a']
        print(f"Pattern data: {pattern_data.heights}")
        #quit()

        # show the turtle screen
        t.showturtle()
        scaler = 30

        # goto point A at origin (0,0)
        t.goto(0, 0)
        t.setheading(0)
        t.pendown()

        # go to point C
        t.goto(pattern_data.segments[2]['length'] * scaler, 0 * scaler)

        t.pencolor("blue")

        # go to point b
        t.goto(pattern_data.heights[3] * scaler, pattern_data.heights[2] * scaler)

        t.pencolor("black")

        # back to point a, at origin
        t.goto(0 * scaler, 0 * scaler)

        screen.exitonclick()

    def create_run_id(self):
        self.run_id = int(datetime.now().timestamp())

    def create_sierpinski_triangle(self, image_output_folder):
        vertices = [
            (random.randint(0, self.image_width), random.randint(0, self.image_height)),
            (random.randint(0, self.image_width), random.randint(0, self.image_height)),
            (random.randint(0, self.image_width), random.randint(0, self.image_height))
        ]
        current_location = (0,0)

        # initialize an image and draw
        img = Image.new('RGB', (self.image_width, self.image_height), color='black')
        draw = ImageDraw.Draw(img)
        file = 'generated_image'
        timestamp = datetime.now().timestamp()
        filetype = 'png'
        output_file = "{}/{}_{}.{}".format(image_output_folder, file, timestamp, filetype)

        # loop through splitting the difference between current_location and any vertex
        loops = self.iteration_count
        file_sequence = 0
        while loops > 0:
            # pick a random vertex
            random_vertex = random.randint(0,len(vertices)-1)

            # calculate new location from current position and random_vertex
            new_location_x = (current_location[0] + vertices[random_vertex][0]) / 2
            new_location_y = (current_location[1] + vertices[random_vertex][1]) / 2

            # draw a point
            draw.point((new_location_x, new_location_y), fill='yellow')

            # save the image
            if self.save_sierpinski_iterations and loops % 500 == 0:
            #if self.save_sierpinski_iterations:
                #timestamp = datetime.now().timestamp()
                output_file = "{}/{}_{}.{}".format(image_output_folder, file, str(file_sequence).zfill(6), filetype)
                #print(output_file)
                img.save(output_file)
                file_sequence += 1

            # set the current location
            current_location = (new_location_x, new_location_y)

            # output information at an interval
            if loops % 500 == 0:
                print(f"Loops completed: {int(loops)}")

            # decrement the iteration_count var
            loops -= 1
