#!/usr/bin/env python

import os
import sys
import youtube_dl

import opentimelineio as otio


youtubeURL = sys.argv[1]

videoFileName = youtubeURL + ".mp4"


ydl_opts = {
    'outtmpl': 'tmp/%(id)s.mp4',
    'noplaylist': True,
    'quiet': True,
    'writedescription' : True
}

# Download the youtube video and description onto local computer 
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    dictMeta = ydl.extract_info(
        "https://www.youtube.com/watch?v={sID}".format(sID=youtubeURL),
        download=True)
    




# Steps for importing the video into OTIO
# 1. Create a TimeLine object
timeline = otio.schema.Timeline()
timeline.name = "Youtube Demo"

# # 2. Create a Track on the timeline 
track = otio.schema.Track()
track.name = "Videos"
timeline.tracks.append(track)

# 3. Find out how long the youtube video is
totalFrames = dictMeta['duration'] * dictMeta['fps']


available_range = otio.opentime.TimeRange(
    otio.opentime.RationalTime(0, dictMeta['fps']),
    otio.opentime.RationalTime(totalFrames, dictMeta['fps'])
)


# 4. Create a media_reference (contians the file path of the youtube video)

media_reference = otio.schema.ExternalReference(
        target_url="tmp/" + videoFileName,
        available_range=available_range
    )

# 5. Create a Clip and set the media_reference (based on what we found in step 4) 
clip = otio.schema.Clip(name="Youtube clip")
clip.media_reference = media_reference


# 6. Append the Clip to the Track
track.append(clip)


#save the timeline as .otio file 



otio_filename = youtubeURL + ".otio"
otio.adapters.write_to_file(timeline, otio_filename)
print(
    "SAVED: {0} with {1} clips.".format(
        otio_filename,
        len(timeline.tracks[0])
    )
)