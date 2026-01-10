# Algebra - JEE Knowledge Base

## Quadratic Equations
### Standard Form
\[ ax^2 + bx + c = 0 \]
where \( a \neq 0 \).

### Roots
The roots are given by the quadratic formula:
\[ x = \frac{-b \pm \sqrt{D}}{2a} \]
where \( D = b^2 - 4ac \) is the discriminant.

### Nature of Roots
- **D > 0**: Roots are real and distinct.
- **D = 0**: Roots are real and equal (\( x = -b/2a \)).
- **D < 0**: Roots are complex conjugates (\( p \pm iq \)).
- **D is a perfect square**: Roots are rational (if a, b, c are rational).

### Properties of Roots
If \(\alpha, \beta\) are roots:
1.  Sum: \( \alpha + \beta = -b/a \)
2.  Product: \( \alpha\beta = c/a \)
3.  Difference: \( |\alpha - \beta| = \frac{\sqrt{D}}{|a|} \)

### Common Mistakes
> [!WARNING]
> - Forgetting \( a \neq 0 \) condition when solving parameter problems.
> - Not checking discriminant when asked for "real roots" (D ≥ 0).
> - Misusing \( \alpha - \beta \) formula (sign errors).

### Solution Template: Finding Parameter for Real Roots
1.  Write equation in standard form \( ax^2 + bx + c = 0 \).
2.  Calculate \( D = b^2 - 4ac \).
3.  Set \( D \geq 0 \) for real roots.
4.  Solve inequality for the parameter.

---

## Sequencing and Series (AP, GP, HP)

### Arithmetic Progression (AP)
- **nth term**: \( T_n = a + (n-1)d \)
- **Sum of n terms**: \( S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(a + l) \)
- **AM**: \( A = \frac{a+b}{2} \)

### Geometric Progression (GP)
- **nth term**: \( T_n = ar^{n-1} \)
- **Sum of n terms**: \( S_n = a\frac{r^n - 1}{r - 1} \) (for \( r \neq 1 \))
- **Sum to infinity**: \( S_\infty = \frac{a}{1 - r} \) (for \( |r| < 1 \))
- **GM**: \( G = \sqrt{ab} \)

### Harmonic Progression (HP)
- Reciprocals of terms are in AP.
- **HM**: \( H = \frac{2ab}{a+b} \)

### Relation between AM, GM, HM
\[ AM \geq GM \geq HM \]
(Equality holds when numbers are equal).

### Common Mistakes
> [!WARNING]
> - Using infinite GP formula when \( |r| \geq 1 \).
> - Confusing \( T_n \) and \( S_n \) formulas.
> - Forgetting that for AM-GM inequality, numbers must be **positive**.

---

## Binomial Theorem
\[ (x+y)^n = \sum_{r=0}^{n} \binom{n}{r} x^{n-r} y^r \]

### General Term
\[ T_{r+1} = \binom{n}{r} x^{n-r} y^r \]

### Important Properties
- Number of terms = \( n + 1 \)
- Sum of binomial coefficients: \( \sum_{r=0}^{n} \binom{n}{r} = 2^n \)
- Sum of coefficients with alternating signs: \( \sum_{r=0}^{n} (-1)^r \binom{n}{r} = 0 \)

### Finding Term Independent of x
1. Write general term \( T_{r+1} \).
2. Collect powers of x.
3. Set exponent of x to 0.
4. Solve for r.

---

## Logarithms
### Properties
1.  \( \log_a(xy) = \log_a x + \log_a y \)
2.  \( \log_a(x/y) = \log_a x - \log_a y \)
3.  \( \log_a(x^n) = n \log_a x \)
4.  **Change of Base**: \( \log_a b = \frac{\log_c b}{\log_c a} \)

### Domain Constraints
For \( \log_a x \) to be defined:
1.  \( x > 0 \)
2.  \( a > 0 \)
3.  \( a \neq 1 \)

### Common Mistakes
> [!WARNING]
> - Ignoring domain constraints (e.g. \( \log(x-2) \) implies \( x > 2 \)).
> - \( \log(x+y) \neq \log x + \log y \).
> - Confusing natural log (\(\ln\)) and base-10 log.
