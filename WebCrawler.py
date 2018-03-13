"""
Eric Smith
CSE 7337

Web Crawler
"""

import urllib.request
from bs4 import BeautifulSoup
import sys
import re
import urllib.parse
from furl import furl

class WebCrawler:
    def __init__(self, seed_url):
        self.seed_url = seed_url
        self.url_frontier = []  # list of urls not yet visited
        self.visited_urls = []
        self.visited_urls_content = []  # hash of content of urls visited
        self.outgoing_urls = []
        self.broken_urls = []
        self.graphic_urls = []
        self.words = {}  # DocumentID, [words]

    # print the report produced from crawling a site
    def __str__(self):
        report = ""
        return report

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

    # returns whether or not a url is valid
    # source: https://stackoverflow.com/a/7160778/8853372
    def url_is_valid(self, url_string):
        pattern = regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return bool(pattern.match(url_string))

    def url_is_within_scope(self, url_string):
        return "lyle.smu.edu/~fmoore" in url_string

    # crawls a site and returns a dictionary of information found
    def crawl(self):
        # dictionary containing information about the site

        robots_txt = self.get_robots_txt()

        self.url_frontier.append(self.seed_url)

        # while the queue is not empty
        # links in queue are valid, full urls
        while self.url_frontier:
            # current_page refers to the url of the current page being processed
            current_page = self.url_frontier.pop()  # select the next url
            self.visited_urls.append(current_page)

            # calculate present working directory
            pwd = "/".join(current_page.split("/")[:-1]) + "/"

            handle = urllib.request.urlopen(self.current_page)
            soup = BeautifulSoup(handle.read(), "lxml")

            for link in soup.find_all('a'):
                # current_url refers to the current link within the current page being processed
                current_url = link.get('href')

                # expand the url to include the domain
                if pwd not in current_url:
                    current_url = urllib.parse.urljoin(pwd, current_url)  # only works if the resulting link is valid

                # the link should be visited
                if self.url_is_valid(current_url):
                    # the link is within scope and hasn't been added to the queue
                    if self.url_is_within_scope(current_url) and current_url not in self.url_frontier:
                        # hasn't been visited
                        if current_url not in self.visited_urls:
                            self.url_frontier.append(current_url)
                    elif not self.url_is_within_scope(current_url):
                        self.outgoing_urls.append(current_url)
                # the link is broken
                elif current_url not in self.broken_urls:
                    self.broken_urls.append(current_url)

            break

if __name__ == "__main__":
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)

    crawler = WebCrawler("http://lyle.smu.edu/~fmoore")
    crawler.crawl()
    print(crawler)
