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
        - if a user enters "nice" it is expanded to "nice beautiful fancy"
 
     
 - etc:
    - finish readme
    - clean up output 
        - make consistent
    - uncomment crawler main() code
    - add cache thing to gitignore
    - test file i/o errors
    - delete todo
