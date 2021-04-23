# youtubesubsearcher
scripts to search in a collection youtube subtitles. 
In what video did your favourite youtube person use a certain word? Now you can find out without going through their videos manually.


## Step1 Build a collection of youtube subtitles

the search scripts expects a collection of srt clean subtitles.

## download the subtitles

### manually

[downsub.com](https://downsub.com/) gives you clean srt subtitles from youtube videos right away.

### youtube-dl
youtube-dl can take care of that for us.
  ./youtube-dl --write-auto-sub --sub-lang de --sub-format vtt --skip-download [channel or playlist URL] -o "%(upload_date)s-%(id)s.%(ext)s"
this gives us a collection of vtt files

### convert subs with ffmpeg
youtube-dl can convert subs using ffmpeg, but only when the video is downloaded and ffmpeg is installed.
We use ffmpeg to convert .vtt subtitles to .srt.

*usage*
`./ffmpeg -i '{vtt-FILE}.vtt' '{SRT-FILE}.srt'`

you can use the convert_to_srt_local scripts to convert serveral subtitles in an automated way.
place the script in a folder with .vtt subs and ffmpeg.exe, then execute the script.

## subtitle-overlap-fixer
When you download youtube subtitles with youtube-dl and convert them to .srt using ffmpeg, the subtitles have overlap and double lines.
This [go script from nimatrueway](https://gist.github.com/nimatrueway/4589700f49c691e5413c5b2df4d02f4f) fixes that.

*usage*
`./subtitle-overlap-fixer '{SRT-FILE}.srt'`
