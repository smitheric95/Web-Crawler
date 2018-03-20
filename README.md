# Web Crawler
### Eric Smith
### CSE 7337


## About
This project is a custom web crawler written in [Python 3](https://www.python.org/downloads/release/python-364/). 
It was meant for browsing content on the [course website](https://lyle.smu.edu/~fmoore/) for my 7337 Info Retrieval and Web Search class.

Main external libraries: 
* [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML parsing.
* [NLTK Porter Stemmer](http://www.nltk.org/api/nltk.stem.html) for stemming.

## Crawler Implementation
- url of each page
- outgoing links
- contents of title tag
- duplicate detection: "report if any urls refer to already seen content"
- broken links
- graphics (gif, jpg, jpeg, png)
- term-document frequency matrix
	- case insensitive matching
	- assign unique id to each doc
- 20 most common stemmed words and their doc frequencies
- ensure that only links in robots.txt are visited


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
This will install all necessary dependencies to your local version of Python3. Alternatively, you can install the dependencies yourself using pip.

#### Step 4 
Now you can run the project:

```commandline
python3 WebCrawler.py <page limit> <stop words file>

python3 WebCrawler.py 20 stopwords.txt
```

Note: If you're using a Mac and you encounter an SSL Certificate warning, you may need to run the command listed in [this StackOverflow answer](https://stackoverflow.com/a/42098127/8853372)

## Output

The output of the crawler will be displayed in real time in the terminal window from which the project is run. 

An example output file is listed 



