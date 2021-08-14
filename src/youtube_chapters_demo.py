#!/usr/bin/env python

import os
import sys
import youtube_dl

import opentimelineio as otio


youtubeURL = sys.argv[1]

videoFileName = youtubeURL + ".mp4"

print("youtube url: ", youtubeURL)

#os.system("youtube-dl --restrict-filenames --write-description -o '%s' %s" % (videoFileName, youtubeURL))



ydl_opts = {
    'outtmpl': 'tmp/%(id)s.mp4',
    'noplaylist': True,
    'quiet': True,
    'forceduration':True
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    dictMeta = ydl.extract_info(
        "https://www.youtube.com/watch?v={sID}".format(sID=youtubeURL),
        download=True)







# Steps for importing the video into OTIO
# 1. Create a TimeLine object
# timeline = otio.schema.TimeLine()
# timeline.name = "Youtube Demo"

# # 2. Create a Track on the timeline 
# track = otio.schema.Track()
# track.name = "Videos"
# timeline.tracks.append(track)

# 3. Find out how long the youtube video is
#available_range = otio.opentime.TimeRange(?,?)


# 4. Create a media_referene (contians the file path of the youtube video)
# 5. Create a Clip and set the media_reference (based on what we found in step 4) 
# 6. Append the Clip to the Track

