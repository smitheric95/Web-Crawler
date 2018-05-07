##TODO

- Report: 
    - Describe in detail what has changed
    - Describe decisions on how to handle questions in requirements
        - How did you determine the leader?
        - non-dict words: keep them (moore, etc) 
        - ignore stop words
        - what doc/query weighting scheme?
            - LTC.LTC
        - filters out terms that aren't in any of the documents
        - only documents whose score is > 0 are returned
        - score is zero if term doesn't appear in any documents
        - words in the title aren't part of the cosine similarity, only .25 is added
            
- Querying:
    - see example queries in requirements
  
- Cosine sim:
    - display score, doc url and title in descending order for top K=6 results
        - explain why you think these are correct
        - also display first 20 words in doc (can be stemmed)
        - If less than K/2 documents are returned for a query, rerun the query using thesaurus expansion.    
    
 - etc:
 *  - does 60 apply to pages crawled or documents collected??
  
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
    - test file i/o errors
    - run crawler w 60 docs
    - test validate query (changed split)
    - email prof query question
    
    
 questions for prof:
 
 - if a user enters "nice" should it be expanded to "nice beautiful fancy"?
 
 yes  - if you add .25, does that go over 1.0?
 x   - format of thesaurus as a CSV passed by optional command line argument?
 x   - do we need to keep things like showing the term frequency matrix? 
no they should be ignored    - how do duplicates come into play in clustering?
 x   - do stopwords and thesaurus HAVE to be passed to the program
 x   - what's the cos threshold for it a document is returned?