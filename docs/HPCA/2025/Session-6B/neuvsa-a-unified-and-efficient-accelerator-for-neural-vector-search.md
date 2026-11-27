---
title: "NeuVSA: A Unified and Efficient Accelerator for Neural Vector Search"
description: "HPCA 2025 · Next Big Bets"
tags:
  - "HPCA2025"
  - "Next Big Bets"
---

# NeuVSA: A Unified and Efficient Accelerator for Neural Vector Search

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Next Big Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Next Big Bets</p>
</div>

**论文链接**：
**作者**：Ziming Yuan (Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences), Lei Dai (Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences), Wen Li (Shanxi University), Jie Zhang (Peking University), Shengwen Liang (Institute of Computing Technology, Chinese Academy of Sciences), Ying Wang (Institute of Computing Technology, Chinese Academy of Sciences), Cheng Liu (Institute of Computing Technology, Chinese Academy of Sciences), Huawei Li (Institute of Computing Technology, Chinese Academy of Sciences), Xiaowei Li (Institute of Computing Technology, Chinese Academy of Sciences), Jiafeng Guo (Institute of Computing Technology, Chinese Academy of Sciences), Peng Wang (Huawei Technologies), Renhai Chen (Huawei Technologies), Gong Zhang (Huawei Technologies)
**会议**：HPCA 2025

---

## 中文标题

NeuVSA：面向神经向量检索的统一高效加速器

## 英文摘要

Neural Vector Search (NVS) has exhibited superior search quality over traditional key-based strategies for information retrieval tasks. An effective NVS architecture requires high recall, low latency, and high throughput to enhance user experience and cost-efficiency. However, implementing NVS on existing neural network accelerators and vector search accelerators is sub-optimal due to the separation between the embedding stage and vector search stage at both algorithm and architecture levels. Fortunately, we unveil that Product Quantization (PQ) opens up an opportunity to break separation. However, existing PQ algorithms and accelerators still focus on either the embedding stage or the vector search stage, rather than both simultaneously. Simply combining existing solutions still follows the beaten track of separation and suffers from insufficient parallelization, frequent data access conflicts, and the absence of scheduling, thus failing to reach optimal recall, latency, and throughput. To this end, we propose a unified and efficient NVS accelerator dubbed NeuVSA based on algorithm and architecture co-design philosophy. Specifically, on the algorithm level, we propose a learned PQ-based unified NVS algorithm that consolidates two separate stages into the same computing and memory access paradigm. It integrates an end-to-end joint training strategy to learn the optimal codebook and index for enhanced recall and reduced PQ complexity, thus achieving smoother acceleration. On the architecture level, we customize a homogeneous NVS accelerator based on the unified NVS algorithm. Each sub-accelerator is optimized to exploit all parallelism exposed by unified NVS, incorporating a structured index assignment strategy and an elastic on-chip buffer to alleviate buffer conflicts for reduced latency. All sub-accelerators are coordinated using a hardware-aware scheduling strategy for boosted throughput. Experimental results show that the joint training strategy improves recall by 4.6% over the separated strategy and accuracy by 43.5% over LUT-NN. NeuVSA achieves 2.82× to 416.17× lower latency over CPU, GPU, DFX+ANNA, and PQA+ANNA, and up to 49.60× and 10.57× higher average throughput over CPU and GPU, respectively. NeuVSA also reduces chip area by 65.2% over PQA+ANNA.

## 中文摘要

神经向量检索（NVS）在信息检索上的质量优于传统基于键的策略，其架构需兼具高召回率、低时延与高吞吐。然而，嵌入阶段与向量检索阶段在算法与架构层面相互分离，使 NVS 在现有加速器上实现并非最优。我们发现乘积量化（PQ）为打破这种分离提供了机会，但现有 PQ 方案只关注其中一个阶段，简单组合无法达到最优的召回率、时延与吞吐。为此，我们提出统一高效的 NVS 加速器 NeuVSA：算法层面提出基于可学习 PQ 的统一 NVS 算法，将两阶段整合到同一计算与访存范式，并以端到端联合训练学习最优码本与索引；架构层面定制同构 NVS 加速器，借助结构化索引分配、弹性片上缓存与硬件感知调度提升吞吐。实验表明，联合训练相比分离策略将召回率提升 4.6%，相比 LUT-NN 将精度提升 43.5%；NeuVSA 相比 CPU、GPU 与 PQA+ANNA 时延降低 2.82 倍至 416.17 倍，平均吞吐最高提升 49.60 倍与 10.57 倍，芯片面积比 PQA+ANNA 减少 65.2%。
