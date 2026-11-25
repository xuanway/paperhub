---
title: "MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production"
description: "EuroSys 2026 · LLM Training at Scale · Chunyu Xue (Shanghai Jiao Tong University), Yangrui Chen (ByteDance Seed), Jiany"
tags:
  - "EuroSys2026"
  - "LLM Training at Scale"
---

# MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production

**中文标题：** MegaScale-Omni：面向生产环境多模态 LLM 训练的超大规模、工作负载弹性系统

**所属 Session：** [Session 3.1: LLM Training at Scale](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Training at Scale。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Training at Scale</p>
</div>

**作者**：Chunyu Xue (Shanghai Jiao Tong University), Yangrui Chen (ByteDance Seed), Jianyu Jiang (ByteDance Seed), Ningxin Zheng (ByteDance Seed), Junda Feng (ByteDance Seed), Jingji Chen (ByteDance Seed), Shixiong Zhao (ByteDance Seed), Shen Yan (Bytedance seed), Yi Lin (ByteDance Seed), Lei Shi (Bytedance Seed), Zanbo Wang (ByteDance Seed), Lishu Luo (ByteDance Seed), Faming Wu (ByteDance Seed), Haibin Lin (ByteDance Seed), Yanghua Peng (ByteDance Seed), Xin Liu (ByteDance Seed), Quan Chen (Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803587)

## 英文摘要

As the foundational component of versatile AI applications, training an multimodal large language model (MLLM) relies on multimodal datasets with dynamic modality mixture proportions and sample length distributions. However, existing MLLM systems remain inefficient under dynamic workloads, due to statically coupled decisions of resource allocation and model parallelization between encoders and the LLM backbone. This paper presents MegaScale-Omni, an industrial-grade MLLM training system tailored for dynamic workload adaption and hyper-scale deployment. MegaScale-Omni is built upon the training scheme of encoder-LLM multiplexing with three key innovations: (1) Decoupled parallelism strategies with long-short sequence parallelism for encoders to process variable-length samples, and full-fledged 5D parallelism for the LLM backbone, both organized under a communication-efficient parallelization layout. (2) Unified encoder-LLM representations for flexible, extensible colocation, and a new paradigm of encoder-LLM joint pipeline with workload resilience. (3) Workload balancing techniques via decentralized grouped reordering in data loaders and adaptive resharding from encoder to LLM ranks. MegaScale-Omni is deployed as the foundation of our in-house largescale MLLM training tasks with thousands of GPUs. Our experimental results demonstrate 1.27×–7.57× throughput improvement under production-grade dynamic workloads, as compared to four state-of-the-art systems.

## 中文摘要

作为多样化 AI 应用的基础组件，多模态大语言模型（MLLM）的训练依赖于模态混合比例和样本长度分布动态变化的多模态数据集。然而，由于编码器与 LLM 主干之间资源分配和模型并行的决策被静态耦合，现有 MLLM 系统在动态工作负载下仍然效率低下。本文提出 MegaScale-Omni，一个面向动态工作负载适配与超大规模部署的工业级 MLLM 训练系统。MegaScale-Omni 建立在编码器-LLM 复用的训练方案之上，具有三项关键创新：（1）解耦的并行策略，为编码器采用长短序列并行以处理变长样本，为 LLM 主干采用完整的 5D 并行，二者均在通信高效的并行化布局下组织。（2）统一的编码器-LLM 表示，实现灵活、可扩展的共置，以及一种具备工作负载弹性的编码器-LLM 联合流水线新范式。（3）工作负载均衡技术，通过数据加载器中的去中心化分组重排序，以及从编码器到 LLM rank 的自适应重分片来实现。MegaScale-Omni 已部署为我们内部数千块 GPU 的大规模 MLLM 训练任务的基础。实验结果表明，与四个最先进的系统相比，在生产级动态工作负载下吞吐量提升 1.27×–7.57×。

**英文关键词：** Distributed systems, multimodal LLM training

**中文关键词：** 分布式系统、多模态 LLM 训练

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
