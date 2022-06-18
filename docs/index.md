# Welcome to OTIOExamples

The github repository is located [here](https://github.com/utsab/OTIOExamples).

## Documentation layout

We will explain the OpenTimelineIO codebase in five levels of complexity: 
* Level 1: The high level purpose of OTIO 
* Level 2: OTIO is a file format, an API, and a collection of adaptors and plugins. 
* Level 3: The technology stack of the OTIO codebase
* Level 4: Important design patterns / architectural components 
* Level 5: Walkthrough of the codebase 



## Level 1 


OpentimeLineIO is a tool that helps to visualize the high-level structure of a media composition (such as an animated film or a movie with layers of visual effects).  

The inputs to OTIO are the media files, such as the video, audio, and any other related content.  The inputs can also include "metadata" about the media, such as the positions of the cameras at different points of the video.   

The output is an .otio file which represents a timeline for the media composition.  All of the various inputs (video, audio, other metadata) are shown as layers on the timeline.  

The OTIOExamples repository illustrates one concrete example of how we can use OTIO.  The example inputs the following into OTIO: 
1. A Youtube video
2. The Youtube description 

![Inputs to OTIO](./img/inputs_visual.png?raw=true "Inputs to OTIO")








