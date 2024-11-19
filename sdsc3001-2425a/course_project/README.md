# MaxLogHash: A Memory-Efficient Sketch Method for Estimating High Similarities in Streaming Sets

[qyy0180/MaxLogHash: paper accepted by SIGKDD 2019](https://github.com/qyy0180/MaxLogHash)

paper accepted by SIGKDD 2019

Pinghui Wang, Yiyan Qi, Yuanming Zhang, Qiaozhu Zhai, Chenxu Wang, John C.S. Lui, Xiaohong Guan:
A Memory-Efficient Sketch Method for Estimating High Similarities in Streaming Sets

- **Introduction** (1)
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

## 1. Introduction

In the context of data science, 'sketching' refers to the process of compressing a dataset or data stream into a smaller representation so that we can efficiently 'reduce' the complexity of the dataset. The use cases of sketching are vast; frequency estimation such as Count-Min Sketch, heavy hitter identification, or matrix sketching that are discussed during last few lectures are some of the examples.

In this presentation, I will introduce a sketching technique called 'MaxLogHash' that is used to estimate the Jaccard similarity coefficient between two sets from a paper titled 'A Memory-Efficient Sketch Method for Estimating High Similarities in Streaming Sets'.

## 2. Jaccard similarity coefficient

In data science, we often deal with multiple datasets and there are cases we need to deal with their similarities. The spam filtering, for instance, starts with the idea where how similar an email that a user received is similar to the dataset of spam emails?

The Jaccard similarity coefficient is a measure of how similar two sets are, and it is defined as the size of the intersection divided by the size of the union of the two sets.

As the size `n` of the dataset gets large, we can intuitively think that it becomes computationally expensive to calculate the Jaccard similarity coefficient.

## 3. Sketching techniques for the Jaccard similarity coefficient estimation

In this paper, the authors introduces several sketching techniques to estimate the Jaccard similarity coefficient between two sets.

- MinHash
- b-bit MinHash => reduces the memory usage of MinHash, but fail to handle streaming sets
- Odd Sketch => reduces the memory usage of MinHash, but fail to handle streaming sets

The first technique is called 'MinHash', which is a set similarity estimation technique that is used to handle large sets.

MinHash is a set similarity estimation technique that is used to handle large sets.

---

## To-dos

- MinHash

## References

- Experimental dataset from the paper: found [Frequent Itemset Mining Dataset Repository](http://fimi.uantwerpen.be/data/)
