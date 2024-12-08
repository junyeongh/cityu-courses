# Question 1

To maintain $k$ uniform samples from a stream of elements $x_1, x_2, x_3, \ldots$, we use a **reservoir sampling algorithm**. Here's the step-by-step algorithm and a proof of correctness:

## Algorithm: Reservoir Sampling for $k$ Samples

1. **Initialization**:  
   Maintain a "reservoir" array of size $k$ to store the samples. As elements arrive:
   - If $t \le k$, directly add $x_t$ to the reservoir.
   - If $t > k$, proceed to Step 2.

2. **Sampling**:  
   For each incoming element $x_t$ where $t > k$:
   - Generate a random integer $r$ uniformly in the range $[1, t]$.
   - If $r \le k$, replace the $r$-th element in the reservoir with $x_t$.

3. **Output**:  
   At any time $t \ge k$, the reservoir contains $k$ uniform samples from the elements seen so far.

---

## Proof of Correctness

### **Objective**:

We need to show that at any time $t \ge k$, each element $x_i$ ($i \le t$) has a probability $\frac{k}{t}$ of being in the reservoir.

---

### **Base Case** ($t \le k$):

When $t \le k$, all elements are directly added to the reservoir. Thus, each element $x_i$ ($i \le t$) is in the reservoir with probability $1$. This satisfies $\frac{k}{t}$ since $t \le k$.

---

### **Inductive Case** ($t > k$):

Suppose at time $t-1$, each element $x_i$ ($i \le t-1$) is in the reservoir with probability $\frac{k}{t-1}$.

At time $t$, element $x_t$ arrives. We need to verify two conditions:

1. **Probability of $x_t$ being in the reservoir at time $t$**:
   - $x_t$ is added to the reservoir if the random integer $r \le k$, which happens with probability $\frac{k}{t}$.
   - Thus, $P(x_t \in \text{reservoir at time } t) = \frac{k}{t}$.

2. **Probability of $x_i$ ($i \le t-1$) remaining in the reservoir**:
   - At time $t-1$, $x_i$ is in the reservoir with probability $\frac{k}{t-1}$.
   - At time $t$, $x_i$ is replaced by $x_t$ if $r = j$, where $j$ is the index of $x_i$ in the reservoir. This occurs with probability $\frac{1}{t}$.
   - Thus, the probability of $x_i$ remaining in the reservoir is:
     \[
     P(x_i \text{ remains in reservoir at time } t) = P(x_i \text{ was in reservoir at } t-1) \cdot P(x_i \text{ not replaced by } x_t)
     \]
     \[
     = \frac{k}{t-1} \cdot \left(1 - \frac{1}{t}\right) = \frac{k}{t}.
     \]

---

### **Conclusion**:

By induction, at any time $t \ge k$, each element $x_i$ ($i \le t$) has a probability $\frac{k}{t}$ of being in the reservoir, as required.
