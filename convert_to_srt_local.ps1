# this powerscript converts all vtt files in folder containing the script to srt using ffmpeg
# you will need to activate the execution of powershell scripts first
# place ffmpeg.exe in the same folder as script and vtt files
Set-Location $PSScriptRoot # replace with your path of vtt files is needed
$files = @(Get-ChildItem  *.vtt -Name)


 foreach ($file in $files) {
 #echo $file
 $out = $file+".srt" 
 #echo $out

 ./ffmpeg.exe -i $("$file") $("$out")
 }