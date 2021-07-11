


import os
import sys
import unittest


class YoutubeChaptersDemoTests(unittest.TestCase):

    def test_download_youtube_files(self):
        youtube_url = "RBSGKlAvoiM"
        video_file = youtube_url + ".mp4"


        # run the youtube_chapters_demo example...
        os.system("python3 ../src/youtube_chapters_demo.py %s" % youtube_url)


        # Tests

        # Test 1: Verify that an mp4 file is created disk. 
        self.assertTrue(os.path.isfile(video_file), "No video file found")


        # Test 2: Verify that a txt file is created on disk.



if __name__ == '__main__':
    unittest.main()


