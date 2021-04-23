for d in *vtt; do
 fmpeg.exe -i $d "${d}.srt"
done
