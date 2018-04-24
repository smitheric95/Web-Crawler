"""
Eric Smith
CSE 7337

Search Engine
"""
from WebCrawler import WebCrawler
import pickle
import sys
import argparse

class SearchEngine(WebCrawler):
    def __init__(self, seed_url):
        super().__init__(seed_url)
        self.thesaurus = None

    def set_thesaurus(self, thesaurus):
        self.thesaurus = thesaurus

    def display_menu(self):
        print("#######################################\n"
              "#    Eric's Search Engine             #\n"
              "#                                     #\n"
              "#    [0] Exit                         #\n"
              "#    [1] Build Index                  #\n"
              "#    [2] Search Documents             #\n"
              "#######################################\n\n")

        while True:
            # prompt user for initial menu selection
            main_menu_input = "-1"
            while main_menu_input.isdigit() is False or int(main_menu_input) not in range(0, 3):
                main_menu_input = input("Please select an option: ")

            # user wants to crawl
            if int(main_menu_input) == 1:
                print("building index...")
            # user wants to enter search query
            elif int(main_menu_input) == 2:
                if len(self.visited_urls) == 0:
                    print("You must build the index first.")
            else:
                break

        print("\nGoodbye!")
if __name__ == "__main__":
    # import crawler from file
    # f = open("crawler.obj", "rb")
    # search_engine = pickle.load(f)  # crawler.crawl()
    # f.close()

    search_engine = SearchEngine("http://lyle.smu.edu/~fmoore")

    # handle command line arguments
    parser = argparse.ArgumentParser(description="Search Engine by Eric Smith - CSE 7337 Spring 2018")
    parser.add_argument("-p", "--pagelimit", help="Maximum number of pages to crawl. (Required)", required=True, default="")
    parser.add_argument("-s", "--stopwords",
                        help="Stop words file: a newline separated list of stop words. (Default is stopwords.txt)", required=False, default="stopwords.txt")
    parser.add_argument("-t", "--thesaurus",
                        help="Thesaurus file: a comma separated list of words and their synonyms. (Default is thesaurus.csv)", required=False, default="thesaurus.csv")

    argument = parser.parse_args()

    # set attributes based off arguments
    search_engine.set_page_limit(argument.pagelimit)
    if argument.stopwords:
        search_engine.set_stop_words(argument.stopwords)
    if argument.thesaurus:
        search_engine.set_thesaurus(argument.thesaurus)




    search_engine.display_menu()