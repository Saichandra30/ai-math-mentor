# Calculus - JEE Knowledge Base

## Limits
### Standard Limits
1. \( \lim_{x \to 0} \frac{\sin x}{x} = 1 \)
2. \( \lim_{x \to 0} \frac{\tan x}{x} = 1 \)
3. \( \lim_{x \to 0} \frac{e^x - 1}{x} = 1 \)
4. \( \lim_{x \to 0} \frac{\ln(1+x)}{x} = 1 \)
5. \( \lim_{x \to a} \frac{x^n - a^n}{x - a} = n a^{n-1} \)

### L'Hopital's Rule
Used for \( \frac{0}{0} \) or \( \frac{\infty}{\infty} \) forms.
\[ \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} \]

### Common Mistakes
> [!WARNING]
> - Applying L'Hopital when limit is NOT indeterminate (e.g., \( 0/constant \)).
> - Forgetting chain rule during differentiation in L'Hopital.
> - Confusing \( \lim_{x \to \infty} \) with \( \lim_{x \to 0} \) standard forms.

---

## Derivatives (Differentiation)
### Chain Rule
\[ \frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x) \]

### Implicit Differentiation
If \( f(x,y) = 0 \), differentiate both sides w.r.t x, treating y as \( y(x) \).
Example: \( x^2 + y^2 = a^2 \implies 2x + 2y y' = 0 \implies y' = -x/y \).

### Applications of Derivatives
- **Tangent Equation**: \( y - y_1 = m(x - x_1) \) where \( m = f'(x_1) \)
- **Normal Equation**: \( y - y_1 = -\frac{1}{m}(x - x_1) \)
- **Increasing/Decreasing**: \( f'(x) > 0 \) (Inc), \( f'(x) < 0 \) (Dec)
- **Maxima/Minima**:
    1.  Find critical points where \( f'(x) = 0 \) or undefined.
    2.  Use **Second Derivative Test**:
        - \( f''(c) < 0 \implies \) Maxima
        - \( f''(c) > 0 \implies \) Minima
        - \( f''(c) = 0 \implies \) Test fails (use first derivative test)

---

## Indefinite Integrals
### Standard Forms
- \( \int x^n dx = \frac{x^{n+1}}{n+1} + C \) (\( n \neq -1 \))
- \( \int \frac{1}{x} dx = \ln|x| + C \)
- \( \int e^x dx = e^x + C \)
- \( \int \tan x dx = \ln|\sec x| + C \)
- \( \int \frac{dx}{a^2 + x^2} = \frac{1}{a} \tan^{-1}(\frac{x}{a}) + C \)
- \( \int \frac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1}(\frac{x}{a}) + C \)

### Integration by Parts
\[ \int u v dx = u \int v dx - \int \left( u' \int v dx \right) dx \]
**ILATE Rule** for priority of 'u':
Inverse, Logarithmic, Algebraic, Trigonometric, Exponential.

### Common Mistakes
> [!WARNING]
> - Forgetting the constant of integration (+C).
> - Incorrect choice of u and v in integration by parts.
> - Ignoring modulus in \( \ln|x| \).

---

## Definite Integrals
### Properties
1. \( \int_a^b f(x) dx = \int_a^b f(t) dt \) (Dummy variable)
2. \( \int_a^b f(x) dx = -\int_b^a f(x) dx \)
3. **King's Property**: \( \int_a^b f(x) dx = \int_a^b f(a+b-x) dx \)
   (Very useful for trigonometric integrals)
4. Odd function (\( f(-x) = -f(x) \)) on \([-a, a]\) \(\implies 0\)
5. Even function (\( f(-x) = f(x) \)) on \([-a, a]\) \(\implies 2\int_0^a f(x) dx\)

### Leibniz Rule (Differentiation under integral sign)
\[ \frac{d}{dx} \int_{\phi(x)}^{\psi(x)} f(t) dt = f(\psi(x)) \psi'(x) - f(\phi(x)) \phi'(x) \]

---

## Differential Equations
### Variable Separable
Rewrite as \( f(y) dy = g(x) dx \) and integrate.

### Linear Differential Equation (LDE)
Form: \( \frac{dy}{dx} + P(x)y = Q(x) \)
Integrating Factor (IF): \( e^{\int P(x) dx} \)
Solution: \( y(IF) = \int Q(x)(IF) dx + C \)

### Homogeneous Equation
Form: \( \frac{dy}{dx} = F(y/x) \). Put \( y = vx \).
