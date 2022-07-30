# otio-youtube-example


## Overview

This project serves as a working example to illustrate the key features of [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) (maintained by the Academy Software Foundation).  The example will take in a youtube url as input.  The example will then download the youtube video and description onto the user's local computer and import the data into an OTIO Timeline.  The example will extract the "table of contents" data from the youtube description and import this information as "Markers" on the Timeline.  The final timeline is exported as a .otio file. 

## Licensing

This repository is licensed under the [Apache License, Version 2.0](LICENSE.md). 

## Documentation 

The documentation can be found here: https://utsab.github.io/otio-youtube-example/ 

The documentation is intended to provide a detailed walkthrough of the basic OpenTimelineIO concepts within the context of a concrete example. 

[Session Notes](https://docs.google.com/document/d/1czIu3xKXr1FmEl88fZekUPy1aaqnHXF-8M3AwJ78BHs/edit) (A log of our programming sessions as we build this). 


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
```python3 youtube_chapters_demo.py pvkTC2xIbeY```

This should create two files on your local computer: NtevTo96Wjc.description and NtevTo96Wjc.mp4

** To run the test: **

python3 -m unittest test_youtube_chapters_demo.py


## Linter
Install [black](https://github.com/psf/black)
```
pip3 install black
```
Run the linter
```
black {source_file_or_directory}
```

## MkDocs

The otio-youtube-example project utilizes MkDocs to build the documentation as a user-friendly web application.  If you wish to update the documentation, you should follow these instructions to build the documentation web application locally.  

Install [mkdocs](https://www.mkdocs.org/getting-started/)
```
pip3 install mkdocs
```

Run MkDoc Server
```
mkdocs serve
```

After you test your documentation changes locally, you can push your changes to the official otio-youtube-example documentation with the following instructions: 


Build the site
``` 
mkdocs build
```

Deploy to Github Pages
```
mkdocs gh-deploy 
```


## Contributions

If you have any suggested changes to the otio-youtube-example repository itself, 
please provide them via [pull request](../../pulls) or [create an issue](../../issues) as appropriate. 

All contributions back to the template repository must align with the contribution
[guidelines](https://opentimelineio.readthedocs.io/en/latest/tutorials/contributing.html) 
of the OpenTimelineIO project.


