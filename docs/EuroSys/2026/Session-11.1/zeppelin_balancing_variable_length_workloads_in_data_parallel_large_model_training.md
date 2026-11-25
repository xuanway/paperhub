---
title: "Zeppelin: Balancing Variable-length Workloads in Data Parallel Large Model Training"
description: "EuroSys 2026 · Distributed Training & Collective Communication · Chang Chen (Peking University), Tiancheng Chen (ETH Zurich), Jiangfei Duan (CUHK"
tags:
  - "EuroSys2026"
  - "Distributed Training & Collective Communication"
---

# Zeppelin: Balancing Variable-length Workloads in Data Parallel Large Model Training

**中文标题：** Zeppelin：在数据并行大模型训练中均衡变长负载

**所属 Session：** [Session 11.1: Distributed Training & Collective Communication](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Training & Collective Communication。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Training & Collective Communication</p>
</div>

**作者**：Chang Chen (Peking University), Tiancheng Chen (ETH Zurich), Jiangfei Duan (CUHK), Qianchao Zhu (Peking University), Zerui Wang (Shanghai AI Laboratory), Qinghao Hu (MIT), Peng Sun (Shanghai AI Laboratory), Xiuhong Li (Peking University), Chao Yang (Peking University), Torsten Hoefler (ETH Zurich)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769369)

## 英文摘要

Training large language models (LLMs) with increasingly long and varying sequence lengths introduces severe load imbalance challenges in large-scale data-parallel training. Recent frameworks attempt to mitigate these issues through data reorganization or hybrid parallel strategies. However, they often overlook how computational and communication costs scale with sequence length, resulting in suboptimal performance. We identify three critical challenges: (1) varying computation-to-communication ratios across sequences of different lengths in distributed attention, (2) mismatch between static NIC–GPU affinity and dynamic parallel workloads, and (3) distinct optimal partitioning strategies required for quadratic attention versus linear components. To address these challenges, we present Zeppelin, a novel training system that integrates three key techniques: (1) a hierarchical sequence partitioning method for the attention module that reduces communication overhead and balances computation, supported by an efficient attention engine that applies divergent parallel strategies; (2) a routing layer that orchestrates inter-node transfers to fully utilize NIC bandwidth; and (3) a remapping layer that transforms sequence layouts between attention and linear modules, ensuring high computational efficiency across both. Comprehensive evaluations across diverse configurations show that Zeppelin delivers an average 2.80× speedup over state-of-the-art methods.

## 中文摘要

训练序列长度日益增长且不断变化的大语言模型（LLM），会在大规模数据并行训练中引入严重的负载不均衡挑战。近期框架尝试通过数据重组或混合并行策略缓解这些问题。然而，它们往往忽视了计算与通信开销如何随序列长度变化，导致性能次优。我们识别出三个关键挑战：（1）在分布式注意力中，不同长度序列的计算通信比不同；（2）静态NIC–GPU亲和性与动态并行负载之间不匹配；（3）二次注意力与线性组件所需的最优划分策略不同。为应对这些挑战，我们提出Zeppelin，一种新颖的训练系统，它集成三项关键技术：（1）面向注意力模块的分层序列划分方法，可降低通信开销并均衡计算，并由采用差异化并行策略的高效注意力引擎提供支持；（2）一个路由层，编排节点间传输以充分利用NIC带宽；（3）一个重映射层，在注意力模块与线性模块之间变换序列布局，确保两者都保持高计算效率。跨多种配置的全面评估表明，Zeppelin相较最先进方法平均取得2.80倍加速。

**英文关键词：** Machine Learning System, Large Model Training, Distributed System

**中文关键词：** 机器学习系统、大模型训练、分布式系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
