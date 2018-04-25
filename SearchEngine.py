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

    # def k_means(self):


    def display_menu(self):
        print("#######################################\n"
              "#    Eric's Search Engine             #\n"
              "#                                     #\n"
              "#    [0] Exit                         #\n"
              "#    [1] Build Index                  #\n"
              "#    [2] Search Documents             #\n"
              "#######################################\n")

        while True:
            # prompt user for initial menu selection
            main_menu_input = "-1"
            while main_menu_input.isdigit() is False or int(main_menu_input) not in range(0, 3):
                main_menu_input = input("\nPlease select an option: ")

            # user wants to crawl
            if int(main_menu_input) == 1:
                # print info about user choices
                [print("-", end="") for x in range(70)]
                print("\nSeed URL: " + self.seed_url)
                print("Page limit: " + str(self.page_limit))
                print("Stop words: " + str(self.stop_words_file))
                [print("-", end="") for x in range(70)]

                # build index
                print("\nBeginning crawling...\n")
                search_engine.crawl()
                print("\nIndex built.")

                # ask user if they want to see optional output
                info_input = "-1"
                while info_input != "y" and info_input != "n":
                    info_input = input("Would you like to see info about the pages crawled? (y/n)").lower()

                # show user crawler duplicates, broken urls, etc
                if info_input == "y":
                    search_engine.produce_duplicates()

                    [print("-", end="") for x in range(70)]
                    print(search_engine)
                    [print("-", end="") for x in range(70)]

                # ask user if they want to see tf matrix
                tf_input = "-1"
                while tf_input != "y" and tf_input != "n":
                    tf_input = input("\nWould you like to see a term frequency matrix? (y/n)").lower()

                # show user tf matrix
                if tf_input == "y":
                    [print("-", end="") for x in range(70)]
                    print("\n\nBuilding Term Frequency matrix...\n")

                    search_engine.build_frequency_matrix()

                    print("Most Common Stemmed Terms:\n")
                    print("{: <15} {: >25} {: >25}".format("Term", "Term Frequency", "Document Frequency"))
                    print("{: <15} {: >25} {: >25}".format("----", "--------------", "------------------"))
                    count = 1
                    for i, j, k in search_engine.n_most_common(20):
                        print("{: <15} {: >25} {: >25}".format((str(count) + ". " + i), j, k))
                        count += 1

                    [print("-", end="") for x in range(70)]

                    # export frequency matrix to file
                    f = open("tf_matrix.csv", "w")
                    f.write(search_engine.print_frequency_matrix())
                    f.close()
                    print("\n\nComplete frequency matrix has been exported to tf_matrix.csv")

            # user wants to enter search query
            elif int(main_menu_input) == 2:
                if len(self.visited_urls) == 0:
                    print("You must build the index first.")
                else:
                    # prompt user to enter query
                    query_input = input("\nPlease enter a query:")
                    print("You entered: " + query_input)
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

    # show main menu to user
    search_engine.display_menu()