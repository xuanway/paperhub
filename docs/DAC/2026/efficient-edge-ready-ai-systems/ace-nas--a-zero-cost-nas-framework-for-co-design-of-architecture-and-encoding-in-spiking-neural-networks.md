ACE-NAS: A Zero-Cost NAS Framework for Co-Design of Architecture and Encoding in Spiking Neural Networks
Authors：
[Mingyu Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=70309462135736710001)，[Liangming Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=16608842566325588221)，[Wei Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=484733449217400082)，[Jinghai Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=43120785840247301761)，[shanlin xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=68337147787736825081)

## 中文标题

ACE-NAS：面向脉冲神经网络架构与编码协同设计的零成本 NAS 框架

## 英文摘要

Spiking Neural Networks (SNNs) promise exceptional energy efficiency for neuromorphic computing through event-driven processing. However, unlocking their full potential requires navigating a complex, strongly coupled design space of network topology and temporal neural encoding. Existing SNN Neural Architecture Search (NAS) frameworks typically decouple these dimensions, focusing exclusively on topology search while relying on manual, fixed encoding schemes. This limitation leaves a vast portion of the design space unexplored, resulting in sub-optimal energy-accuracy tradeoffs. To bridge this gap, we present ACE-NAS, the first zero-cost NAS framework that automates the co-design of SNN architecture and encoding mechanisms. Addressing the challenge of "encoding-blind" proxies, we introduce Jacob_cov, a novel Jacobian-based spectral metric that efficiently quantifies the temporal discriminability of different encoding schemes without training. ACE-NAS integrates Jacob_cov with structural proxies (ZiCo) into a hardware-aware, multi-objective evolutionary search strategy. On CIFAR-10, ACE-NAS achieves 92.95% accuracy, effectively identifying Pareto-optimal designs that balance high performance with minimal spike activity. By automating the joint optimization of structure and dynamics, ACE-NAS delivers an orders-of-magnitude reduction compared to standard training-based NAS and a 7× speedup over state-of-the-art efficient SNN-NAS methods (e.g., AutoSNN).

## 中文摘要

脉冲神经网络（SNN）通过事件驱动处理为神经形态计算带来卓越的能效前景。然而，要释放其全部潜力，需要在网络拓扑与时间神经编码这一高度耦合的复杂设计空间中进行探索。现有 SNN 神经架构搜索（NAS）框架通常将这些维度解耦，只关注拓扑搜索，而依赖人工设定的固定编码方案。这一局限使设计空间的很大一部分未被探索，导致能效-精度权衡次优。为弥合这一空白，我们提出 ACE-NAS，首个自动化 SNN 架构与编码机制协同设计的零成本 NAS 框架。针对“编码盲”代理指标的挑战，我们引入 Jacob_cov，一种新颖的基于 Jacobian 的谱度量，无需训练即可高效量化不同编码方案的时间可区分性。ACE-NAS 将 Jacob_cov 与结构代理指标（ZiCo）集成到硬件感知的多目标进化搜索策略中。在 CIFAR-10 上，ACE-NAS 达到 92.95% 精度，有效识别出兼顾高性能与最小脉冲活动的 Pareto 最优设计。通过自动化结构与动力学的联合优化，ACE-NAS 相比标准的基于训练的 NAS 带来数量级的降低，并相比最先进的高效 SNN-NAS 方法（如 AutoSNN）实现 7 倍加速。

## 英文关键词

Spiking Neural Network, Neural Architecture Search

## 中文关键词

脉冲神经网络、神经架构搜索
