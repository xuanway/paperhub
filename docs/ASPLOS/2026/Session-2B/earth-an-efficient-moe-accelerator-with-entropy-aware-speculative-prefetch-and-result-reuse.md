---
title: "EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse"
description: "ASPLOS 2026 · Session 2B · EARTH：一种具有熵感知投机预取与结果复用的高效 MoE 加速器"
tags:
  - "ASPLOS2026"
  - "Session 2B"
  - "Speculative Decoding"
---

# EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse

**中文标题：** EARTH：一种具有熵感知投机预取与结果复用的高效 MoE 加速器

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Fangxin Liu (Shanghai Jiao Tong University), Ning Yang (Shanghai Jiao Tong University), Jingkui Yang (National University of Defense Technology), Zongwu Wang (Shanghai Jiao Tong University), Chenyang Guan (Shanghai Jiao Tong University), Yu Feng (Shanghai Jiao Tong University), Li Jiang (Shanghai Jiaotong University), Haibing Guan (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；National University of Defense Technology；Shanghai Jiaotong University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790155) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Mixture-of-Experts (MoE) models significantly reduce computation in large language models by activating only a subset of experts per input token, but they introduce severe memory bottlenecks due to the large number of expert parameters. Existing offloading and prefetching strategies either incur accuracy loss, prohibitively high memory traffic, or high decoding overhead, limiting deployment on resource-constrained hardware. In this work, we present EARTH, a hardware–software co-design that addresses these challenges through three key innovations. First, we propose a dual-entropy encoding scheme that decomposes each expert into a high-information base and a delta component, enabling compact storage while preserving accuracy via adaptive precision management. Second, we introduce a deltaaware speculative prefetching and reuse mechanism that preloads base components of predicted experts and selectively fetches deltas, reusing previously computed delta patterns to reduce memory traffic and redundant computation. Third, we design a hardware accelerator that is co-designed to efficiently support this encoding and prefetching strategy, optimizing execution order, parallelism, and memory utilization. Across representative MoE workloads, EARTH reduces data movement overhead, improves prefetch efficiency, and achieves up to 2.10× speedup compared to state-of-the-art baselines, while maintaining high model accuracy.

## 中文摘要

混合专家（MoE）模型通过为每个输入 token 只激活一部分专家，显著减少了大型语言模型中的计算量，但由于专家参数数量庞大，它们引入了严重的内存瓶颈。现有的卸载与预取策略要么带来精度损失，要么造成过高的内存流量，要么产生高昂的解码开销，从而限制了在资源受限硬件上的部署。在本工作中，我们提出 EARTH，一种软硬件协同设计，通过三项关键创新应对这些挑战。第一，我们提出双熵编码方案，将每个专家分解为高信息量的基分量与增量分量，在通过自适应精度管理保持精度的同时实现紧凑存储。第二，我们引入增量感知的投机预取与复用机制，预加载被预测专家的基分量并有选择地获取增量，复用先前计算出的增量模式以减少内存流量与冗余计算。第三，我们设计了一款与该编码和预取策略协同设计的硬件加速器，以高效支持该策略，并优化执行顺序、并行度与内存利用率。在具有代表性的 MoE 工作负载上，EARTH 降低了数据搬移开销、提升了预取效率，相比最先进的基线最高实现 2.10× 加速，同时保持了较高的模型精度。

## 英文关键词

Mixture-of-Experts (MoE), accelerator, hardwaresoftware co-design, speculative prefetching

## 中文关键词

混合专家（MoE）；加速器；软硬件协同设计；投机预取

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790155)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2026](../index.md)
