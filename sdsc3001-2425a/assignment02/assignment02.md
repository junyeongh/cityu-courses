# SDSC3001 - Assignment 2

![Assignment_2](./SDSC3001%20-%20Assignment%202.png)

## Question 1

To prove that the rows of $A$ are nearly orthogonal to each other, Chebyshev's inequality is used.

For any two fixed rows i ≠ j: $a_i^Ta_j = \sum_{k=1}^d A_{ik}A_{jk}$. As each product $A_{ik}A_{jk}$ is a product of independent standard normal variables, the expected value is $E[A_{ik}A_{jk}] = E[A_{ik}]E[A_{jk}] = 0$ and the variance is $Var(A_{ik}A_{jk}) = E[A_{ik}^2]E[A_{jk}^2] = 1$

By the Central Limit Theorem, $\frac{a_i^Ta_j}{d}$ approaches $N(0,\frac{1}{d})$, since $\frac{a_i^Ta_j}{d}$ is a sum of d independent products divided by d.

By Chebyshev's inequality,

$$
\text{P}\left\{ \left| \frac{a_i^T a_j}{d} \right| \geq \epsilon \right\} \leq \frac{1}{\epsilon^2 d}
$$

There are $\frac{t(t-1)}{2}$ pairs of distinct rows. Using the union bound,

$$
\text{P}\left\{ \exists i \neq j, \left| \frac{a_i^T a_j}{d} \right| \geq \epsilon \right\} \leq \frac{t(t-1)}{2\epsilon^2 d}
$$

Since $t(t-1) \leq t^2$,

$$
\text{P}\left\{ \exists i \neq j, \left| \frac{a_i^T a_j}{d} \right| \geq \epsilon \right\} \leq \frac{t^2}{2\epsilon^2 d}
$$

Therefore,

$$
\text{P}\left\{ \forall i \neq j, \left| \frac{a_i^T a_j}{d} \right| \leq \epsilon \right\} \geq 1 - \frac{t^2}{2\epsilon^2 d}
$$

Hence, the rows of $A$ are nearly orthogonal to each other with high probability for the given condition when when d is large compared to t.

## Question 2

### Question 2.1

To show that the indicators $X_{uv}$'s for all edges are not mutually independent,consider a graph with three nodes, $a$, $b$, and $c$, and two edges $(a, b)$ and $(b, c)$. To define the indicators $X_{ab}$ and $X_{bc}$; $X_{ab} = 1$ if $(a, b)$ is a cut edge, $0$ otherwise, $X_{bc} = 1$ if $(b, c)$ is a cut edge, $0$ otherwise. The indicators are not mutually independent since the events $X_{ab} = 1$ and $X_{bc} = 1$ are not independent. For example, if $a$ and $b$ are in the same partition, then $(a, b)$ cannot be a cut edge, so $X_{ab} = 0$. But in this case, $b$ and $c$ must be in different partitions, so $(b, c)$ must be a cut edge, and $X_{bc} = 1$. Therefore, the events $X_{ab} = 0$ and $X_{bc} = 1$ are dependent, and the indicators are not mutually independent.

### Question 2.2

To show that the indicators $X_{uv}$'s for all edges are pairwise independent, we need to prove that for any two distinct edges $(u, v)$ and $(x, y)$, the random variables $X_{uv}$ and $X_{xy}$ are independent. Considering two distinct edges $(u, v)$ and $(x, y)$, the probability that $(u, v)$ is a cut edge is $P(X_{uv} = 1) = \frac{1}{2}$, as each node is assigned to $V_1$ or $V_2$ with equal probability.

Similarly, the probability that $(x, y)$ is a cut edge is $P(X_{xy} = 1) = \frac{1}{2}$. To show that $P(X_{uv} = i, X_{xy} = j) = P(X_{uv} = i) P(X_{xy} = j)$ for all $i, j \in \{0, 1\}$. This is true as the assignments of nodes to $V_1$ and $V_2$ are independent for each edge, so the events $X_{uv} = i$ and $X_{xy} = j$ are independent.

Therefore, the indicators $X_{uv}$'s for all edges are pairwise independent.

### Question 2.3

To prove that if we generate $k$ random and independent partitions of $V$, with probability at least $1-\frac{1}{k}$, among the $k$ random partitions we have a partition $V_1$ and $V_2$ such that $cut(V_1,V_2) \geq \frac{|E|-\sqrt{|E|}}{2}$, we can use the Markov inequality. Let $X = \sum_{(u,v) \in E} X_{uv}$ be the random variable representing the size of the cut. Knowing that $E[X] = \frac{|E|}{2}$, each edge has a probability of $\frac{1}{2}$ of being a cut edge.

Using Markov's inequality,
$P(X < \frac{|E|}{2} - \sqrt{|E|}) \leq \frac{E[X]}{\frac{|E|}{2} - \sqrt{|E|}} = \frac{1}{2 - \sqrt{\frac{1}{|E|}}}$

Then, by rearranging,
$P(X \geq \frac{|E|}{2} - \sqrt{|E|}) \geq 1 - \frac{1}{2 - \sqrt{\frac{1}{|E|}}}$

If we generate $k$ random and independent partitions, the probability that at least one of them has a cut of size at least $\frac{|E|}{2} - \sqrt{|E|}$ is:
$1 - \left(\frac{1}{2 - \sqrt{\frac{1}{|E|}}}\right)^k \geq 1 - \frac{1}{k}$

Therefore, with probability at least $1-\frac{1}{k}$, among the $k$ random partitions we have a partition $V_1$ and $V_2$ such that $cut(V_1,V_2) \geq \frac{|E|-\sqrt{|E|}}{2}$.
