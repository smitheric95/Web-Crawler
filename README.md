#Web-Crawler

note: may need to run /Applications/Python\ 3.6/Install\ Certificates.command
	also: pip install validators, nltk.download() words

TODO:
- write report
- take user input of num pages and stop words
- bash script to install requirements
- finish crawler
- how to handle spreadsheets and pdfs?



crawler:
- url of each page
- outgoing links
- contents of title tag
- duplicate detection: "report if any urls refer to already seen content"
- broken links
- graphics (gif, jpg, jpeg, png)
- term-document frequency matrix
	- case insensitive matching
	- assign unique id to each doc
- 20 most common words
- ensure that only links in robots.txt are visited

data structure:

