# Welcome to OTIOExamples

The github repository is located [here](https://github.com/utsab/OTIOExamples).

The goal of this documentation is to explain the basic OpenTimelineIO concepts using our Youtube Demo (contained in the OTIOExamples repository) as a concrete example.  We will walk through the following statement within the context of our Youtube Demo: 

"OpenTimelineIO is a file format, an API, and a plugin system." 





## High-level purpose of OpenTimelineIO 


OpentimeLineIO (OTIO) is a tool that helps to visualize the high-level structure of a media composition (such as an animated film or a movie with layers of visual effects).  

The inputs to OTIO are the media files, such as the video, audio, and any other related content.  The inputs can also include "metadata" about the media, such as the positions of the cameras at different points of the video.   

The output is an .otio file which represents a timeline for the media composition.  All of the various inputs (video, audio, other metadata) are shown as layers on the timeline.  

![High-level visual](./img/high_level_visual.png?raw=true "High-level purpose of OTIO")


The OTIOExamples repository illustrates one concrete example of how we can use OTIO.  The example inputs the following files into OpenTimelineIO: 

1. A Youtube video
2. The Youtube description 

![Inputs to OTIO](./img/inputs_visual.png?raw=true "Inputs to OTIO")


You can run the example yourself for a [specific Youtube video](https://www.youtube.com/watch?v=RBSGKlAvoiM) by running a command such as the following: 

`$ python3 youtube_chapters_demo.py RBSGKlAvoiM`


OpenTimeLineIO then generates the following .otio file: 

[RBSGKlAvoiM.otio](./examples/RBSGKlAvoiM.otio)

We can use the otioview program to visualize the contents of the RBSGKlAvoiM.otio file. 

`$ otioview RBSGKlAvoiM.otio`


![otioview visual](./img/otioview_visual.png?raw=true "otioview visual")


Note that the list of chapter titles from the description of the original Youtube video are represented as the green markers in the timeline, while the video itself is represented as the blue rectangle behind the markers. 

![Annotated markers](./img/annotated_markers.png?raw=true "Annotated markers")


Ultimately, the purpose of the final output (the .otio file) is to enable editors to make decisions.  For example, in our Youtube Demo, an editor can look at the timeline and visualize the layout of all the markers.  The editor might then realize, for example, "We could use another marker at the 4:31 timestamp." 

A more realistic example of how editors might use the .otio file in the context of, say, an animated film could be somethign like the following: 

“The helicopter explosion clip should be overlayed on the timeline a little bit earlier, at 42:30 instead of 42:31.” 






