# SDSC3001 - Assignment 1

![SDSC3001 - Assignment 1](<./SDSC3001 - Assignment 1.png>)

## Question 1

Prove that for any associate rule $X \to Y$ and $a \in X$, if we move the item a from $X$ to $Y$ , then the confidence of the new association rule$X - {a} -> Y \cup {a}$is at most the confidence of $X \to Y$.

ref. <- too trivial set theory question

## Question 2

Prove the Lower Tail of Chernoff bound

ref.

- [Chernoff bounds, and some applications](https://math.mit.edu/~goemans/18310S15/chernoff-notes.pdf) !this
- [CSE 312, Summer 2020](https://courses.cs.washington.edu/courses/cse312/20su/)
  - <https://courses.cs.washington.edu/courses/cse312/20su/files/student_drive/6.1.pdf>
  - <https://courses.cs.washington.edu/courses/cse312/20su/files/student_drive/6.2.pdf> !this
  - <https://courses.cs.washington.edu/courses/cse312/20su/files/student_drive/6.3.pdf>

## Question 3

There is a playlist of $n$ songs. A random music player randomly selects a song from the list to play (that is, each song is selected with probability $1/n$). Suppose that after listening to $T$ songs played by the random music player, all the $n$ songs have been played at least once.

Prove that

- (1) $E[T] \leq n \left(1 + \frac{1}{2} + \cdots + \frac{1}{n}\right) = nH_n$, where $H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$ is the $n$-th Harmonic number
- (2) $\text{Pr}\left(\left|T-nH_n\right|\ge cn\right)\le\frac{\pi^2}{6c^2}$
  - (Hint: $1+\frac{1}{2^2}+\frac{1}{3^2}+....=\frac{\pi^2}{6}$)

ref.

- EE3001: Chapter 4: Random Variables and Expectation

## Question 4

Let $\mathbf{P}$ be a $n\times n$ transition probability matrix, where $p_{ij}\ge0$ denotes the probability of directly jumping from $i$ to $j$, and $\sum^n_{j=1}p_{ij}=1$ for each row $i$. Prove that the eigenvalues of $\mathbf{P}$ are within the range [-1,1].

ref.

- [matrices - Eigenvalues of a transition probability matrix - Mathematics Stack Exchange](https://math.stackexchange.com/questions/1300345/eigenvalues-of-a-transition-probability-matrix)
- [linear algebra - How to prove that the matrix P has eigenvalues $1,-\frac{1}{2},\cdots,(-1)^{n-1}\frac{1}{n}$? - Mathematics Stack Exchange](https://math.stackexchange.com/questions/4254452/how-to-prove-that-the-matrix-p-has-eigenvalues-1-frac12-cdots-1n-1)
- [Perron–Frobenius theorem - Wikipedia](https://en.wikipedia.org/wiki/Perron–Frobenius_theorem)
- [[Linear Algebra] Lecture 24 마코브 행렬(Markov Matrix) :: Learn Again! 러너게인](https://twlab.tistory.com/53)
- [Lecture 24: Markov matrices; fourier series : 네이버 블로그](https://m.blog.naver.com/skkong89/221390722810)
  - <https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/c8a22883b5e0cc402b3df9c1d754ef5b_MIT18_06SCF11_Ses2.11sum.pdf>
  - [24. Markov Matrices; Fourier Series - YouTube](https://www.youtube.com/watch?v=lGGDIGizcQ0)

need to review linear algebra for sure

## Question 5

Denote by $d_v$ the degree of the node $v$, which is the number of neighbor nodes of $v$ in the graph. Let $n_v=\frac{d_v}{D}$ be the normalized degree of $v$, where $D=\sum_vd_v$ is the sum of the degrees of all nodes. We simulate a random walk with $M$ steps as follows:

- (1) the starting point is randomly selected (that is, each node is selected as the starting point with probability $\frac{1}{\left|V\right|}$ where $V$ is the set of all nodes), and
- (2) at each step, randomly jump to a neighbor node of the current node. Let $m_v$ be the number of times that $v$ is visited in the random walk. Denote by $\textbf{f}=\left(f_1,f_2,...,f_{\left|V\right|}\right)$ the empirical frequency vector, where $f_v=\frac{m_v}{M}$ Similarly, let $\textbf{n}=\left(n_1,n_2,...,n_{\left|V\right|}\right)$ be the normalized degree vector.

=>

- Write a program to simulate the above random walk and calculate the $\ell_1$-distance (rounded to three decimal places) between $n$ and $f$ ($\left|\textbf{n}-\textbf{f}\right|_1=\sum_v\left|n_v-f_v\right|$)
- Vary $M$ and report the values of the $\ell_1$-distance $\left|\textbf{n}-\textbf{f}\right|_1$ when $M=10^7,\:2\times10^7,\:3\times10^7,\:4\times10^7,\:5\times10^7$.
- Briefly summarize your findings and make a guess of the relationship between $n$ and $f$.
