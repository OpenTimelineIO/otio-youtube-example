#!/usr/bin/env python

import os
import sys
import youtube_dl
import re

import opentimelineio as otio


# Input: @description_file contains the Youtube description
# Function should parse the Youtube description to find any table-of-contents entries. 
# The table-of-contents entries will contain a timestamp paired with a chapter title. 
# For example: (00:12:15) Thor fights Thanos
# 
# The function should return an array of all such timestamps and chapter titles. 
#
def process_youtube_description(description_file): 
  with open(description_file) as f:
    lines = f.readlines()

  # Should match the following timestamp patterns: 
  # 01:34:21 chapter title
  # 1:34:21 chapter title
  # 34:21 chapter title
  # 4:21 chapter title
  pattern = re.compile('((?:\d+:)+\d{2})\s(.+)')
 

  for line in lines: 
      print(line)
      print(pattern.findall(line))  


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

# 2. Create a Track on the timeline 
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



# 7. Process the youtube description and insert Markers into the timeline
description_file = "tmp/" + youtubeURL + ".description"
process_youtube_description(description_file)


#save the timeline as .otio file 

otio_filename = youtubeURL + ".otio"
otio.adapters.write_to_file(timeline, otio_filename)
print(
    "SAVED: {0} with {1} clips.".format(
        otio_filename,
        len(timeline.tracks[0])
    )
)



