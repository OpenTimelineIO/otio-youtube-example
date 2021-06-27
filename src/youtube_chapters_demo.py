#!/usr/bin/env python

import os
import sys
import opentimelineio as otio


youtubeURL, outputpath = sys.argv[1:]

videoFileName = youtubeURL + ".mp4"

print("youtube url: ", youtubeURL)
print("outputpath: ", outputpath)

os.system("youtube-dl --restrict-filenames --write-description -o '%s' %s" % (videoFileName, youtubeURL))
