# fixes srt subtitles produced by ffmpeg converting youtube subtitles
# based on https://gist.github.com/nimatrueway/4589700f49c691e5413c5b2df4d02f4f


import sys
import os
import srt # needs to be installed
from datetime import timedelta

# gooey is optional
try:
    from gooey import Gooey, GooeyParser
    use_gooey = True
except ImportError:
    from argparse import ArgumentParser
    use_gooey = False



def fix_subtitle(subtitles):
    fixed_subtitles = []
    last_subtitle = None

    for subtitle in subtitles:
        if last_subtitle:
            subtitle.content = subtitle.content.strip()
            if not subtitle.content:  # skip over empty subtitles
                continue

            # skip over super-short subtitles that basically contain what their previous subtitle contains,
            # and just prolong the previous subtitle
            if subtitle.end - subtitle.start < timedelta(milliseconds=150) and subtitle.content in last_subtitle.content:
                last_subtitle.end = subtitle.end
                continue

            # if the first line of the current subtitle is repeating the last line of the previous subtitle, remove it
            current_lines = subtitle.content.split("\n")
            last_lines = last_subtitle.content.split("\n")
            if current_lines[0] == last_lines[-1]:
                subtitle.content = "\n".join(current_lines[1:])

            # if the current subtitle starts before the previous subtitle ends, adjust the previous subtitle's end time
            if subtitle.start < last_subtitle.end:
                last_subtitle.end = subtitle.start - timedelta(milliseconds=1)

        if last_subtitle:
            fixed_subtitles.append(last_subtitle)

        last_subtitle = subtitle

    if last_subtitle:
        fixed_subtitles.append(last_subtitle)

    return fixed_subtitles



def main_parser():
    if use_gooey:
        parser = GooeyParser(description="Fix subtitle timings and overlapping text")
        parser.add_argument("in_folder", metavar="Input Folder", help="Folder containing subtitle files to fix",
                            widget="DirChooser")
        parser.add_argument("out_folder", metavar="Output Folder", help="Folder to save fixed subtitle files",
                            widget="DirChooser")

    else:
        parser = ArgumentParser(description="Fix subtitle timings and overlapping text")

        parser.add_argument("in_folder", metavar="Input Folder", help="Folder containing subtitle files to fix")
        parser.add_argument("out_folder", metavar="Output Folder", help="Folder to save fixed subtitle files")

    return parser

def wrapped_main(in_folder, out_folder):
    dirlist=os.listdir(in_folder)

    for i,filename in enumerate(dirlist):
        if filename.endswith(".srt"):
            infile_path = os.path.join(in_folder, filename)
            outfile_path = os.path.join(out_folder, filename)

            with open(infile_path, "r",encoding="utf8") as file:
                subtitle_text = file.read()

            subtitles = list(srt.parse(subtitle_text))
            fixed_subtitles = fix_subtitle(subtitles)
            fixed_subtitle_text = srt.compose(fixed_subtitles)

            with open(outfile_path, "w",encoding="utf8") as new_file:
                new_file.write(fixed_subtitle_text)
        print(f"{i+1} of {len(dirlist)}")

if use_gooey:
    @Gooey(program_name="Subtitle Fixer")
    def main():
        parser = main_parser()
        parser.set_defaults(widget_type="DirChooser")
        args = parser.parse_args()
        wrapped_main(args.in_folder, args.out_folder)
else:
    def main():
        parser = main_parser()
        args = parser.parse_args()
        wrapped_main(args.in_folder, args.out_folder)

if __name__ == "__main__":
    main()
