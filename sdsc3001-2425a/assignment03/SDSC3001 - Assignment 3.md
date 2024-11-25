# SDSC3001 - Assignment 3

## Question 1

Design a sampling algorithm to maintain $k$ uniform samples from a stream of elements $x_1,x_2,x_3,...$. Prove the correctness of your algorithm, that is, your algorithm can guarantee that at any time point $t \ge k$ (the time we have received $x_1,x_2,...,x_t$) the probability that $x_i$ ($i\le t$) is kept as a sample is $\frac{k}{t}$.

## Question 2

Download the file "trans.txt" and implement a streaming algorithm for mining the top-$k$ most frequent patterns. In the data file "trans.txt", every line is a transaction represented by a set of item ids and the largest transaction contains $15$ items.

### Part A

Prove that to mine top-$k$ most frequent patterns, we do not need to consider patterns of size greater than $m=\lceil\log_2\left(k+1\right)\rceil$.

### Part B

Apply the idea of the Misra–Gries Algorithm to mine approximate frequent patterns by scanning each transaction only once. Specifically, implement your algorithm as follows.

- Maintain at most $C$ counters. Each counter is a (key, value) pair where "key" represents a specific pattern and "value" indicates the corresponding (approximate) support of the pattern.
- When reading a transaction, enumerate all its subsets of size at most $m$. Suppose for the $i$-th transaction we have $L_i$ such valid subsets and clearly, $L_i=\sum_{j=1}^{\min(l_i, m)} {l_i \choose j}$ where $l_i$ is the size of the $i$-th transaction. Transform the $i$-th transaction to a stream of $L_i$ subsets (the order could be arbitaray) and use the Misra–Gries Algorithm to count each subset's number of appearances (support).

#### b.1

Suppose in total we have $M$ transactions. Let $L=\sum_{i=1}^ML_i$. Suppose $f_S$ is the real support of a pattern $S$ and $\hat{f}_S$ is the approximate support maintained by your Misra–Gries Algorithm. Prove that for any pattern $S$, we have that $f_S \geq \hat{f}_S \geq f_S-\frac{L}{C+1}$.

#### b.2

Suppose $S^k$ is the real $k$-th most frequent pattern. Let $\hat{f}^k$ be the $k$-th largest (approximate) support obtained by your Misra–Gries Algorithm. Prove that $f_{S^k} \geq \hat{f}^k \geq f_{S^k}-\frac{L}{C+1}$.

#### b.3

Since we only have the approximate supports of patterns obtained by our Misra–Gries Algorithm, we can only use such approximate supports to return approximate top-$k$ patterns. We hope to collect all the true top-$k$ patterns by returning a collection of patterns $A=\{S \mid \hat{f}_S \geq t\}$ where $t$ is a threshold for us to filter out non-frequent patterns. Prove that if we set $t=\hat{f}^k-\frac{L}{C+1}$, we can guarantee that:

- The returned pattern collection $A$ has 100% recall. This means that if for a pattern $S$, $f_S \geq f_{S^k}$, then $S \in A$
- The minimum support of patterns in $A$, denoted by $minSup(A)=\min_{S \in A} f_S$, is at least $f_{S^k}-\frac{2L}{C+1}$. That is, $minSup(A) \geq f_{S^k}-\frac{2L}{C+1}$.

#### b.4

Set $k=500$. Run your Misra–Gries Algorithm on the "trans.txt" dataset and report the values of $L$ and $minSup(A)$ when setting $C=500000, 750000, 1000000$. To compute $minSub(A)$, you can refer to the file "patterns_Apriori.txt" containing all the frequent patterns of support at least $21$. Each line of "patterns_Apriori.txt" is in the form $id_1,id_2,...,id_l:sup$, where $id_1,id_2,...,id_l$ denotes a pattern $\{id_1,id_2,...,id_l\}$ and $sup$ is the support of this pattern. (Hint: the file "patterns_Apriori.txt" contains enough information. If your algorithm returns some pattern that is not in the "patterns_Apriori.txt" file, probably your algorithm is not implemented correctly.)
