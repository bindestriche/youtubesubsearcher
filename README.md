# youtubesubsearcher
scripts to search in a collection of youtube subtitles. 
In what video did your favourite youtube person use a certain word? Now you can find out without going through their videos manually.


## Step1 Build a collection of youtube subtitles
the search scripts expect a collection of srt clean subtitles.
you can use *autocollect_subs.py* for this.
`python autocollect_subs.py {URL}`
the URL can be anything that youtube-dl can get subtitles from. e.g. youtube channel,youtube-playlist, or just a single video.
 the default option right now is to download all subtitles, consider changing them to you need eg `'--write-auto-sub', '--sub-lang', 'en', `
 
### setup
Windows10 64bit, making it work for other platfrom should only requires minimal Changes. Make the script point to the ffmpeg and yotube-dl binaries of your plattform and compile the "subtitle-overlap-fixer" go script.

All of these files in the same folder as the *autocollect_subs.py* script:
 * [ffmpeg.exe](https://ffmpeg.org/download.html)
 * [youtube-dl.exe](https://ytdl-org.github.io/youtube-dl/download.html)
 * [subtitle-overlap-fixer.exe](https://github.com/bindestrichsoz/youtubesubsearcher/raw/main/subtitle-overlap-fixer.exe)


### manually
#### external services
[downsub.com](https://downsub.com/) gives you clean srt subtitles from youtube videos right away.

### youtube-dl and ffmpeg
Youtube-dl can download subtitles in batches for us.
 `./youtube-dl --write-auto-sub --sub-lang de --sub-format vtt --skip-download [channel or playlist URL] -o "%(upload_date)s-%(id)s.%(ext)s"`
yt-dlp is a fork of YouTube-dl that works better, the command is the same , just start with yt-dlp.
  
this gives us a collection of vtt files.

youtube-dl can convert subs using ffmpeg, but only when the video is downloaded, so use ffmpeg directly to convert .vtt subtitles to .srt.

`./ffmpeg -i '{vtt-FILE}.vtt' '{SRT-FILE}.srt'`

You can use the 'convert_to_srt_local' scripts to convert serveral subtitles in an automated way.
place the script in a folder with .vtt subs and ffmpeg.exe, then execute the script.

### subtitle-overlap-fixer
When you download youtube subtitles with youtube-dl and convert them to .srt using ffmpeg, the subtitles have overlap and double lines.
the subtitle over lap fixer takes care of that. code is based on this [go script from nimatrueway](https://gist.github.com/nimatrueway/4589700f49c691e5413c5b2df4d02f4f).
the tk inter gui asks for an input and end out but folder.

*usage*
`./subtitle-overlap-fixer '{SRT-FILE}.srt'`


## Step2 search collection of youtube subtitles

### listfind.py
uses find to search in srt lines. expects a folder *srt_fixed* as a subfolder (as produced by *autocollect_subs.py* )

`'python listsearch.py' term1,term2`
or just run `'python listsearch.py' and enter the search terms manually


### listsearch.py

uses fuzzymatching for finding words
have the module 'fuzzywuzzy' installed `pip install fuzzywuzzy`

**use**
`'python listsearch.py' term1,term2`

**output**
a *search results.csv*  the links in the table link go directly to video at the time when the searchterm is said.

resline,id,duration,resurl

Line with term1,XXXXXXXXXXX,"00:06:49,199 --> 00:06:51,810",https://youtu.be/XXXXXXXXXXX?t=409

### Other Tools
The software [AntConc](http://www.laurenceanthony.net/software/antconc/) is a gratis Concordance Tool, it might be usefull to for deeper analysis. you can use make txt.py to convert the fixed srt subtitles to txt files for corpus analysis.
More tools https://corpus-analysis.com/


