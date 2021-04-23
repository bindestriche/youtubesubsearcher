import os
import subprocess
import glob as glob
from sys import argv





directory=os.path.dirname(os.path.realpath(__file__))
os.chdir(directory) # change working directory to path of this script file


# make sure these exist will be called with subprocess
path_ffmpeg='ffmpeg.exe'
path_subfixer='subtitle-overlap-fixer.exe'
path_youtube_dl='youtube-dl.exe'

neededfiles=[path_ffmpeg,path_subfixer,path_youtube_dl]

for file in neededfiles:
    if os.path.isfile(file):
        print(file+" found.")
    else:
        print(file+" missing! aborting.")
        exit()
              
print ("all needed files present") 

#these folder names can be changed
folder_vtt="vtt_raw"
folder_srt_raw="srt_raw"
folder_srt_fixed="srt_fixed"
folder_infojson="json_info"




print(directory)
print(argv)

if len(argv)==1:
    url = input("please provide url:")

if len(argv)==2:
    url = argv[1]

# you can change the naming convention of the files as long as the file endings stay at the end ".%(ext)s' "   
# consider changing the download options of the subtitles eg ' '--write-auto-sub', '--sub-lang', 'en', ' 
callline=[path_youtube_dl, '--write-auto-sub', '--all-subs', '--sub-format', 'vtt', '--skip-download', '-o', "'%(upload_date)s-%(uploader_id)s-%(id)s.%(ext)s'", '--write-info-json', '--skip-download',url]

    




# create folders if not presen

folders=[folder_vtt,folder_srt_raw,folder_srt_fixed,folder_infojson]

for path in folders:
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed, probalby allready there" % path)
    else:
        print ("Successfully created the directory %s " % path)

# dowload subtitles
subprocess.call(callline)

# move info json in correct folder
for file in glob.glob('*.info.json'):
    try:
        os.replace(file,folder_infojson+"/" +file)
    except OSError as e:
        print(e)

# move vtt in correct folder
for file in glob.glob('*.vtt'):
    try:
        os.replace(file,folder_vtt+"/" +file)
    except OSError as e:
        print(e)

# convert subs using ffmpeg
for raw_sub_file in glob.glob(folder_vtt+'/*.vtt'):
    if os.name == 'nt':
        #print(raw_sub_file)
        subprocess.call([path_ffmpeg, '-i',  raw_sub_file, folder_srt_raw+"\\"+raw_sub_file[len(folder_vtt):-4]+".srt"])
    else:
        subprocess.call(['ffmpeg', '-i',     raw_sub_file, folder_srt_raw+"\\"+raw_sub_file[len(folder_vtt):-4] + ".srt"])

for file in glob.glob(folder_srt_raw+'/*.srt'):
    if os.name == 'nt':
        print(file)
        subprocess.call([path_subfixer,file])
    else:
        subprocess.call(['subtitle-overlap-fixer',file])


#move fixed srt files
for file in glob.glob(folder_srt_raw+'/*.fixed.srt'):
    print(file)
    try:
        os.replace(file,folder_srt_fixed+"\\" +file[len(folder_srt_raw):])
    except OSError as e:
        print(e)
