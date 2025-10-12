from moviepy import (
    TextClip, 
    VideoFileClip,
    AudioFileClip,
    ImageClip,
    CompositeVideoClip
    )

# Estou usando FFMPEG
# Learning MoviePy

# ImageClip('./img/stickmen.jpg', duration=5).preview()

clip = VideoFileClip('./movies/Back.to.the.Future.1985.720p.BrRip.x264.YIFY.mp4',).subclipped(100.893,104.187)

# clip.subclipped(417,420).preview(fps=120)



clip.preview(fps=60)
