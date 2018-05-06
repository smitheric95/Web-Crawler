##TODO

- Report: 
    - Describe in detail what has changed
    - Describe decisions on how to handle questions in requirements
        - How did you determine the leader?
        - non-dict words: keep them (moore, etc) 
        - ignore stop words
        - what doc/query weighting scheme?
            - LTC.LTC
            
- Querying:
    - see example queries in requirements
  
- Cosine sim:
    - display score, doc url and title in descending order for top K=6 results
        - explain why you think these are correct
        - also display first 20 words in doc (can be stemmed)
        - If less than K/2 documents are returned for a query, rerun the query using thesaurus expansion.    
    
 - etc:
    - add exceptions to parsing stopwords.txt and thesaurus.csv
    - should I stem words in the docs?
    - add user agent
    - replace all input instances with just one variable
        - make it a function?
    - clean up output 
        - make consistent
    - uncomment crawler main() code
    - adding line 161 on webcrawler made the program slow?
    - "building term freq matrix..." lags
    - add cache thing to gitignore
    - try entering query w space
    - "enter a query (stop to stop)"
    - shouldn't self.titles have duplicate urls?
    
    
 questions for prof:
 yes  - if you add .25, does that go over 1.0?
 x   - format of thesaurus as a CSV passed by optional command line argument?
 x   - do we need to keep things like showing the term frequency matrix? 
no they should be ignored    - how do duplicates come into play in clustering?
 x   - do stopwords and thesaurus HAVE to be passed to the program
 x   - what's the cos threshold for it a document is returned?