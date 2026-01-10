# Probability - JEE Knowledge Base

## Classical Probability
\[ P(A) = \frac{n(A)}{n(S)} \]
where \( n(A) \) is the number of favorable outcomes and \( n(S) \) is the total number of equally likely outcomes.

### Axioms
1. \( 0 \leq P(A) \leq 1 \)
2. \( P(S) = 1 \)
3. If \( A \cap B = \emptyset \), then \( P(A \cup B) = P(A) + P(B) \)

---

## Conditional Probability & Independence
### Conditional Probability
\[ P(A|B) = \frac{P(A \cap B)}{P(B)} \]
(Probability of A given B has occurred).

### Independent Events
Two events A and B are independent if:
\[ P(A \cap B) = P(A) \cdot P(B) \]
or equivalently \( P(A|B) = P(A) \).

> [!NOTE]
> Mutually Exclusive vs Independent:
> - Mutually Exclusive: \( A \cap B = \emptyset \) implies \( P(A \cap B) = 0 \).
> - Independent: \( P(A \cap B) = P(A)P(B) \neq 0 \) (usually).
> - **Error**: Confusing independent and mutually exclusive. They are rarely the same.

---

## Bayes' Theorem
Used to find reverse probability (Cause given Effect).
Let \( E_1, E_2, \dots, E_n \) be a partition of sample space S.
\[ P(E_i | A) = \frac{P(A | E_i) P(E_i)}{\sum_{j=1}^{n} P(A | E_j) P(E_j)} \]

### Template: Bayes' Problems
1.  Identify the mutually exclusive events \( E_1, E_2, \dots \) (Hypotheses).
2.  Identify the common event A (Evidence).
3.  Calculate Priors \( P(E_i) \) and Likelihoods \( P(A|E_i) \).
4.  Apply formula.

---

## Probability Distributions
### Binomial Distribution
For n independent trials with success prob p:
\[ P(X = r) = \binom{n}{r} p^r (1-p)^{n-r} \]
- **Mean**: \( np \)
- **Variance**: \( npq \) (where \( q = 1-p \))
- **Mode**: \( \lfloor (n+1)p \rfloor \)

### Common Mistakes
> [!WARNING]
> - Confusing "at least one" (\( 1 - P(\text{none}) \)) with summing many terms.
> - Forgetting \( \binom{n}{r} \) coefficient in binomial problems.
> - Using Binomial for dependent events (Use Hypergeometric, or logic).

---

## Permutation & Combination (Basics for Probability)
- **Selection**: \( \binom{n}{r} = \frac{n!}{r!(n-r)!} \) (Order doesn't matter)
- **Arrangement**: \( P(n, r) = \frac{n!}{(n-r)!} \) (Order matters)
- **Arrangement in a Circle**: \( (n-1)! \)

### Distributing Objects
- **Identical Objects into Distinct Groups**: \( \binom{n+r-1}{r-1} \) (Stars and Bars)
- **Distinct Objects into Distinct Groups**: \( r^n \) (each object has r choices)
