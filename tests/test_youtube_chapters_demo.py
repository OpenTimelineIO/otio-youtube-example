import os
import sys

sys.path.append("../src/")

import unittest
import opentimelineio as otio
import youtube_chapters_demo as demo


class YoutubeChaptersDemoTests(unittest.TestCase):
    def test_download_youtube_files(self):
        youtubeVideoID = "pvkTC2xIbeY"
        skip_video_download = False  # If you want to speed up the test, set this to True so that the video doesn't download

        # run the youtube_chapters_demo example...
        results = demo.run_demo(youtubeVideoID, skip_video_download)

        video_file = results["video_file"]
        description_file = results["description_file"]
        otio_file = results["otio_file"]

        # Tests

        # Test 1: Verify that an mp4 file is created disk.
        if not skip_video_download:
            self.assertTrue(os.path.isfile(video_file), "No video file found")

        # Test 2: Verify that a txt file is created on disk.
        self.assertTrue(os.path.isfile(description_file), "No description file found")

        # Test 3: Verify that an otio file is created
        self.assertTrue(os.path.isfile(otio_file), "No otio file found")

        # Test 4: Verify that the clip has the correct media_reference.
        timeline = otio.adapters.read_from_file(otio_file)

        track = timeline.tracks[0]  # track contains clips (array)
        clip = track[0]

        self.assertEqual(
            clip.media_reference.target_url,
            video_file,
            "Clip has incorrect media_reference: {media_reference}".format(
                media_reference=clip.media_reference.target_url
            ),
        )

        markers = clip.markers
        self.assertEqual(
            len(markers),
            7,
            "Timeline object has incorrect number of markers: {num_markers}".format(
                num_markers=len(markers)
            ),
        )


if __name__ == "__main__":
    unittest.main()
