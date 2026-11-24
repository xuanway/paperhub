---
title: "HybridFlow: A Flexible and Efficient RLHF Framework"
description: "EuroSys 2025 · LLM Training · Guangming Sheng (The University of Hong Kong), Chi Zhang (ByteDance), Zilingfeng"
tags:
  - "EuroSys2025"
  - "LLM Training"
---

# HybridFlow: A Flexible and Efficient RLHF Framework

**中文标题：** 灵活高效的基于人类反馈的强化学习框架

**所属 Session：** [Session 9.2: LLM Training](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Training。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Training</p>
</div>

**作者**：Guangming Sheng (The University of Hong Kong), Chi Zhang (ByteDance), Zilingfeng Ye (ByteDance), Xibin Wu (ByteDance), Wang Zhang (ByteDance), Ru Zhang (ByteDance), Yanghua Peng (ByteDance), Haibin Lin (ByteDance), Chuan Wu (The University of Hong Kong)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696075)

## 英文摘要

Reinforcement Learning from Human Feedback (RLHF) is widely used in Large Language Model (LLM) alignment. Traditional RL can be modeled as a dataflow, where each node represents computation of a neural network (NN) and each edge denotes data dependencies between the NNs. RLHF complicates the dataflow by expanding each node into a distributed LLM training or generation program, and each edge into a many-to-many multicast. Traditional RL frameworks execute the dataflow using a single controller to instruct both intra-node computation and inter-node communication, which can be inefficient in RLHF due to large control dispatch overhead for distributed intra-node computation. Existing RLHF systems adopt a multi-controller paradigm, which can be inflexible due to nesting distributed computation and data communication. We propose HybridFlow, which combines single-controller and multi-controller paradigms in a hybrid manner to enable flexible representation and efficient execution of the RLHF dataflow. We carefully design a set of hierarchical APIs that decouple and encapsulate computation and data dependencies in the complex RLHF dataflow, allowing efficient operation orchestration to implement RLHF algorithms and flexible mapping of the computation onto various devices. We further design a 3D-HybridEngine for efficient actor model resharding between training and generation phases, with zero memory redundancy and significantly reduced communication overhead. Our experimental results demonstrate 1.53×∼20.57× throughput improvement when running various RLHF algorithms using HybridFlow, as compared with state-of-the-art baselines. HybridFlow source code is available at https://github.com/volcengine/verl

## 中文摘要

基于人类反馈的强化学习（RLHF）被广泛用于大语言模型（LLM）对齐。传统强化学习可以建模为数据流：每个节点表示一个神经网络（NN）的计算，每条边表示各 NN 之间的数据依赖。RLHF 使这一数据流更为复杂，每个节点扩展为一个分布式 LLM 训练或生成程序，每条边扩展为多对多组播。传统强化学习框架使用单一控制器执行数据流，同时指挥节点内计算和节点间通信；在 RLHF 中，由于分布式节点内计算的控制分发开销很大，这种方式可能效率低下。现有 RLHF 系统采用多控制器范式，但由于分布式计算与数据通信相互嵌套，这种方式可能不够灵活。我们提出 HybridFlow，以混合方式结合单控制器与多控制器范式，实现 RLHF 数据流的灵活表示与高效执行。我们精心设计了一组分层 API，将复杂 RLHF 数据流中的计算和数据依赖解耦并封装，从而支持高效的算子编排以实现 RLHF 算法，并支持将计算灵活映射到各种设备。我们还设计了 3D-HybridEngine，用于在训练与生成阶段之间高效地对 actor 模型重分片，实现零内存冗余并显著降低通信开销。实验结果表明，与最先进的基线相比，使用 HybridFlow 运行各种 RLHF 算法时吞吐量提升 1.53×∼20.57×。HybridFlow 源代码见 https://github.com/volcengine/verl

**英文关键词：** Distributed systems, Reinforcement Learning from Human Feedback

**中文关键词：** 分布式系统、基于人类反馈的强化学习

## 代码与研究制品

- 代码：[https://github.com/volcengine/verl](https://github.com/volcengine/verl)

以上链接来自论文现有摘要中的公开资料。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
