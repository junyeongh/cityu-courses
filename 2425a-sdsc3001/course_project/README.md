# MaxLogHash: A Memory-Efficient Sketch Method for Estimating High Similarities in Streaming Sets

- **Introduction** (1)
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

---

Unfortunately, the complexity of the naïve approach scales linearly with the number of stored elements
making it infeasible for large-scale datasets

이거랑 저거는 우리 수업 시간에 배웠던 스트리밍을 생각해보면 그런 문제가 있네?

그래서 이 새 알고리즘의 목표는 스트리밍 환경에서 쓸 수 있으면서 좀 더 효율적인 알고리즘이야

그래서 이 알고리즘에 대한 직관적인 아이디어는 똑같이 해쉬를 써.
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

- Paper: <https://arxiv.org/abs/1905.08977>
- Code
  - <https://github.com/ekzhu/datasketch/blob/master/datasketch/minhash.py>
  - <https://github.com/ekzhu/datasketch/blob/master/datasketch/hashfunc.py>
  - <https://docs.python.org/3/library/hashlib.html>
  - <https://github.com/hajimes/mmh3>
  - <https://github.com/qyy0180/MaxLogHash>
- Readings
  - <https://en.wikipedia.org/wiki/W-shingling>
  - <https://deepgram.com/ai-glossary/k-shingles>
