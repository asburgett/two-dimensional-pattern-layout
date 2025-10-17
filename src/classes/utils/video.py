from src.config.config import Config
import os
import subprocess

class Video:
    def __init__(self):
        self.input_folder = ''
        # TODO: make the ffmpeg functionality os agnostic (linux, mac, win, etc)
        #self.ffmpeg_installation_folder = "C:\\Users\\PC\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"
        self.ffmpeg_installation_folder = "C:\\Users\\PC\\Downloads\\ffmpeg-8.0-essentials_build\\bin\\ffmpeg.exe"

    def run(self):
        print(f"Input folder: {self.input_folder}")

    def check_for_ffmpeg_installation(self):
        if os.path.isfile(self.ffmpeg_installation_folder):
            print(f"FFMPEG installed at: {self.ffmpeg_installation_folder}")

    def create_video_with_ffmpeg(self, image_folder, output_video_path, fps):
        # The files in the image_folder must be numbered sequentially as of ffmpeg version N-121335-g660983b7f3-20251007
        print(os.path.join(image_folder, "generated_image_%6d.png"))
        ffmpeg_command = [
            self.ffmpeg_installation_folder,
            "-framerate", str(fps),
            "-i", os.path.join(image_folder, "generated_image_%6d.png"),  # Adjust pattern if needed
            "-c:v", "h264_nvenc",  # h264, threaded nvidia gpu
            #"-c:v", "hevc_nvenc",  # nvidia gpu, hevc
            #"-c:v", "libx264",  #std, h264, threaded cpu's
            "-pix_fmt", "yuv420p",
            output_video_path
        ]
        print(ffmpeg_command)

        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f"Video created successfully at: {output_video_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating video with FFmpeg: {e}")
