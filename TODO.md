##TODO

- Report: 
    - Describe in detail what has changed
    - Describe decisions on how to handle questions in requirements
    
- Clustering:
    * based off the documents that were exported to tf_matrix.csv *
    - Max 60 documents
    - Cluster in 5 leader/follower sets 
        - what if there's not enough docs?
        - pick leaders, assign closest!
        - How did you determine the leader?
        - List leader-id, doc-id, and "score"? for each *pair*
        
- Querying:
    - accept multiple words from user
        - words are separated by spaces
        - "stop" stops the program 
    - handle non-dictionary words (ignore? or give suggestions?)
    - handle stop-words (ignore?)
    - see example queries in requirements
  
- Cosine sim:
    - execute against query vs each leader document
    - what query weighting scheme?
    - if any query words in <title>, add +0.25 to score
    - display score, doc url and title in descending order for top K=6 results
        - explain why you think these are correct
        - also display first 20 words in doc (can be stemmed)
        - If less than K/2 documents are returned for a query, rerun the query using thesaurus expansion.    
    
 - etc:
    - add exceptions to parsing stopwords.txt and thesaurus.csv
    - add clear output and show main menu to display_menu()
    - should I stem words in the docs?
    - add user agent
    - "press enter to continue" after printing optional info
    
 questions for prof:
 yes  - if you add .25, does that go over 1.0?
 x   - format of thesaurus as a CSV passed by optional command line argument?
 x   - do we need to keep things like showing the term frequency matrix? 
no they should be ignored    - how do duplicates come into play in clustering?
 x   - do stopwords and thesaurus HAVE to be passed to the program
 x   - what's the cos threshold for it a document is returned?