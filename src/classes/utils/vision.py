import cv2

class ComputerVision:
    def __init__(self):
        self.create_run_folder = True

    # TODO: refactor this, need to clarify where I want the majority of processing logic (main.py or here)
    # eg: does main run each step, or is it all invisible to main (does main need the gray image?)
    def convert_image_to_grayscale(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)
        return gray_image

    def get_installed_version(self):
        return cv2.__version__

    def run_canny_edge_detector(self, gray_image):
        edges = cv2.Canny(gray_image, 100, 200)
        return edges

    def process_image_for_edges(self, filename):
        image = cv2.imread(filename)
        if image is not None:
            # TODO: apply image processing?  Return the image and process elsewhere?
            gray_image = self.convert_image_to_grayscale(image)
            edges = self.run_canny_edge_detector(gray_image)
            cv2.imshow("Original image", image)
            cv2.imshow("Gray image", gray_image)
            cv2.imshow("Canny image", edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print(f"Error reading image: {filename}")