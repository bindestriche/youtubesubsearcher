import os
import glob as glob
from sys import argv

endfolder="txt_clean"
infolder="srt_fixed"

# converts the srt files from the in folder
# and saves them to the out folder as txt. remove timecodes and subnumbers

def cleansrt(txt):
    import re
    regex = re.compile(r'\d')
    oldlines = txt.split('\n')
    newlines = list(filter(lambda x: not regex.match(x), oldlines))
    return '\n'.join(newlines)



try:
    os.mkdir(endfolder)
except OSError:
    print ("Creation of the directory %s failed, probably allready there" % endfolder)
else:
    print ("Successfully created the directory %s " % endfolder)

for srt_file in glob.glob(infolder+'/*.srt'):
    print(srt_file)
    with open(srt_file, "r", encoding='utf8') as infile:
        txt=infile.read()
        out_txt=cleansrt(txt)
        basename = os.path.basename(srt_file)
        
        outfile = open(endfolder+"/"+basename[:-4]+".txt", "w",encoding='utf8')
        outfile.write(out_txt)
        outfile.close()

