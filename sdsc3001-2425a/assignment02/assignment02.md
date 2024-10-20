# SDSC3001 - Assignment 2

## Question 1

Suppose $A\:\in\mathbb{R}^{t\times d}$ ($d\:\gg t$) is a random projection matrix where each entry $A_{ij}$ is independently sampled from a standard normal distribution $\mathcal{N}\left(0,1\right)$. Let $a_i^T$ be the $i$-th row of $A$. Prove that the rows of $A$ are nearly orthogonal to each other, that is, $\text{Pr}\{\forall i \neq j, \frac{a_i^Ta_j}{d} \leq \epsilon\} \geq 1-\frac{t^2}{2\epsilon^2d}$.
(**Hint**: use the Chebyshev's inequality)

## Question 2

Given an undirected graph $G=\langle V,E\rangle$, we hope to partition $V$ into two disjoint sets $V_1$ and $V_2$ such that $cut\left(V_1,V_2\right)=\left|\{(u,v)\mid u \in V_1, v \in V_2, (u,v) \in E\}\right|$ is large. Suppose we randomly, uniformly, and independently assign each node $u\in V$ to $V_1$ or $V_2$ with equal probability. Prove that $E[cut(V_1,V_2)] \geq \frac{|E|}{2}$.

## Question 3

Write code to compute PageRank values of nodes in the DBLP network used in Assignment 1. You are required to upload your code for this question. Set \alpha=0.15.

### Question 3.0

Implement the power iteration method. Initialize the PageRank vector as
 where
 is the number of nodes. Let
 be the PageRank vector obtained after the
-th iteration and
 be the PageRank value of node
 after the
-th iteration. The power iteration method can be regarded as applying the following updating rule for iterations.

### Question 3.1

Implement the Monte Carlo method to approximate PageRank. Compare the PageRank vector computed by the power iteration method. The difference between $\pi$ and the PageRank vector approximated by the Monte Carlo method can be regarded as $\sum_v\left|\pi_v-\frac{f_v}{M}\right|$. Vary $M$ and report the values of $\sum_v\left|\pi_v-\frac{f_v}{M}\right|$ when $M=2n,\:4n,\:6n,\:8n,\:10n$.

### Question 3.2

In the above Monte Carlo method, we only use the stopping node to approximate PageRank which is wasteful as all the non-stopping nodes in random walks are ignored. Let $s_v$ be the number of times that $v$ appears in the $M$ random walk. Use $\frac{\alpha s_v}{M}$ to estimate the PageRank value of $v$. Report the values of $\sum_v\left|\frac{\alpha s_v}{M}-\pi_v\right|$ when $M=2n,\:4n,\:6n,\:8n,\:10n$.

### Question 3.3

Show that $\frac{\alpha s_v}{M}$ is an unbiased estimation of $\pi_v$ (the ground truth PageRank value of $v$), that is, $E\left[\frac{\alpha s_v}{M}\right]=\pi_v$.
