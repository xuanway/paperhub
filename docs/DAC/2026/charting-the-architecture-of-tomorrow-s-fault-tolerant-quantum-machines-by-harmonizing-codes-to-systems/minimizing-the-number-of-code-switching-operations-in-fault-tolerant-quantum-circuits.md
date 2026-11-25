Minimizing the Number of Code Switching Operations in Fault-Tolerant Quantum Circuits
Authors：
[Erik Weilandt](https://63dac.conference-program.com/?post_type=page&p=15&uid=66134466673493439)，[Tom Peham](https://63dac.conference-program.com/?post_type=page&p=15&uid=2814771622622502806)，[Robert Wille](https://63dac.conference-program.com/?post_type=page&p=15&uid=487643)

## 中文标题

最小化容错量子电路中的码切换操作数量

## 英文摘要

Fault-tolerant quantum computers rely on Quantum Error-Correcting Codes (QECCs) to protect information from noise. However, no single error-correcting code supports a fully transversal and therefore fault-tolerant implementation of all gates required for universal quantum computation. Code switching addresses this limitation by moving quantum information between different codes that, together, support a universal gate set. Unfortunately, each switch is costly—adding time and space overhead and increasing the logical error rate. Minimizing the number of switching operations is, therefore, essential for quantum computations using code switching. In this work, we study the problem of minimizing the number of code switches required to run a given quantum circuit. We show that this problem can be solved efficiently in polynomial time by reducing it to a minimum-cut instance on a graph derived from the circuit. Our formulation is flexible and can incorporate additional considerations, such as reducing depth overhead by preferring switches during idle periods or biasing the compilation to favor one code over another. To the best of our knowledge, this is the first automated approach for compiling and optimizing code-switching-based quantum computations at the logical level.

## 中文摘要

容错量子计算机依赖量子纠错码（QECC）来保护信息免受噪声影响。然而，没有任何单一纠错码能够支持通用量子计算所需全部门的完全横向、因而容错的实现。码切换通过在不同码之间移动量子信息来应对这一局限，这些码共同支持通用门集合。遗憾的是，每次切换代价高昂——增加时间与空间开销并提高逻辑错误率。因此，最小化切换操作数量对于使用码切换的量子计算至关重要。在本工作中，我们研究运行给定量子电路所需的最小码切换次数问题。我们证明，通过将该问题归约为由电路导出的图上的最小割实例，可在多项式时间内高效求解。我们的形式化表述具有灵活性，可以纳入额外考量，例如通过在空闲期优先切换来降低深度开销，或使编译偏向某一种码。据我们所知，这是首个在逻辑层面编译并优化基于码切换的量子计算的自动化方法。
