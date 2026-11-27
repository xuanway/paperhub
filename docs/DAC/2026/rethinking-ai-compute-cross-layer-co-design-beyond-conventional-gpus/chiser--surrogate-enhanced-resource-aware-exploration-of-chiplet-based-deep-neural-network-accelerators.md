ChiSER: Surrogate-Enhanced Resource-Aware Exploration of Chiplet-Based Deep Neural Network Accelerators
Authors：
[Yi-Cheng Lo](https://63dac.conference-program.com/?post_type=page&p=15&uid=6638870682926570236)，[Siva Satyendra Sahoo](https://63dac.conference-program.com/?post_type=page&p=15&uid=89620320209989280421)

## 中文标题

ChiSER：代理模型增强的芯粒级深度神经网络加速器资源感知探索

## 英文摘要

Co-designing chiplet-based neural-network accelerators spans partitioning, placement, dataflow, and microarchitecture under tight energy and latency limits. Fast system-level estimators scale to large searches but blur the intra-core effects that dominate energy. On the other hand, fine-grain reference models capture them but are too slow in the loop. We close this speed–fidelity gap with a coarse-to-fine flow, where a compact, architecture-aware surrogate of intra-core cost guides the global search, and only top designs are rechecked with the reference model. Our contributions include an energy-focused feature space and a lightweight predictor across Conv2D and GEMM-like workloads. On ResNet-50 and a Transformer, we reduce a manufacturing-weighted energy–delay objective by up to 62% and 44%, respectively, using the proposed approach.

## 中文摘要

芯粒级神经网络加速器的协同设计需在严苛的能耗与延迟约束下同时考虑划分、放置、数据流与微架构。快速的系统级估算器可支撑大规模搜索，却模糊了对能耗起主导作用的核内效应；而细粒度参考模型虽能刻画这些效应，却因速度过慢难以进入设计闭环。我们以由粗到细的流程弥合这一速度与保真度之间的差距：由一个紧凑的、架构感知的核内开销代理模型引导全局搜索，仅对最优的设计用参考模型复检。我们的贡献包括一个面向能耗的特征空间，以及覆盖 Conv2D 与类 GEMM 工作负载的轻量级预测器。在 ResNet-50 和一个 Transformer 上，采用所提方法分别将制造加权后的能耗-延迟目标最多降低 62%和 44%。

## 英文关键词

Design Space Exploration, Chiplets, Deep Neural Networks, Surrogate Modeling, ML for EDA

## 中文关键词

设计空间探索、芯粒、深度神经网络、代理模型、面向 EDA 的机器学习
