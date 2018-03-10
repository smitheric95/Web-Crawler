"""
Eric Smith
CSE 7337

Web Crawler
"""

import urllib.request
from bs4 import BeautifulSoup
import os
import sys

# seed_url = "http://lyle.smu.edu/~fmoore"
# handle = urllib.request.urlopen(seed_url)
#
# print(handle.read())
# soup = BeautifulSoup(handle.read(), "lxml")
#
# print(soup)
# https://s2.smu.edu/~fmoore/robots.txt

class WebCrawler:
    def __init__(self):
        print("web crawler")

    # Given a url for robots.txt, returns a dictionary of allowed and disallowed urls
    # https://stackoverflow.com/a/43086135/8853372
    def get_robots_txt(self, url):
        try:
            # open url
            result = os.popen("curl " + url).read()
            result_data_set = {"Disallowed": [], "Allowed": []}

            # for reach line in the file
            for line in result.split('\n'):
                if line.startswith("Allow"):
                    result_data_set["Allowed"].append(
                        line.split(": ")[1].split(' ')[0])  # to neglect the comments or other junk info
                elif line.startswith("Disallow"):  # this is for disallowed url
                    result_data_set["Disallowed"].append(
                        line.split(": ")[1].split(' ')[0])  # to neglect the comments or other junk info

            return result_data_set

        except Exception as e:
            print(e)

if __name__ == "__main__":
    print("running crawler")
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)
