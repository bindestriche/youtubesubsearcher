import os
import subprocess

directory=os.path.dirname(os.path.realpath(__file__))
os.chdir(directory) # change working directory to path of this script file

for raw_sub_file in os.listdir(directory):
    if raw_sub_file.endswith("vtt"):
        subprocess.call(['ffmpeg.exe', '-i', directory + "/" + raw_sub_file, raw_sub_file+".srt"])
