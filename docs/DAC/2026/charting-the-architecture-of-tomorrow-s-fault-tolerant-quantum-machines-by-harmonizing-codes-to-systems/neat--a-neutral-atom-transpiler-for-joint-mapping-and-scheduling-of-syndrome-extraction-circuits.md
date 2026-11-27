NEAT: A Neutral-Atom Transpiler for Joint Mapping and Scheduling of Syndrome Extraction Circuits
Authors：
[Dingchao Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=52266196590711740811)，[Kai Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0474100528237401706)，[Sanjiang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=788243)，[Shenggang Ying](https://63dac.conference-program.com/?post_type=page&p=15&uid=55310813763969621711)，[Fangming Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=53218853326290288141)，[Jianxin Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=4313246786885282846)

## 中文标题

NEAT：用于伴随式提取电路联合映射与调度的中性原子转译器

## 英文摘要

Quantum Error Correction (QEC) demands efficient implementation of syndrome extraction circuits. However, existing compilers for neutral-atom processors largely miss the opportunity to co-optimize these circuits by exploiting both the structural properties of Quantum Error-Correcting Codes (QECCs) and the physical constraints of neutral-atom architectures. In this work, we introduce NEAT, an SMT-based compiler that jointly optimizes qubit mapping and syndrome extraction scheduling for a broad class of stabilizer-based QECCs, achieving depth-optimal execution with minimal shuttling overhead on neutral-atom platforms. Across a wide range of QECCs, NEAT consistently achieves near-optimal circuit depth and reduces atom movement by 3×–30× compared the baseline compiler Enola. Logical-level simulations further demonstrate 2×–20× lower logical error rates under realistic hardware noise. A hierarchical symmetry-breaking formulation and relaxed parallel-motion constraints substantially improve solver scalability, yielding up to 100× speedup in compilation time. Together, these results show that NEAT produces depth-optimal, movement-efficient, and logically robust syndrome extraction schedules, while scaling effectively to large QECCs on neutral-atom hardware.

## 中文摘要

量子纠错（QEC）要求高效实现伴随式提取电路。然而，现有的中性原子处理器编译器在很大程度上错失了同时利用量子纠错码（QECC）的结构特性与中性原子架构物理约束来协同优化这些电路的机会。在本工作中，我们提出 NEAT，一个基于 SMT 的编译器，针对广泛的基于稳定子的 QECC 联合优化量子比特映射与伴随式提取调度，在中性原子平台上实现深度最优的执行，并将移动开销降至最低。在多种 QECC 上，NEAT 一致地达到近最优的电路深度，相比基线编译器 Enola 将原子移动减少 3×–30×。逻辑级仿真进一步表明，在真实硬件噪声下逻辑错误率降低 2×–20×。分层对称性破除的建模与松弛的并行移动约束显著提升了求解器的可扩展性，使编译时间最高加速 100×。这些结果共同表明，NEAT 生成的伴随式提取调度具有深度最优、移动高效和逻辑鲁棒的特点，同时能够在中性原子硬件上有效扩展到大型 QECC。

## 英文关键词

Quantum Error Correction, Neutral-Atom Quantum Computing, SMT-based Compilation

## 中文关键词

量子纠错、中性原子量子计算、基于 SMT 的编译
