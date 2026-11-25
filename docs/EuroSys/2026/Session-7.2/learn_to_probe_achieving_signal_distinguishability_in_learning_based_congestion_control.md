---
title: "Learn-to-Probe: Achieving Signal Distinguishability in Learning-based Congestion Control"
description: "EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control · Han Tian (University of Science and Technology of China), Wenbo Li (University o"
tags:
  - "EuroSys2026"
  - "Traffic Engineering, CDNs & Congestion Control"
---

# Learn-to-Probe: Achieving Signal Distinguishability in Learning-based Congestion Control

**中文标题：** Learn-to-Probe：在学习型拥塞控制中实现信号可区分性

**所属 Session：** [Session 7.2: Traffic Engineering, CDNs & Congestion Control](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Traffic Engineering, CDNs & Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control</p>
</div>

**作者**：Han Tian (University of Science and Technology of China), Wenbo Li (University of Science and Technology of China), Junxue Zhang (University of Science and Technology of China), Xudong Liao (Hong Kong University of Science and Technology), Decang Sun (Hong Kong University of Science and Technology), Donghui Chen (Huawei Technologies Co., Ltd.), Bin Huang (Huawei Technologies Co., Ltd.), Wenxue Li (Hong Kong University of Science and Technology), Yong Wang (Hong Kong University of Science and Technology), Kai Chen (Hong Kong University of Science and Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769317)

## 英文摘要

Internet congestion control remains a fundamental challenge, and recent learning-based congestion control algorithms (CCAs) have shown potential in optimizing network performance. However, their reliance on heuristically chosen input signals often leads to suboptimal behavior across diverse network conditions. In this paper, we identify the root cause as the lack of signal distinguishability–the ability of signals to reflect meaningful differences in network states. To address this, we propose Learn-to-Probe (LTP), a novel signal engineering paradigm that actively generates distinguishable network signals to improve the learning process. LTP (i) employs Bayesian filtering to accurately estimate network states from historical signals, and (ii) introduces an intrinsic reinforcement learning reward that encourages the flow to probe the network, inducing signal sequences that minimize the estimation uncertainty in (i). This probing behavior naturally enhances signal distinguishability, enabling the learning model to make more informed decisions. Extensive evaluations show that LTP consistently achieves high link utilization, low queuing delay, and stable convergence across diverse environments. Our results underscore the importance of signal distinguishability and offer a new direction for robust, adaptive congestion control.

## 中文摘要

互联网拥塞控制仍是一项根本性挑战，近期基于学习的拥塞控制算法（CCA）在优化网络性能方面展现出潜力。然而，它们依赖启发式选择的输入信号，往往导致在多样网络条件下出现次优行为。本文指出，其根本原因在于缺乏信号可区分性——即信号反映网络状态中有意义差异的能力。为解决此问题，我们提出 Learn-to-Probe（LTP），一种新的信号工程范式，主动生成可区分的网络信号以改进学习过程。LTP（i）采用贝叶斯滤波从历史信号中准确估计网络状态，（ii）引入一种内在强化学习奖励，鼓励流探测网络，从而诱导出最小化（i）中估计不确定性的信号序列。这种探测行为自然增强了信号可区分性，使学习模型能够做出更明智的决策。大量评估表明，LTP 在多样环境中始终实现高链路利用率、低排队延迟和稳定收敛。我们的结果强调了信号可区分性的重要性，并为鲁棒、自适应的拥塞控制提供了新方向。

**英文关键词：** Congestion Control, Machine Learning, Transport Protocol

**中文关键词：** 拥塞控制、机器学习、传输协议

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
