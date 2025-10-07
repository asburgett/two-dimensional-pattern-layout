from PIL import Image, ImageDraw
from datetime import datetime

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