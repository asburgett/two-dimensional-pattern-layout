import os
import subprocess

class Video:
    def __init__(self):
        self.input_folder = ''
        self.ffmpeg_installation_folder = "C:\\Users\\PC\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"

    def run(self):
        print(f"Input folder: {self.input_folder}")

    def check_for_ffmpeg_installation(self):
        if os.path.isfile(self.ffmpeg_installation_folder):
            print(f"FFMPEG installed at: {self.ffmpeg_installation_folder}")

    def create_video_with_ffmpeg(self, image_folder, output_video_path, fps):
        ffmpeg_command = [
            "C:\\Users\\PC\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe",
            "-framerate", str(fps),
            "-i", os.path.join(image_folder, "generated_image_%20d.png"),  # Adjust pattern if needed
            #"-c:v", "h264_nvenc",  # h264, threaded nvidia gpu
            #"-c:v", "hevc_nvenc",  # nvidia gpu, hevc
            "-c:v", "libx264",  #std, h264, threaded cpu's
            "-pix_fmt", "yuv420p",
            os.path.join(image_folder, output_video_path)
        ]
        print(ffmpeg_command)

        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f"Video created successfully at: {output_video_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating video with FFmpeg: {e}")
