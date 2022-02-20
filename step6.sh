echo "=== step 6 ==="

ffmpeg -filter_complex [0:v]setpts=0.0346*PTS -pattern_type glob -i "./frames5/*.png" 5.webm
ffprobe 5.webm | grep Duration
md5sum 5.webm
