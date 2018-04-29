"""
Eric Smith
CSE 7337

Search Engine
"""
from WebCrawler import WebCrawler
import pickle
import sys
import argparse
import numpy as np
import random
from sklearn.metrics.pairwise import euclidean_distances

class SearchEngine(WebCrawler):
    def __init__(self, seed_url):
        super().__init__(seed_url)
        self.thesaurus = None
        self.clusters = None  # {leader: [ (follower0, distance0) .. (followerN, distanceN) ]}

    def set_thesaurus(self, thesaurus):
        self.thesaurus = thesaurus

    # loads index from disk
    def load_index(self):
        try:
            f = open("exported_index.obj", "rb")
        except IOError:
            print("Error opening \"exported_index.obj\" :(")
            return 0

        tmp_dict = pickle.load(f)
        f.close()

        self.__dict__.update(tmp_dict)

    # saves index from disk
    def save_index(self):
        f = open("exported_index.obj", 'wb')
        pickle.dump(self.__dict__, f)
        f.close()

    """
    clusters tf matrix into k pairs of leaders and followers
    populates self.clusters
    """
    def cluster_docs(self, k=5):
        # transpose tf matrix
        X = np.matrix([list(x) for x in zip(*self.frequency_matrix)])

        # normalize term frequencies
        X_max, X_min = X.max(), X.min()
        X = (X - X_min) / (X_max - X_min)

        if len(X) < k:
            print("Warning: not enough documents to pick " + str(k) + " leaders.")
            k = int(len(X) / 2)
            print("Clustering around " + str(k) + " leaders.")

        # pick a random sample of k docs to be leaders
        leader_indices = random.sample(range(0, len(X)), k)
        follower_indices = list(set([i for i in range(len(X))]) - set(leader_indices))

        # stores leader: [(follower, distance)]
        clusters = {l: [] for l in leader_indices}

        # assign each follower to its closest leader
        for f in follower_indices:
            min_dist = sys.maxsize
            min_dist_index = -1

            for l in leader_indices:
                cur_dist = euclidean_distances(X[f], X[l])
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    min_dist_index = l

            clusters[min_dist_index].append((f, min_dist[0][0]))

        self.clusters = clusters

    def display_clusters(self):
        if self.clusters is not None:
            for leader, followers in self.clusters.items():
                print("Doc" + str(leader) + ":")
                for follower in followers:
                    print("\t\t+ Doc" + str(follower[0]) + " (Distance: " + str(follower[1]) + ")")
        else:
            print("Documents not yet clustered.")

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

            # user wants to build index (crawl)
            if int(main_menu_input) == 1:
                import_input = "-1"
                while import_input != "y" and import_input != "n":
                    import_input = input("Would you like to import the index from disk? (y/n)").lower()

                # import the index from file
                if import_input == "y":
                    self.load_index()

                # crawl site to build index
                else:
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

                    # build tf matrix to be used for clustering
                    [print("-", end="") for x in range(70)]
                    print("\n\nBuilding Term Frequency matrix...", end="")
                    search_engine.build_frequency_matrix()
                    print(" Done.")

                    # export frequency matrix to file
                    f = open("tf_matrix.csv", "w")
                    f.write(search_engine.print_frequency_matrix())
                    f.close()
                    print("\n\nComplete frequency matrix has been exported to tf_matrix.csv")

                    # ask user if they want to see tf matrix
                    tf_input = "-1"
                    while tf_input != "y" and tf_input != "n":
                        tf_input = input("\nWould you like to see the term frequency matrix? (y/n) \n\n").lower()

                    # show user tf matrix
                    if tf_input == "y":
                        print("Most Common Stemmed Terms:\n")
                        print("{: <15} {: >25} {: >25}".format("Term", "Term Frequency", "Document Frequency"))
                        print("{: <15} {: >25} {: >25}".format("----", "--------------", "------------------"))
                        count = 1
                        for i, j, k in search_engine.n_most_common(20):
                            print("{: <15} {: >25} {: >25}".format((str(count) + ". " + i), j, k))
                            count += 1

                        [print("-", end="") for x in range(70)]

                    # cluster docs
                    self.cluster_docs()

                    # ask user if they want to see clustering
                    c_input = "-1"
                    while c_input != "y" and c_input != "n":
                        c_input = input("\nDocuments clustered. Would you like to see their clustering? (y/n) \n\n").lower()

                    # show clustering
                    if c_input == "y":
                        self.display_clusters()

                    b_input = "-1"
                    while b_input != "y" and b_input != "n":
                        b_input = input("\nWould you like to export this index to disk? (y/n)").lower()

                    if b_input == "y":
                        self.save_index()
                        print("Exported to \"exported_index.obj\".")

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
    if int(argument.pagelimit) > 1:
        search_engine.set_page_limit(argument.pagelimit)

        if argument.stopwords:
            search_engine.set_stop_words(argument.stopwords)
        if argument.thesaurus:
            search_engine.set_thesaurus(argument.thesaurus)

        # show main menu to user
        search_engine.display_menu()
    else:
        print("Sorry. You must crawl a minimum of 2 pages. Otherwise, why would you need a search engine?")
