# Upload 3.webm to youtube.com ...

# Download 3.webm from youtube.com as 4.web. In my case:

# https://youtu.be/DQB9fi2ixhQ # --output 4.webm
md5sum 4.webm

mkdir frames4
ffmpeg -i 4.webm "./frames4/out-%8d.png"
