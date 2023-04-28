import os

from rapidfuzz import process
#converts all youtube-dl json in current folder into one csv file
import os
import glob as glob
import csv

outputfilename = "search results.csv"

reslimit = 95  # limit for result match
chardif = 2  # maximum match length difference
charmin = 3  # minimum of carakters
srt_fixed='srt_fixed' # folder with srt files




if len(argv)==1:
    searchlist = input("please provide commaspeprated list of searchtemrs : term1,term2:\n").split(',')

if len(argv)==2:
    searchlist = argv[1].split(',')




def ts2idlink(timestring,id):
    hour=int(timestring[:2])
    #print(hour)
    minute=int(timestring[3:5])
   #print(minute)

    second=int(timestring[6:8])
   # print(second)
    seconds=second+minute*60+hour*60*60
  #  print(seconds)
    return "https://youtu.be/"+id+"?t="+str(seconds)


def srtlistmatch(filename, searchlist,writer):
    year=filename[:4]
    date = filename[6:8] + "." + filename[4:6] + "." + year
    with open(filename, "r", encoding='utf8') as f:
        lines = f.read().lower().split('\n')  # each line is a list elem
        lines = list(filter(None, lines))  # remove empty lines
        for i in range(len(lines)):
            if not lines[i][0].isdigit():
                text = lines[i].split()  # split line in words
                for searchterm in searchlist:
                    result = process.extract(searchterm, text, limit=3)
                    if result[0][1] >= reslimit:


                        duration=lines[i - 1]
                        resline = lines[i]

                        myid=filename[-len("MY0Sv-K-FG8.de.fixed.srt"):-len(".de.fixed.srt")]
                        resurl = ts2idlink(duration, myid)
                        dataline = [ resline , myid, duration, resurl]
                        writer.writerow(dataline)

                        print(dataline)

                        print('\n')


print("current path")
directory=os.path.dirname(os.path.realpath(__file__))
print(directory)


os.chdir(directory)



with open(outputfilename, 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    headline = ['resline', 'id', 'duration', 'resurl' ]
    writer.writerow(headline)

    for filename in glob.glob(srt_fixed+'/*.srt'):

        with open(filename, "r",encoding='utf-8') as srt_file:
            srtlistmatch(filename, searchlist,writer)
            dataline=list()








