#Web-Crawler

note: may need to run /Applications/Python\ 3.6/Install\ Certificates.command
	also: pip install validators, nltk.download() words

TODO:
- write report
- bash script to install requirements
	- pycharm > tools > setup.py
- how to handle dictionary words and numbers?
	- re-read requirements for words
- include links not specifically in <a> tags
	- including graphics
- print status of crawler to user

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
- 20 most common stemmed words and their doc frequencies
- ensure that only links in robots.txt are visited


