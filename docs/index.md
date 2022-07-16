# Welcome to OTIOExamples

The github repository is located [here](https://github.com/utsab/OTIOExamples).



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


Note that list of chapter titles from the description of the original Youtube video are represented as the green markers in the timeline, while the video itself is represented as the blue rectangle behind the markers. 




==> Talk about OTIOView (helps visualize the .otio file)

==> Show a screenshot of OTIOView displaying the Youtube demo timeline 

==> Annotate the screenshot ==> Show the relationship between the markers on the timeline and the chapter breakdown in the Youtube description.  

==> Explanation how this otio file is then used by editors to make a decision. “As an editor, I would look at XYZ part of the otio file and realize that EFG is off so I would make GHI recommendation to adjust XYZ.” 

TODO: Ask the OTIO maintainers for a realistic example that can complete the above scenario.

For the Youtube Demo: “As the Youtube video creator, I can see how all the markers are spaced out, and I’m realizing that we could use another marker at the 4:31 timestamp in the video timeline”  




