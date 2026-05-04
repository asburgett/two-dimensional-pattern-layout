from dotenv import load_dotenv

class Config:
    def __init__(self):
        self.ffmpeg_install_folder = "C:\\Users\\PC\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"
        self.graphviz_dot_install_folder = "C:\\Program Files\\Graphviz\\bin\\dot.exe"
        self.graphviz_neato_install_folder = "C:\\Program Files\\Graphviz\\bin\\neato.exe"
        self.load_configuration()

    def load_configuration(self):
        load_dotenv()
