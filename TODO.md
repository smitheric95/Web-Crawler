##TODO

- Report: 
    - Describe in detail what has changed
    - Describe decisions on how to handle questions in requirements
    
- Clustering:
    - Max 60 documents
    - Cluster in 5 leader/follower sets (K-Means?)
        - How did you determine the leader?
        - List leader-id, doc-id, and "score"? for each *pair*
        
- Querying:
    - accept multiple words from user
        - words are separated by spaces
        - "stop" stops the program 
    - handle non-dictionary words (ignore? or give suggestions?)
    - handle stop-words (ignore?)
    - see example queries in requirements
  
- Cosine sim
    - execute against query vs each leader document
    - what query weighting scheme?
    - if any query words in <title>, add +0.25 to score
    - display score, doc url and title in descending order for top K=6 results
        - explain why you think these are correct
        - also display first 20 words in doc (can be stemmed)
        - If less than K/2 documents are returned for a query, rerun the query using thesaurus expansion.    
    
 questions for prof:
    - if you add .25, does that go over 1.0?
    - format of thesaurus as a CSV passed by optional command line argument?
    - do we need to keep things like showing the term frequency matrix? 
    - how do duplicates come into play in clustering?