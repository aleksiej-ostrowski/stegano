# This is a steganographic science experiment to combine two videos.

## The acceptor-video:

https://user-images.githubusercontent.com/55213346/153609701-b25d4be6-d690-4389-b8a8-bba8010d10f1.mp4


## The donor-video:

https://user-images.githubusercontent.com/55213346/153609755-fd10dc95-3b4d-4993-8dd5-efca5f8b7a6f.mp4


## The result:

https://user-images.githubusercontent.com/55213346/153610501-a2a172f3-6fca-43c4-b14e-f68587912a35.mp4


## To run this experiment, follow these steps:

```bash
bash step1.sh
# Resizing 2.mp4 to 2_.mp4. Unpacking 1.mp4 and 2_.mp4 to PNG frames. Checking the combination function. 
```

```bash
bash step2.sh
# Running the combination function for PNG frames.
```

```bash
bash step3.sh
# Packing PNG frames to 3.webm
```

```bash
bash step4.sh
# Uploading 3.webm to youtube.com ... and downloading this file as 4.webm.
# Unpacking 4.webm
```

```bash
bash step5.sh
# Extracting internal information from 4.webm
```

```bash
bash step6.sh
# Packing PNG frames to 5.webm with speed correction.
```

```bash
bash step7.sh
# Preparing a video comparing two parts: 2_.mp4 and 5.webm.  
```

OR for shortening:

```bash
bash run.sh
```

## TODO
- [X] Rewriting the module mix.py in golang.


## Paper about this
[Стеганографические эксперименты с видеофайлами и Youtube (in Russian)](https://habr.com/ru/post/651905/)
