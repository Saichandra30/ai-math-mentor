# Linear Algebra (Matrices & Determinants) - JEE Knowledge Base

## Determinants
### Properties
1. \( |A^T| = |A| \)
2. \( |AB| = |A||B| \)
3. \( |kA| = k^n |A| \) (for \( n \times n \) matrix)
4. If two rows/cols are identical, determinant is 0.
5. Row operations \( R_i \to R_i + k R_j \) do NOT change determinant value.
6. **Area of Triangle**: \( \frac{1}{2} | \text{det matrix of coords} | \)

### Cramers Rule
For system \( AX = B \):
- \( x = D_x/D, y = D_y/D, z = D_z/D \)
- **Consistent**: \( D \neq 0 \) (Unique solution)
- **Inconsistent**: \( D = 0 \) and at least one \( D_i \neq 0 \) (No solution)
- **Infinite Solutions**: \( D = D_x = D_y = D_z = 0 \)

---

## Matrices
### Types
- **Symmetric**: \( A^T = A \)
- **Skew-Symmetric**: \( A^T = -A \) (Diagonal elements must be 0)
- **Orthogonal**: \( A A^T = I \) (Implies \( A^{-1} = A^T \))
- **Idempotent**: \( A^2 = A \)
- **Involutory**: \( A^2 = I \)
- **Nilpotent**: \( A^k = 0 \)

### Inverse and Adjoint
- \( A(\text{adj} A) = (\text{adj} A)A = |A| I \)
- \( A^{-1} = \frac{1}{|A|} (\text{adj} A) \)
- \( |\text{adj} A| = |A|^{n-1} \)
- \( \text{adj}(\text{adj} A) = |A|^{n-2} A \)
- \( (AB)^{-1} = B^{-1} A^{-1} \) (Reversal Law)

### System of Linear Equations (Matrix Method)
System \( AX = B \):
1.  Calculate \( |A| \).
2.  If \( |A| \neq 0 \), unique solution \( X = A^{-1}B \).
3.  If \( |A| = 0 \) and \( (\text{adj} A)B \neq 0 \), **No Solution**.
4.  If \( |A| = 0 \) and \( (\text{adj} A)B = 0 \), **Infinite Solutions** (usually).

### Common Mistakes
> [!WARNING]
> - Calculating \( (A+B)^{-1} \) as \( A^{-1} + B^{-1} \) (FALSE).
> - Forgetting scalar multiplier \( k^n \) when taking determinant of \( kA \).
> - Matrix multiplication is NOT commutative (\( AB \neq BA \)).

### Vectors (Basics)
- **Dot Product**: \( \mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta \)
- **Cross Product**: \( \mathbf{a} \times \mathbf{b} = |\mathbf{a}||\mathbf{b}|\sin\theta \hat{n} \)
- **Projection**: Proj of a on b = \( \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|} \)
- **Coplanar test**: Scalar Triple Product \( [\mathbf{a} \mathbf{b} \mathbf{c}] = 0 \)
