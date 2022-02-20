echo "=== step 7 ==="

# mpv 2_.mp4 --external-file=5.webm --lavfi-complex='[vid1] [vid2] vstack [vo]' # --stream-record=compare.ts
ffmpeg -i 2_.mp4 -i 5.webm -filter_complex hstack compare.webm
