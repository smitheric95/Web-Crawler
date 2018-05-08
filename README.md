# Web Crawler/Search Engine
Eric Smith<br>
CSE 7337 - Info Retrieval and Web Search<br>
Southern Methodist University<br>
https://github.com/smitheric95/Web-Crawler<br>

## About
This project is a custom web crawler and search engine written in [Python 3](https://www.python.org/downloads/release/python-364/). 
It was meant for browsing content on the [course website](https://lyle.smu.edu/~fmoore/) for my 7337 Info Retrieval and Web Search class. 


It is an expansion on [Part 1](https://github.com/smitheric95/Web-Crawler/tree/part1), which was just a web crawler.

### Differences in Part 2
* Easier command line interface for executing the program
* The web crawler now clusters documents in addition to indexing them.
* Minor bug fixes for the crawler
* The program now features a search engine allowing the user to query the pages crawled.<br> (See Search Engine Implementation below)
* The index created from the crawler can now be imported and exported from disk.


### Main external libraries:
* [SciKit-Learn](http://scikit-learn.org/stable/) for Euclidean distance calculation.
* [Pickle](https://wiki.python.org/moin/UsingPickle) for importing and exporting the index.
* [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML parsing.
* [NLTK Porter Stemmer](http://www.nltk.org/api/nltk.stem.html) for stemming.
<br>

## How to Run 
#### Step 1 
Download [Python 3.6](https://www.python.org/downloads/release/python-364/). This is required to run the crawler.

#### Step 2 
Install [Python setuptools](https://pypi.python.org/pypi/setuptools).
On Linux, run the following command:
```commandline
sudo apt-get install python3-setuptools
```
#### Step 3
Navigate to the project folder and run the setup script as root. 
On Linux:

```commandline
cd Web-Crawler/
sudo python3 setup.py install
```
This will install all necessary dependencies to your local version of Python3. 
If you still have problems after running the setup file, you can install the dependencies yourself using [pip](https://pypi.org/project/pip/).

#### Step 4 
Now you can run the project:

```commandline
usage: SearchEngine.py [-h] [-p PAGELIMIT] [-s STOPWORDS] [-t THESAURUS]

Search Engine by Eric Smith - CSE 7337 Spring 2018

optional arguments:
  -h, --help            show this help message and exit
  -p PAGELIMIT, --pagelimit PAGELIMIT
                        Maximum number of pages to crawl. (Required)
  -s STOPWORDS, --stopwords STOPWORDS
                        Stop words file: a newline separated list of stop
                        words. (Default is Input/stopwords.txt)
  -t THESAURUS, --thesaurus THESAURUS
                        Thesaurus file: a comma separated list of words and
                        their synonyms. (Default is Input/thesaurus.csv)
```

Note: If you're using a Mac and you encounter an SSL Certificate warning, you may need to run the command listed in [this StackOverflow answer](https://stackoverflow.com/a/42098127/8853372).
<br>

## Running the Program
The program gives user a simple, command line interface to use. 

```commandline
$ python SearchEngine.py
----------------------------------------------------------------------
|    Eric's Search Engine                                            |
|                                                                    |
|    [0] Exit                                                        |
|    [1] Build Index                                                 |
|    [2] Search Documents                                            |
----------------------------------------------------------------------
Please select an option:  
```

### Running the Crawler
In order to start performing searches, you must first allow the crawler to build the index. Indexes can be built manually or imported from disk.

```commandline
Please select an option: 1
----------------------------------------------------------------------
Would you like to import the index from disk? (y/n) n

Seed URL: http://lyle.smu.edu/~fmoore
Page limit: 60
Stop words: Input/stopwords.txt
Thesaurus: Input/thesaurus.csv

Beginning crawling...

robots.txt: Disallowed['/~fmoore/dontgohere/'] Allowed[]

1. Visiting: /~fmoore/ (Freeman Moore - SMU Spring 2018)
2. Visiting: /~fmoore/index-fall2017.htm (Freeman Moore - SMU Fall 2017)
...
```

The output of the crawler will be displayed in real time in the terminal window from which the project is run. <br>
The crawler outputs:
1. The URL and title of each page
2. Outgoing, broken, and graphical (gif, jpg, jpeg, png) links
3. Page duplicates determined by hashing
4. 20 most common <i>stemmed</i> words and their document frequencies
5. Document clusterings around 5 random leader documents (Added in Part 2)

Also, a complete term frequency matrix will be exported to [Output/tf_matrix.csv](./Output/tf_matrix.csv).<br>
Users are given the option to export the index created to [Output/exported_index.obj](./Output/exported_index.obj).

<b>For an example of a complete output from the crawler, see [Output/Example Output.txt](./Output/Example%20Output.txt).</b> 

### Running the Search Engine

```commandline
----------------------------------------------------------------------
|    Eric's Search Engine                                            |
|                                                                    |
|    [0] Exit                                                        |
|    [1] Build Index                                                 |
|    [2] Search Documents                                            |
----------------------------------------------------------------------
Please select an option: 2
----------------------------------------------------------------------

Please enter a query or "stop": smu schedule
----------------------------------------------------------------------
1.	[0.3996]  SMU CSE 5337/7337 Spring 2018 Schedule (/~fmoore/schedule.htm)

	"smu cse preliminary schedule page maintained
	 latest schedule content and activities date topics
	 activity jan course overview introduction ir chpt"
```


## Crawler Implementation

#### Crawler Class
A WebCrawler object holds onto various forms of information about the pages it crawls.<br>
This information includes but is not limited to:
* <b>seed_url</b>: The starting URL used to initialize the crawler 
* <b>url_frontier</b>: A queue of pages to be crawled
* <b>robots_txt</b>: A dictionary containing directories that are either "Allowed" or "Disallowed"
* <b>visited_urls</b>: A dictionary containing visited links, their page titles, and a unique Document ID.
    * Document IDs are assigned by hashing the contents of a page 
* <b>duplicate_urls</b>: A dictionary containing DocumentIDs and arrays of the pages that produce that ID.
* <b>outgoing_urls</b>, broken_urls, and graphic_urls: Lists of various types of URLs picked up by the crawler
* <b>words</b>: A dictionary containing DocumentIDs and the valid words found in a page
* <b>frequency_matrix</b>: A 2D array of terms and their frequencies

#### Crawler Algorithm
In order to perform the basic operations of a crawler, I implemented a custom crawling method.

The crawl() method can be summarized as follows:
* Add the seed URL to the queue url_frontier
* While the queue isn't empty:
    * Pop the next URL from the queue
    * If the URL meets the requirements of the robots.txt file:
        * "Visit" the page using python's URL Library
        * Parse the contents of the page using Beautiful Soup:
            * Use regex to store the valid "words" of a page
            * Store necessary metadata about the page
            * Add valid, unvisited links links found in \<a> tags to the queue 
 
This crawler is <i>polite</i> in the sense that it checks the robots.txt file before visiting a page.<br>
It is also relatively <i>robust</i> as it is immune to duplicate and broken pages - both of which are reported when the crawler is finished.

The crawler also computes a term frequency matrix. Each unique word is stemmed with the NLTK Porter stemmer and its term and document frequencies are outputted.
Document clusterings are determined by picking 5 random leaders and assigning followers to the leaders of shortest Euclidean distance. 

## Search Engine Implementation 
