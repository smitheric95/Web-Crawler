##TODO

- Report: 
    - Describe in detail what has changed
    - Describe decisions on how to handle questions in requirements
        - How did you determine the leader?
        - non-dict words: keep them (moore, etc) 
        - ignore stop words
        - what doc/query weighting scheme?
            - LTC.LTC
            - this does a reasonable job of returning docs, maybe not in perfect order
        - filters out terms that aren't in any of the documents
        - only documents whose score is > 0 are returned
        - score is zero if term doesn't appear in any documents
        - words in the title aren't part of the cosine similarity, only .25 is added
        - if a user enters "nice" should it is expanded to "nice beautiful fancy"
            
 - etc:
 *  - does 60 apply to pages crawled or documents collected??
    - clean up output 
        - make consistent
    - uncomment crawler main() code
    - "building term freq matrix..." lags
    - add cache thing to gitignore
    - try entering query w space
    - "enter a query (stop to stop)"
    - shouldn't self.titles have duplicate urls?
    - test file i/o errors
    - run crawler w 60 docs 