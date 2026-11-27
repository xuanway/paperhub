CPW-SMO: Generating Mask Sets and Common Source for Maximum Common Process Window
Authors：
[Hongquan He](https://63dac.conference-program.com/?post_type=page&p=15&uid=78003952228107280321)，[Ziyang Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=45839454402838021661)，[Jiaqi Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=301791953262832763)，[Bei Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=991243)，[Jingyi Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2434541213894243641)，[Hao Geng](https://63dac.conference-program.com/?post_type=page&p=15&uid=64456419866376934351)

## 中文标题

CPW-SMO：面向最大共同工艺窗口的掩模集与共同光源生成

## 英文摘要

Source Mask Optimization (SMO), as a key enabler in Design Technology Co-Optimization (DTCO), plays a vital role in enlarging the process window (PW) for advanced technology nodes and PDK development. Conventional SMO relies heavily on iterative optimization using lithography models to obtain a single source-mask pair for improved PW. In full-chip applications, however, a set of critical patterns are co-optimized under a common source, forming a one-source-to-many-masks optimization paradigm for maximum common process window (CPW). To overcome the limitations of existing methods, we introduce CPW-SMO, a novel single-shot generative flow that simultaneously generates an optimal source and a set of corresponding mask patterns using set-based attention mechanisms. Our approach formulates the source and mask patterns as a unified set and employs a highly parallelized generative simulator to enable efficient training. By transforming multi-objective, nondifferentiable CPW into a single-objective CPW preference penalty and optimizing generators through an SMO-aware gradient response method, CPW-SMO achieves nearly 2× CPW compared to state-of-the-art methods, while delivering ∼200× speedup in runtime. These improvements significantly boost the practicality and effectiveness of SMO for holistic lithography applications.

## 中文摘要

光源掩模优化（SMO）作为设计工艺协同优化（DTCO）的关键使能技术，在扩大先进技术节点的工艺窗口（PW）以及 PDK 开发中发挥着重要作用。传统 SMO 严重依赖使用光刻模型的迭代优化，以获得单一的源掩模对来改善 PW。然而在全芯片应用中，一组关键图案在共同光源下被协同优化，形成“一源多掩模”的优化范式，以实现最大共同工艺窗口（CPW）。为克服现有方法的局限，我们提出 CPW-SMO，一种新颖的单次生成式流程，它利用基于集合的注意力机制同时生成最优光源与一组相应的掩模图案。我们将光源与掩模图案建模为一个统一的集合，并采用高度并行化的生成式仿真器以实现高效训练。通过将多目标、不可微的 CPW 转化为单目标的 CPW 偏好惩罚，并借助 SMO 感知的梯度响应方法优化生成器，CPW-SMO 相比最先进方法实现了近 2 倍的 CPW，同时运行时间加速约 200 倍。这些改进显著提升了 SMO 在全景光刻应用中的实用性与有效性。
