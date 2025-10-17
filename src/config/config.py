from dotenv import load_dotenv

class Config:
    def __init__(self):
        #self.ffmpeg_install_folder = "path"
        self.ffmpeg_install_folder = "C:\\Users\\PC\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"

    def load_configuration(self):
        load_dotenv()
