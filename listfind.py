import os

import os
import glob as glob
import csv
from sys import argv

outputfilename = "search results.csv"

reslimit = 95  # limit for result match
chardif = 2  # maximum match length difference
charmin = 3  # minimum of carakters
srt_fixed='srt_fixed' # folder with srt files




if len(argv)==1:
    searchlist = input("please provide comma separated list of searchtemrs : term1,term2:\n").split(',')
    print(searchlist)
    print(type(searchlist))

if len(argv)==2:
    print(argv[1])
    searchlist = str(argv[1]).split(',')
    print(searchlist)
    print(type(searchlist))



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


def srtlistfind(filename, searchlist,writer):

    basefilename=os.path.basename(filename)
    year=basefilename[:4]
    date = basefilename[6:8] + "." + basefilename[4:6] + "." + year
    with open(filename, "r", encoding='utf8') as f:
        lines = f.read().lower().split('\n')  # each line is a list elem
        lines = list(filter(None, lines))  # remove empty lines
        for i in range(len(lines)):
            if not lines[i][0].isdigit():
                text = lines[i]  # split line in words
                for searchterm in searchlist:
                    result = text.find(searchterm)
                    if result>-1:
                        timecode=lines[i - 1]
                        resline = lines[i]

                        myid=filename[-len("XXXXXXXXXXX.de.fixed.srt"):-len(".de.fixed.srt")]
                        resurl = ts2idlink(timecode, myid)
                        dataline = [ resline , myid, timecode,date,searchterm,resurl]
                        writer.writerow(dataline)

                        #print(dataline)

                        #print('\n')


print("current path")
directory=os.path.dirname(os.path.realpath(__file__))
print(directory)


os.chdir(directory)



with open(outputfilename, 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    headline = ['resline', 'id', 'timecode','date','searchterm','resurl' ]
    writer.writerow(headline)
# derpi derp
    
    for filename in glob.glob(srt_fixed+'/*.srt'):
        print(filename)
        with open(filename, "r",encoding='utf-8') as srt_file:
            srtlistfind(filename, searchlist,writer)
            dataline=list()









