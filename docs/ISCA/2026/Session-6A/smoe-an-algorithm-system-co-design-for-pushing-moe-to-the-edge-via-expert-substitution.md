---
title: "SMoE: An Algorithm-System Co-Design for Pushing MoE to the Edge via Expert Substitution"
description: "ISCA 2026 · Session 6A · SMoE: An Algorithm-System Co-Design for Pushing MoE to the Edge via Expert Substitution"
tags:
  - "ISCA2026"
  - "Session 6A"
  - "LLM 4"
---

# SMoE: An Algorithm-System Co-Design for Pushing MoE to the Edge via Expert Substitution

**中文标题：** SMoE: 通过专家替换将 MoE 推向边缘端的算法-系统协同设计

**所属 Session：** [Session 6A](index.md) · [ISCA 2026](../index.md)

**作者：** Guoying Zhu, Meng Li, Haipeng Dai, Xuechen Liu, Weijun Wang, Keran Li, Jun Xiao, Ligeng Chen, Wei Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The Mixture of Experts (MoE) architecture has emerged as a key technique for scaling Large Language Models by activating only a subset of experts per query. Deploying MoE on consumer-grade edge hardware, however, is constrained by limited device memory, making dynamic expert offloading essential. Unlike prior work that treats offloading purely as a scheduling problem, we leverage expert importance to guide decisions, substituting low-importance active experts with functionally similar ones already cached in GPU memory, thereby preserving accuracy. As a result, this design reduces memory usage and data transfer, while largely eliminating PCIe overhead. In addition, we introduce a scheduling policy that maximizes the reuse ratio of GPU-cached experts, further boosting efficiency. Our extensive evaluations show that, compared with state-of-the-art approaches, our method achieves a 48% reduction in decoding latency and maintains an expert cache hit rate above 60%, all while preserving nearly lossless accuracy.

## 中文摘要

专家混合（MoE）架构已成为扩展大语言模型的关键技术，其针对每次查询仅激活一部分专家。然而，在消费级边缘硬件上部署 MoE 受限于设备内存容量，因此动态专家卸载至关重要。与以往将卸载纯粹视为调度问题的研究不同，我们利用专家重要性来指导决策，用 GPU 内存中已缓存的功能相似的专家替代重要性低的激活专家，从而保持精度。由此，该设计减少了内存占用与数据传输，同时在很大程度上消除了 PCIe 开销。此外，我们提出一种调度策略，最大化 GPU 缓存专家的复用率，进一步提升效率。大量评估表明，与最先进方法相比，我们的方法将解码延迟降低 48%，专家缓存命中率保持在 60% 以上，同时几乎保持无损精度。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：goingshr/SMoE](https://github.com/goingshr/SMoE)
- [实验材料归档（Figshare）](https://doi.org/10.6084/m9.figshare.31982136)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2026](../index.md)
