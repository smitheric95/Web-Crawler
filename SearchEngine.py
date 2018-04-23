"""
Eric Smith
CSE 7337

Search Engine
"""
import WebCrawler


class SearchEngine(WebCrawler):
    def __init__(self, seed_url, thesaurus):
        super().__init__(seed_url)
        self.thesaurus = thesaurus
