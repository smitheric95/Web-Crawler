##TODO

- Report: 
    - Describe in detail what has changed
    - Describe decisions on how to handle questions in requirements
        - How did you determine the leader?
            - Do you agree with the clustering? (kinda)
        - non-dict words: keep them (moore, etc) 
        - ignore stop words
        - what doc/query weighting scheme?
            - LTC.LTC
            - this does a reasonable job of returning docs, maybe not in perfect order
                - eg "smu schedule"
        - filters out terms that aren't in any of the documents
        - if the user enters a word not in the dictionary:
            - users must enter valid "words" (define words)
        - if a user enters a word not in any of the docs, it is thrown out
        - stop words are also thrown out, as they are not indexed
        - only documents whose score is > 0 are returned
        - score is zero if term doesn't appear in any documents
        - words in the title aren't part of the cosine similarity, only .25 is added
        - if a user enters "nice" it is expanded to "nice beautiful fancy"
        
     
 - etc:
    - remove name from output file
    - test example output link
    - finish readme
    - clean up output 
        - make consistent
    - uncomment crawler main() code
    - add cache thing to gitignore
    - test file i/o errors
    - delete todo
    - but in bold answers to questions?
