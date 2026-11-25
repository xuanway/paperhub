Optimized Time-Dependent Hamiltonian Evolution Quantum Solver for Power System Transient Computations
Authors：
[Jiyuan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=94758750015791009731)，[Yongming Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=26385495698393920751)，[Baoping Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8699525323734165347)，[Mengdi Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=8594611422326624773)，[He Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=692143)

## 中文标题

面向电力系统暂态计算的优化时变哈密顿量演化量子求解器

## 英文摘要

Quantum computing has been demonstrated as a promising solution for computation-intensive power system electromagnetic transient (EMT) computation. However, existing work have focused on time-independent Hamiltonian evolution to solve ordinary differential equations (ODEs) with heavily classical interactions. This work proposes OHQS, an optimized time-dependent Hamiltonian evolution quantum solver, to enable high-accuracy computation for ODE-dominated EMT problems without classical iterations. The spatiotemporay mapping transformation is discretized to construct iterative quantum circuit evolution, leveraging the spatiotemporal fixed points (SFPs)-enabled automatic optimizer to reduce discretized errors. Experimental results have demonstrated that OHQS can support time-dependent Hamiltonian evolution in practical applications with up to 99.91% accuracy and achieve up to 9.56× error reduction compared to classical methods. The observed exponential decay of the relative error implies that consumed qubits scale as O(𝑙𝑜𝑔(1/𝜉)) and the 𝜉is the target relative error tolerance.

## 中文摘要

量子计算已被证明是求解计算密集型电力系统电磁暂态（EMT）问题的一种有前景的方案。然而，现有工作主要关注时间无关的哈密顿量演化，用以求解带有大量经典交互的常微分方程（ODE）。本文提出 OHQS，一种优化的时变哈密顿量演化量子求解器，可在无需经典迭代的情况下为以 ODE 为主的 EMT 问题实现高精度计算。通过对时空映射变换进行离散化，构建迭代式量子线路演化，并借助时空不动点（SFP）驱动的自动优化器降低离散化误差。实验结果表明，OHQS 能够在实际应用中支持时变哈密顿量演化，精度高达 99.91%，相较经典方法可将误差降低最多 9.56 倍。所观测到的相对误差指数衰减意味着消耗的量子比特数按 O(log(1/ξ))规模增长，其中ξ为目标相对误差容限。

## 英文关键词

Quantum Computing, Ordinary Differential Equations, Hamiltonian Evolution

## 中文关键词

量子计算、常微分方程、哈密顿量演化
