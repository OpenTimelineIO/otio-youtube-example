#!/usr/bin/env python

import os
import sys
import youtube_dl
import re
import datetime

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
  # (4:21) chapter title
  # [4:21] chapter title


  pattern = re.compile('((?:\d+:)+\d{2})[\),\]]*\s(.+)')
  chapters = []

  for line in lines: 
      matches = pattern.findall(line) 
      if matches: 
          chapters.append(matches[0])
   
  return chapters
         


def convert_time_stamp_to_seconds(time_stamp):
    if len(time_stamp) > 5:
        date_time = datetime.datetime.strptime(time_stamp, "%H:%M:%S")
    else:
        date_time = datetime.datetime.strptime(time_stamp, "%M:%S")
    
    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    return seconds 


def create_markers(chapters, fps):
    markers = []

    for chapter in chapters: 
        seconds = convert_time_stamp_to_seconds(chapter[0])
 
        marker = otio.schema.Marker()

        marker.marked_range = otio.opentime.TimeRange(
            start_time=otio.opentime.RationalTime(seconds*fps, fps),
            duration=otio.opentime.RationalTime(0, fps) # We are setting the duration of each marker to be 0 frames. 
        )
 
        marker.color = otio.schema.MarkerColor.RED
 
        marker.name = chapter[1]
        markers.append(marker)


    return markers





def download_from_youtube(youtubeURL): 
    ydl_opts = {
        'outtmpl': os.path.join('tmp', '%(id)s.mp4'),
        'noplaylist': True,
        'quiet': True,
        'writedescription' : True
    }

    # Download the youtube video and description onto local computer 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        dictMeta = ydl.extract_info(
            "https://www.youtube.com/watch?v={sID}".format(sID=youtubeURL),
            download=True)
    
    return dictMeta
    


def create_timeline(dictMeta, video_file, description_file, otio_file): 
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
            target_url=os.path.join('tmp', video_file),
            available_range=available_range
        )

    # 5. Create a Clip and set the media_reference (based on what we found in step 4) 
    clip = otio.schema.Clip(name="Youtube clip")
    clip.media_reference = media_reference


    # 6. Append the Clip to the Track
    track.append(clip)



    # 7. Process the youtube description and insert Markers into the timeline
    chapters = process_youtube_description(description_file) 

    markers = create_markers(chapters, dictMeta['fps'])


    for marker in markers:
        clip.markers.append(marker)





    #save the timeline as .otio file 
    otio.adapters.write_to_file(timeline, otio_file)
    print(
        "SAVED: {0} with {1} clips.".format(
            otio_file,
            len(timeline.tracks[0])
        )
    )





  

def main():
   # I'd also recommend building a simple argument parser using the
   # argparse module here, so you get --help and other affordances
   youtubeURL = sys.argv[1]

   video_file = youtubeURL + ".mp4"
   description_file = os.path.join('tmp', youtubeURL + '.description')
   otio_file = youtubeURL + ".otio"

   dictMeta = download_from_youtube(youtubeURL)  
   create_timeline(dictMeta, video_file, description_file, otio_file)  

if __name__ == "__main__":
   main()






