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
    def __init__(self, seed_url):
        self.seed_url = seed_url
        self.url_frontier = [] # list of urls not yet visited

    # Returns a dictionary of allowed and disallowed urls
    # Adapted from https://stackoverflow.com/a/43086135/8853372
    def get_robots_txt(self):
        # open seed url
        result = urllib.request.urlopen(self.seed_url + "/robots.txt").read()
        result_data_set = {"Disallowed": [], "Allowed": []}

        # for reach line in the file
        for line in result.decode("utf-8").split('\n'):
            if line.startswith("Allow"):
                result_data_set["Allowed"].append(
                    line.split(": ")[1].split('\r')[0])  # to neglect the comments or other junk info
            elif line.startswith("Disallow"):  # this is for disallowed url
                result_data_set["Disallowed"].append(
                    line.split(": ")[1].split('\r')[0])  # to neglect the comments or other junk info

        return result_data_set

if __name__ == "__main__":
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)

    crawler = WebCrawler("http://lyle.smu.edu/~fmoore")
    print(crawler.get_robots_txt())

