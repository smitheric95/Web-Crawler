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
import hashlib

class WebCrawler:
    def __init__(self, seed_url):
        self.seed_url = seed_url
        self.robots_txt = None
        self.url_frontier = []  # list of urls not yet visited
        self.visited_urls = {}  # URL : (Title, DocumentID) (hash of content of a visited URL)
        self.duplicate_urls = {}    # DocumentID : [URLs that produce that ID]
        self.outgoing_urls = []
        self.broken_urls = []
        self.graphic_urls = []
        self.words = {}  # DocumentID : [words]

    # print the report produced from crawling a site
    def __str__(self):
        report = " seed_url: " + self.seed_url \
                 + "\n\n robots_txt: " + "[" + ''.join('{}{}'.format(key, val) for key, val in self.robots_txt.items()) \
                 + "\n\n url_frontier: " + "[" + " ".join(self.url_frontier) + "]" \
                 + "\n\n visited_urls: " + str(self.visited_urls) \
                 + "\n\n outgoing_urls: " + "[" + " ".join(self.outgoing_urls) + "]" \
                 + "\n\n broken_urls: " + "[" + " ".join(self.broken_urls) + "]" \
                 + "\n\n graphic_urls: " + "[" + " ".join(self.graphic_urls) + "]" \
            # + "\n\n words: " +  "[" + " ".join(self.words)

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
                    self.seed_url + line.split(": ")[1].split('\r')[0]
                )  # to neglect the comments or other junk info
            elif line.startswith("Disallow"):  # this is for disallowed url
                result_data_set["Disallowed"].append(
                    self.seed_url + line.split(": ")[1].split('\r')[0]
                )  # to neglect the comments or other junk info

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
            r'(?:/?|[/?]\S+)$',
            re.IGNORECASE)

        return bool(pattern.match(url_string))

    # returns whether or not the url is within the scope of the seed url
    def url_is_within_scope(self, url_string):
        return self.seed_url in url_string

    '''
    produces a list of duplicate documents
    populates self.duplicate_urls with DocumentID : [URLs that produce that ID]
    '''
    def produce_duplicates(self):
        # self.visited_urls = {}  # URL : (Title, DocumentID) (hash of content of a visited URL)
        duplicates = {}

        # populate duplicates with DocumentID : [URLs]
        for url, (title, docID) in self.visited_urls:
            duplicates[url] = docID

        return duplicates

    # crawls a site and returns a dictionary of information found
    def crawl(self):
        # dictionary containing information about the site

        self.robots_txt = self.get_robots_txt()

        self.url_frontier.append(self.seed_url + "/")

        '''
        pop from the URL frontier while the queue is not empty
        links in queue are valid, full urls
        '''
        while self.url_frontier:
            # current_page refers to the url of the current page being processed
            current_page = self.url_frontier.pop()  # select the next url

            # calculate present working directory
            pwd = "/".join(current_page.split("/")[:-1]) + "/"

            if pwd not in self.robots_txt["Disallowed"]:
                try:
                    # hit the current page
                    handle = urllib.request.urlopen(current_page)

                # basic HTTP error e.g. 404, 501, etc
                except urllib.error.HTTPError as e:
                    if current_page not in self.broken_urls:
                        self.broken_urls.append(current_page)
                else:
                    # convert url to BeautifulSoup
                    soup = BeautifulSoup(handle.read(), "lxml")

                    # hash the content of the page to produce a unique DocumentID
                    current_content = hashlib.sha224(soup.contents[0].text.encode('utf-8')).hexdigest()

                    # grab the title of the page, store file name if title isn't available (e.g. PDF file)
                    current_title = soup.title.text if soup.title is not None else current_page.replace(pwd, '')

                    # mark that the page has been visited by adding to visited_url
                    self.visited_urls[current_page] = (current_title, current_content)

                    print("visiting: " + current_page + " (" + current_title + ")")

                    for link in soup.find_all('a'):

                        # current_url refers to the current link within the current page being processed
                        current_url = link.get('href')

                        # expand the url to include the domain
                        if pwd not in current_url:
                            # only works if the resulting link is valid
                            current_url = urllib.parse.urljoin(pwd, current_url)

                        # the link should be visited
                        if self.url_is_valid(current_url):

                            # the link is within scope and hasn't been added to the queue
                            if self.url_is_within_scope(current_url) and current_url not in self.url_frontier:

                                # ensure the hasn't been visited before adding it to the queue
                                if current_url not in self.visited_urls.keys():
                                    self.url_frontier.append(current_url)

                            elif not self.url_is_within_scope(current_url):
                                self.outgoing_urls.append(current_url)

                        # the link is broken
                        elif current_url not in self.broken_urls:
                            self.broken_urls.append(current_url)

            else:
                print("not allowed: " + current_page)
        print("done crawling")


if __name__ == "__main__":
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)

    crawler = WebCrawler("http://lyle.smu.edu/~fmoore")
    crawler.crawl()
    print(crawler)
    duplicates = crawler.produce_duplicates()
    print("done")