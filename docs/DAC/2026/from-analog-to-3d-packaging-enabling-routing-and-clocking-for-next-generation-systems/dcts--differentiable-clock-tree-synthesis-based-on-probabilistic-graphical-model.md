DCTS: Differentiable Clock Tree Synthesis Based on Probabilistic Graphical Model
Authors：
[han zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2034760935682449097)，[Junming Jiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=142843)，[Zhi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=8929691451404552405)，[Qixun Tian](https://63dac.conference-program.com/?post_type=page&p=15&uid=26099051383845364111)，[Peng Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=768143)

## 中文标题

DCTS：基于概率图模型的可微时钟树综合

## 英文摘要

Clock Tree Synthesis (CTS) constitutes a complex, discrete, and combinatorial multi-objective optimization (MOO) problem, which is typically fragmented into sequential steps, including clustering, topology generation, and buffering in traditional flows, trapping solutions in local optima. Despite significant potential in MOO, differentiable methods are inherently limited to represent dynamic topological adjustments during CTS. To solve this, we propose an end-to-end differentiable CTS framework, DCTS, based on Probabilistic Graphical Model (PGM) to re-parameterize the discrete topological search into a continuous gradient-based problem, enabling co-optimization of clock tree topology and buffer sizing within a global design space. The proposed DCTS was evaluated on ISCAS’89 and OpenCores benchmark circuits under the ASAP7 technology node. Experimental results show that it achieves competitive power, performance, and area (PPA) metrics against a leading commercial tool, along with a 2.78× speedup on large-scale circuits. Furthermore, when compared to state-of-the-art academic solutions, DCTS guarantees minimum improvements of 20% in delay, 17% in skew, 1% in power, and 17% in area, while also achieving a minimum speedup of 1.93× on large-scale designs.

## 中文摘要

时钟树综合（CTS）是一个复杂、离散且组合的多目标优化（MOO）问题，传统流程通常将其拆分为聚类、拓扑生成和缓冲器插入等串行步骤，致使解陷入局部最优。尽管可微方法在 MOO 方面具有显著潜力，但其在表示 CTS 过程中动态拓扑调整方面存在固有局限。为解决这一问题，我们提出了一种基于概率图模型（PGM）的端到端可微 CTS 框架 DCTS，将离散的拓扑搜索重新参数化为连续的基于梯度的问题，从而能够在全局设计空间内协同优化时钟树拓扑与缓冲器尺寸。在 ASAP7 工艺节点下，基于 ISCAS'89 和 OpenCores 基准电路对所提出的 DCTS 进行了评估。实验结果表明，相较于一款领先的商业工具，DCTS 在功耗、性能和面积（PPA）指标上具备竞争力，并在大规模电路上实现了 2.78 倍的加速。此外，与最先进的学术方案相比，DCTS 在延迟、偏斜、功耗和面积上分别至少改善 20%、17%、1%和 17%，同时在大规模设计上至少实现 1.93 倍的加速。

## 英文关键词

Clock Tree Synthesis, Probabilistic Graphical Model, Differentiable Optimization, Multi-Objective Optimization

## 中文关键词

时钟树综合、概率图模型、可微优化、多目标优化
