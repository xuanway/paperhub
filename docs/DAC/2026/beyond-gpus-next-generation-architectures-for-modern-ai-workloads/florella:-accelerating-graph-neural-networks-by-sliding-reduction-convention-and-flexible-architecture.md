Florella: Accelerating Graph Neural Networks by Sliding Reduction Convention and Flexible Architecture
Authors：
[Xiaobo Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3539575739763418804)，[Jianbin Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0829996901234782826)，[Lin Peng](https://63dac.conference-program.com/?post_type=page&p=15&uid=9332706764443995021)，[Yang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=59912665167421443011)，[Yixiang Di](https://63dac.conference-program.com/?post_type=page&p=15&uid=1776458110136497612)，[Chun Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4130046468738245906)

## 中文标题

Florella：基于滑动归约约定与灵活架构的图神经网络加速

## 英文摘要

The rapid evolution of graph neural networks (GNNs) has introduced diverse computational patterns beyond the message-passing paradigm. To support end-to-end inference, existing accelerators need to integrate heterogeneous, loosely-coupled components, incurring significant inter-accelerator communication and low performance density. This paper introduces Florella, an acceleration framework for unifying inconsistent computational patterns in end-to-end GNN inference. We first propose the sliding reduction convention, a declarative language that provides a flexible and hardware-friendly representation for diverse GNN operations. Building upon this, we design a versatile architecture that enables atomic mapping of macro-operations. This architecture is centered around a novel Jacobian-logarithm unit, which enables high hardware reuse across operators by leveraging logarithmic transformation and approximation. Evaluated across a range of GNN models, Florella achieves an average speedup of 2.2× and reduces memory traffic by 2× compared to four state-of-the-art accelerators, while improving performance density by 3.3×.

## 中文摘要

图神经网络（GNN）的快速演进带来了超越消息传递范式的多样化计算模式。为支持端到端推理，现有加速器需要集成异构、松耦合的组件，从而引入大量加速器间通信并导致较低的性能密度。本文提出 Florella，一个用于统一端到端 GNN 推理中不一致计算模式的加速框架。我们首先提出滑动归约约定（sliding reduction convention），这是一种声明式语言，为多样化的 GNN 操作提供灵活且硬件友好的表示。在此基础上，我们设计了一种通用架构，可实现宏操作的原子化映射。该架构以一种新颖的 Jacobian 对数单元（Jacobian-logarithm unit）为核心，通过利用对数变换与近似实现算子间的高度硬件复用。在一系列 GNN 模型上的评估表明，与四个最先进的加速器相比，Florella 平均实现 2.2 倍加速，内存流量降低 2 倍，同时性能密度提升 3.3 倍。
