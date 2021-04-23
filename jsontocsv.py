#converts all youtube-dl json in current folder into one csv file
import os
import glob as glob
import json
import csv


#print("current path")
directory=os.path.dirname(os.path.realpath(__file__))
outname='videoinfo.csv'
#print(directory)
os.chdir(directory)



with open(outname, 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    headline = ['title', 'channel', 'duration', 'vcodec', 'uploader_url', 'webpage_url', 'channel_id', 'fulltitle',
                 'webpage_url_basename', 'upload_date', 'channel_url', 'view_count',
                'like_count', 'categories', 'uploader_id', 'id', 'uploader','tags',]
    writer.writerow(headline)

    for filename in glob.glob('*.json'):
        with open(filename, "r",encoding='utf-8') as json_file:
            #print("filename"+filename)
            jsonfile = json.load(json_file)
            dataline=list()
            for item in headline:
                try:
                    dataline.append(str(jsonfile[item]))
                except:
                    dataline.append("")
            #print(dataline)
            writer.writerow(dataline)

            url=jsonfile['webpage_url']
            duration=jsonfile['duration']
            id = jsonfile['id']


