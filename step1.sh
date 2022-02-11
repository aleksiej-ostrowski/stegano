mkdir frames1 frames2 audio1 audio2

ffmpeg -i 1.mp4 "./frames1/out-%8d.png"
ffmpeg -i 1.mp4 "./audio1/audio.ogg"
ffmpeg -i 2.mp4 -s 320x180 -c:a copy 2_.mp4
md5sum 2_.webm
ffmpeg -i 2_.mp4 "./frames2/out-%8d.png"
ffmpeg -i 2_.mp4 "./audio2/audio.ogg"
cp "./frames1/out-00000001.png" "./one.png"
cp "./frames2/out-00000001.png" "./two.png"
python3.9 mix.py
