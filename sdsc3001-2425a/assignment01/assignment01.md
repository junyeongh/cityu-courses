# SDSC3001 - Assignment 1

[Assignment_1](./SDSC3001%20-%20Assignment%201.png)

## Question 1

An association rule $X \to Y$ is a rule where $X$ and $Y$ are disjoint itemsets. The confidence of the rule $X \to Y$ is defined as:

$$
\text{Conf}(X \to Y) = \frac{\text{Sup}(X \cup Y)}{\text{Sup}(X)}
$$

Then, moving an item $a \in X$ to the itemset $Y$ forms a new rule $(X - \{a\}) \to (Y \cup \{a\})$.

The confidence of this new rule using the formula is:

$$
\text{Conf}((X - \{a\}) \to (Y \cup \{a\})) = \frac{\text{Sup}((X - \{a\}) \cup (Y \cup \{a\}))}{\text{Sup}(X - \{a\})}
$$

Considering the property of union operator, $(X - \{a\}) \cup (Y \cup \{a\}) = X \cup Y$;
therefore, the numerator in the confidence of both rules remains the same:

In the meantime, the denominator for $(X - \{a\}) \to (Y \cup \{a\})$ becomes $\text{Sup}(X - \{a\})$.

Rewriting the confidence of the new rule:

$$
\text{Conf}((X - \{a\}) \to (Y \cup \{a\})) = \frac{\text{Sup}(X \cup Y)}{\text{Sup}(X - \{a\})}
$$

Since, $X - \{a\} \subseteq X$, every transaction that supports $X$ also supports $X - \{a\}$; therefore, $\text{Sup}(X) \leq \text{Sup}(X - \{a\})$, which implies:

$$
\frac{1}{\text{Sup}(X - \{a\})} \leq \frac{1}{\text{Sup}(X)}
$$

Given:

- $\text{Conf}((X - \{a\}) \to (Y \cup \{a\})) = \frac{\text{Sup}(X \cup Y)}{\text{Sup}(X - \{a\})}$
- $\text{Conf}(X \to Y) = \frac{\text{Sup}(X \cup Y)}{\text{Sup}(X)}$

This could be concluded:

$$
\text{Conf}((X - \{a\}) \to (Y \cup \{a\})) \leq \text{Conf}(X \to Y)
$$

## Question 2

(coin tosses)

The Lower Tail of Chernoff Bound is expressed as:
$$
\Pr(X \leq (1-\epsilon)\mu) \leq \exp\left(-\frac{\epsilon^2 \mu}{2}\right), 0 < \epsilon < 1
$$

- $X = \sum_{i=1}^n X_i$
- $\mu = \mathbb{E}[X]$

Using the fact that $ln(1 - x) \leq -x + \frac{x^2}{2}$ if $0 \leq x < 1$:

- $\Pr(X \leq (1-\epsilon)\mu) = \Pr(e^{-s X} \geq e^{-s(1-\epsilon)\mu}) \leq \frac{\mathbb{E}[e^{-s X}]}{e^{-s(1-\epsilon)\mu}}$ from Markov's Inequality.
- $\mathbb{E}[e^{-s X}] = \mathbb{E}[e^{-s \sum_{i=1}^n X_i}] = \prod_{i=1}^n \mathbb{E}[e^{-s X_i}]$
- $\mathbb{E}[e^{-s X_i}] \leq 1 - s \mathbb{E}[X_i] + \frac{s^2}{2} \mathbb{E}[X_i^2] \leq e^{-s \mathbb{E}[X_i] + s^2 / 2}$
  - $e^{-s X_i} = 1 - s X_i + \frac{(s X_i)^2}{2!} + \cdots \leq 1 - s X_i + \frac{s^2 X_i^2}{2}$
- $\mathbb{E}[e^{-s X_i}] \leq 1 - s p_i + \frac{s^2 p_i}{2}$
- Using $\ln(1-x) \leq -x + \frac{x^2}{2} \Rightarrow \ln(\mathbb{E}[e^{-s X_i}]) \leq -s p_i + \frac{s^2 p_i^2}{2}$
- Then, $\mathbb{E}[e^{-s X_i}] \leq e^{-s p_i + \frac{s^2 p_i}{2}}$ by taking exponentials on both sides.
- Therefore for all $i$, $\mathbb{E}[e^{-s X}] \leq \prod_{i=1}^n e^{-s p_i + \frac{s^2 p_i}{2}} = e^{-s \sum_i p_i + \frac{s^2 \sum_i p_i}{2}} = e^{-s \mu + \frac{s^2 \mu}{2}}$
- Solving it for $s$, $\Pr(X \leq (1-\epsilon)\mu) \leq \frac{e^{-s \mu + \frac{s^2 \mu}{2}}}{e^{-s (1-\epsilon)\mu}} = e^{s \epsilon \mu - \frac{s^2 \mu}{2}}$
  - Choosing $s = \epsilon$, $e^{\epsilon^2 \mu - \frac{\epsilon^2 \mu}{2}} = e^{-\frac{\epsilon^2 \mu}{2}}$, minimizes the expression

$\therefore \Pr(X \leq (1-\epsilon)\mu) \leq \exp\left(-\frac{\epsilon^2 \mu}{2}\right)$

## Question 3

## Question 4
