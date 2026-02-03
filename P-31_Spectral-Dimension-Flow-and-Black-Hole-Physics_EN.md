# P-31 Spectral Dimension Flow and Black Hole Physics

**Author:** Bin Wang  
**Email:** wang.bin@foxmail.com  
**Date:** February 2026  
**Version:** v1.0.0  
**Series:** Fixed 4D Topology - Energy-Dependent Effective Dimension - Multiple Torsion Fractal Clifford Algebra Unified Field Theory  
**Category:** Physical Applications - Black Hole Theory and Quantum Gravity

---

## Abstract

Starting from the first principles of spectral dimension flow, this paper derives the effective dimension distribution equation near the horizon, proving that the "image frozen at the horizon edge" is a paradox of classical coordinate choice, not physical reality. By introducing the **spectral dimension gradient flow equation**, we show that the horizon is a **transition layer of Planck-scale thickness**, where the effective dimension smoothly transitions from $d_s = 4$ to $d_s = 2$, with information flowing continuously rather than freezing. The theory also predicts the spectral dimension correction to the Page curve during black hole evaporation, providing a physical picture for resolving the information paradox.

**Keywords:** Black hole, spectral dimension flow, horizon, information paradox, holographic principle

---

## 1. The Paradox of the Classical Horizon

### 1.1 The "Freezing" Phenomenon in Schwarzschild Coordinates

In classical general relativity, an external observer sees an object falling toward a black hole:
$$v_{\text{observed}} = \frac{dr}{dt} \xrightarrow{r \to 2GM} 0$$

The object appears to "freeze" at the horizon, never able to enter.

### 1.2 The Essence of the Paradox

This is actually a product of **coordinate choice**:
- Schwarzschild time $t$ diverges at the horizon
- But proper time $\tau$ remains finite
- The object itself **indeed** crosses the horizon

**Core Question:** How to naturally eliminate this paradox within the effective dimension framework?

---

## 2. Spectral Dimension Gradient Flow Equation

### 2.1 Basic Assumptions

**Assumption 1:** The effective dimension $d_s$ is a function of radial coordinate $r$ and energy scale $E$:
$$d_s = d_s(r, E)$$

**Assumption 2:** Spectral dimension flow follows the gradient flow equation:
$$\frac{\partial d_s}{\partial \ln r} = -\nabla_{\text{eff}} \cdot \mathbf{F}(d_s, r)$$

where $\mathbf{F}$ is the spectral dimension flow.

### 2.2 Spectral Dimension Distribution at the Horizon

In the static spherically symmetric case, derive the radial distribution of spectral dimension:
$$\frac{dd_s}{dr} = -\frac{\alpha}{r}(d_s - d_{\text{core}})(d_s - d_{\infty})$$

where:
- $d_{\infty} = 4$ (asymptotically flat)
- $d_{\text{core}} = 2$ (fractal core)
- $\alpha$ is the spectral dimension flow strength parameter

### 2.3 Analytical Solution

The solution to the equation is:
$$\boxed{d_s(r) = 3 + \tanh\left(\frac{r - r_s}{\Delta}\right)}$$

where:
- $r_s$: Horizon radius (transition layer center)
- $\Delta = \frac{2r_s}{\alpha(d_{\infty} - d_{\text{core}})}$: Transition layer thickness

**Key Results:**
- $r \gg r_s$: $d_s \to 4$ (classical spacetime)
- $r = r_s$: $d_s = 3$ (horizon center)
- $r \ll r_s$: $d_s \to 2$ (fractal core)

### 2.4 Thickness Estimate

$$\Delta \sim \frac{r_s}{\alpha}$$

For a solar-mass black hole:
- $r_s \sim 3$ km
- If $\alpha \sim 10^{38}$ (Planck scale ratio)
- $\Delta \sim 10^{-35}$ m (Planck length scale)

---

## 3. The Real Structure of the Horizon

### 3.1 Physical Picture of the Transition Layer

```
r → ∞:          d_s = 4  (classical spacetime)
    ↓
r = r_s + Δ:    d_s ≈ 3.76
    ↓
r = r_s:        d_s = 3   (horizon center)
    ↓
r = r_s - Δ:    d_s ≈ 2.24
    ↓
r → 0:          d_s = 2   (fractal core)
```

**Core Conclusion:** The horizon is not a surface, but a layer of finite thickness!

### 3.2 Continuity of Information Flow

Entropy flow density:
$$\mathbf{J}_S = -\frac{k_B}{\hbar} \nabla d_s$$

Since $\nabla d_s$ is finite, entropy flow is continuous, and information flows continuously.

---

## 4. Image Smoothing Mechanism

### 4.1 Light Propagation Equation

In the spectral dimension flow background, the group velocity of light:
$$v_g(r) = c \cdot \left(\frac{d_s(r)}{4}\right)^{\beta}$$

### 4.2 Correction to Redshift Factor

Classical redshift: $z_{\text{classical}} \to \infty$ (diverges)

Spectral dimension correction:
$$z_{\text{spectral}} \sim \ln\left(\frac{\Delta}{r - r_s}\right) \cdot \left(\frac{4}{d_s(r)}\right)^{\beta}$$

**Key Difference:** $z$ is finite but large, and behavior changes as $d_s \to 2$.

### 4.3 Continuous Disappearance of Images

The external observer sees:
1. **$r > r_s + \Delta$**: Normal image, slight redshift
2. **$r_s < r < r_s + \Delta$**: Rapid redshift, spectral dimension decreases
3. **$r = r_s$**: $d_s = 3$, image "blurs" rather than freezes
4. **$r < r_s$**: $d_s < 3$, image enters invisible region (not frozen, but dimension reduction prevents coupling)

**Not "stopping", but "fading into" fractal dimensions!**

---

## 5. Spectral Dimension Description of Black Hole Evaporation

### 5.1 Dimension Evolution During Evaporation

As the black hole evaporates (mass decreases):
- Early ($M \gg M_P$): $d_s \approx 4$ (classical)
- Middle ($M \sim M_P$): $d_s$ transitions from 4 to 2
- Late ($M \ll M_P$): $d_s \approx 2$ (quantum)

### 5.2 Spectral Dimension Correction to Hawking Radiation

Standard Hawking temperature:
$$T_H = \frac{\hbar c^3}{8\pi GM k_B}$$

Spectral dimension correction:
$$T_{\text{effective}} = T_H \cdot \frac{d_s - 2}{2}$$

**Important Results:**
- $d_s = 4$: Standard Hawking temperature
- $d_s = 3$: Half temperature
- $d_s = 2$: $T = 0$ (no radiation, stable information)

---

## 6. Information Conservation and Page Curve

### 6.1 Spectral Dimension Picture of Information Flow

$$|\Psi\rangle_{\text{initial}}^{(d_s=4)} \xrightarrow{\text{inter-dimensional flow}} \sum_i c_i |i\rangle_{d_s=2} \otimes |\text{rad}\rangle_{d_s=3}$$

- $|i\rangle_{d_s=2}$: Stored in fractal core
- $|\text{rad}\rangle_{d_s=3}$: Hawking radiation

### 6.2 Page Curve

Entanglement entropy evolution:
$$S_{\text{rad}}(t) = \min(S_{BH}(t), S_{\text{max}} - S_{BH}(t))$$

where:
$$S_{BH}(t) = \frac{k_B A(t)}{4\ell_P^2} \cdot f(d_s(t))$$

**Evolution Stages:**
- Early ($d_s \approx 4$): $S_{\text{rad}}$ increases (thermal radiation)
- Page time ($d_s = 3$): $S_{\text{rad}}$ reaches maximum
- Late ($d_s \to 2$): $S_{\text{rad}}$ decreases (information returns)

### 6.3 Spectral Dimension Interpretation of Complementarity Principle

- **External observer**: Sees information on horizon ($d_s = 2$)
- **Free-falling observer**: Crosses horizon, information continues to flow
- **Unified**: Not a contradiction, but different perspectives of the same physics

---

## 7. Experimental Simulation Schemes

### 7.1 Soft Boundary Potential Well Design

**Hyperbolic Tangent Potential Well:**
$$V(r) = V_0 \left[1 + \tanh\left(\frac{r - r_c}{\delta}\right)\right]$$

With damping:
$$\gamma(r) = \gamma_0 \left[1 - \tanh\left(\frac{r - r_c}{\delta}\right)\right]$$

### 7.2 Key to Avoiding "Freezing"

**Must use soft boundaries** (fractal structure):
- Soft boundary $\Rightarrow$ finite gradient $\nabla d_s$
- Finite gradient $\Rightarrow$ smooth transition

### 7.3 Measurement Scheme

1. **Infrared radiation temperature**: Measure "Hawking temperature"
2. **Information storage capacity**: Verify relationship with contact area
3. **Entropy flow continuity**: Measure inter-dimensional entropy production

---

## 8. Conclusion and Outlook

### 8.1 Main Results

1. **Horizon Equation**: $d_s(r) = 3 + \tanh((r-r_s)/\Delta)$
2. **Finite Thickness**: $\Delta \sim 10^{-35}$ m (Planck scale)
3. **Continuous Information**: Entropy flow $J_S = -(k_B/\hbar)\nabla d_s$ is finite
4. **Page Curve**: Inter-dimensional entanglement explains information return

### 8.2 Theoretical Significance

Under the "Fixed 4D Topology + Energy-Dependent Effective Dimension" paradigm:
- **No information loss**
- **No infinite redshift**
- **No coordinate paradox**

Only **smooth dimension transition** and **continuous information flow**.

### 8.3 Future Directions

1. Numerical simulation of dimension dynamics at the end of evaporation
2. Design of more precise tabletop experiments
3. Cross-validation with loop quantum gravity and string theory

---

## References

1. M-0.17 Spectral Dimension Flow Thermodynamics and Phase Transition Theory (Fundamental-Mathematics)
2. M-0.18 Spectral Dimension Flow Quantum Statistical Mechanics (Fundamental-Mathematics)
3. S. W. Hawking, "Particle Creation by Black Holes" (1975)
4. D. N. Page, "Information in black hole radiation" (1993)
5. A. Almheiri et al., "The entropy of Hawking radiation" (2020)

---

## Copyright Notice

This work is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0) License**.

---

**Author:** Bin Wang  
**Email:** wang.bin@foxmail.com
