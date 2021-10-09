# OTIOExamples


## Overview

This project serves as a working example to illustrate the key features of the OpenTimelineIO project (owned by Pixar).  The example will take in a youtube url as input.  The example will then download the youtube video and description onto the user's local computer and import the data into an OTIO Timeline.  The example will extract the "table of contents" data from the youtube description and import this information as "Markers" on the Timeline.  The final timeline is exported as a .otio file. 

## Pre-Requisites

* Install the OpenTimelineIo python library based on these [instructions](https://opentimelineio.readthedocs.io/en/latest/tutorials/quickstart.html)
* A valid C/C++ compiler
* For MacOS if you run into a 'SSL: CERTIFICATE_VERIFY_FAILED' error then follow these [instructions](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)

## Installation

sudo pip3 install youtube-dl

python version: 3.x

## Sample usage: 


** To run the actual example: **

```git checkout youtube_demo```     
```python3 youtube_chapters_demo.py NtevTo96Wjc```

This should create two files on your local computer: NtevTo96Wjc.description and NtevTo96Wjc.mp4

** To run the test: **

python3 -m unittest test_youtube_chapters_demo.py



[Session Notes](https://docs.google.com/document/d/1czIu3xKXr1FmEl88fZekUPy1aaqnHXF-8M3AwJ78BHs/edit) (A log of our programming sessions as we build this). 
