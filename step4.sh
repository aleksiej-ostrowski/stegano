echo "=== step 4 ==="

# Upload 3.webm to youtube.com ...

# Download 3.webm from youtube.com as 4.webm. In my case:

# https://youtu.be/DQB9fi2ixhQ # --output 4.webm
md5sum 4.webm

mkdir frames4
time ffmpeg -i 4.webm "./frames4/out-%8d.png"
