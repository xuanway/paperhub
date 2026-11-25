A Hamiltonian-Guided Pre-Trainer for Variational Quantum Algorithms
Authors：
[Taotao Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5144400273364274978)，[He Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=692143)

## 中文标题

面向变分量子算法的哈密顿量引导预训练器

## 英文摘要

The optimization of variational quantum algorithms (VQAs) is notoriously challenging due to poor parameter initialization, which often traps optimizers in suboptimal local minima. Existing methods rely on a static guessing paradigm that is fundamentally limited. This paper presents a Hamiltonian-guided pre-trainer (HGP), a new approach that dynamically constructs a better starting point. HGP iteratively refines parameters by performing exact global optimization within low-dimensional subspaces. These subspaces are identified using a Hamiltonian-guided parameter blocking strategy, and the optimization is achieved by reconstructing the analytic landscape from a few quantum measurements via a Discrete Fourier Transform. We evaluated HGP on canonical spin models, where it consistently produced superior starting points for standard optimizers. Ablation studies reveal Hamiltonian-guided parameter blocking reduces the initial energy error by nearly 30-fold versus the second best benchmark. These results highlight the importance of Hamiltonian guided pre-training for enhancing VQA performance.

## 中文摘要

变分量子算法（VQA）的优化因参数初始化不佳而众所周知地困难，这常常使优化器陷入次优的局部极小值。现有方法依赖一种静态猜测范式，其能力存在根本性局限。本文提出哈密顿量引导预训练器（HGP），一种动态构建更优起始点的新方法。HGP 通过在低维子空间内执行精确全局优化来迭代精化参数。这些子空间借助哈密顿量引导的参数分块策略加以识别，而优化则通过离散傅里叶变换从少量量子测量中重建解析能量景观来实现。我们在典型自旋模型上评估了 HGP，它始终能为标准优化器给出更优的起始点。消融研究表明，与次优基准相比，哈密顿量引导的参数分块可将初始能量误差降低近 30 倍。这些结果凸显了哈密顿量引导预训练对提升 VQA 性能的重要性。

## 英文关键词

Quantum Computing, Variational Quantum Algorithms, Parameter Initialization, Optimization

## 中文关键词

量子计算、变分量子算法、参数初始化、优化
