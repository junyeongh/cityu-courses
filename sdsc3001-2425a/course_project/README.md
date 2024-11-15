# SDSC3001 - Course Project

The [instruction](./SDSC3001%20-%20Course%20Project.md) for this assignment is found here.

There are:

- Presentation (12 mins)
  - (1) The big data problem in the research paper. What are the major challenges?
  - (2) The method developed to solve the problem.
    - What is the intuition of the method?
    - How does the method work? Any theoretical guarantees?
  - (3) The dataset(s) used in the paper and key statistics of the dataset(s).
  - (4) The experimental results.
  - (5) Any thoughts on the advantages and disadvantages as well as potential improvements of the proposed method? (optional)
- Report

Structure of both presentation and report will be

- **Introduction** (1)
  - 'In data science, we deal with multiple datasets and there are cases we need to deal with the similarities. The spam filtering, for instance, starts with the idea where how similar an email that a user received is similar to the dataset of spam emails?'
  - There are different approaches to determine how similar a certain dataset is similar to, and one metric to show the similarities are Jaccard similarity coefficient, which is defined as the ...
  - It is obvious when the size `n` of the dataset gets large, and MinHash is a set similarity estimation techique to handle larget sets.
- **Similarity matrix and their problems** (1)
  - *MinHash*
    - explanation
    - its problem
  - *b-bit MinHash*
    - explanation
    - its problem -> cannot be used for stream dataset
  - *Odd Sketch*
    - explanation
    - its problem -> cannot be used for stream dataset
- **MaxLogHash** (2)
  - <- 5x memory efficient than MinHash with the same accuracy and computational cost for estimating high similarities
- **Dataset & Result analysis** (3, 4)

The data is from [Frequent Itemset Mining Dataset Repository](http://fimi.uantwerpen.be/data/)
