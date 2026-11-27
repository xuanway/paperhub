---
title: "Towards Compute-Aware In-Switch Computing for LLMs Tensor-Parallelism on Multi-GPU Systems"
description: "HPCA 2026 · Distributed and Multi-GPU Training"
tags:
  - "HPCA2026"
  - "Distributed and Multi-GPU Training"
---

# Towards Compute-Aware In-Switch Computing for LLMs Tensor-Parallelism on Multi-GPU Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Distributed and Multi-GPU Training。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Distributed and Multi-GPU Training</p>
</div>

**论文链接**：
**作者**：Chen Zhang Shanghai Jiao Tong University , Qijun Zhang Shanghai Jiao Tong University , Zhuoshan Zhou Shanghai Jiao Tong University , Yijia Diao Shanghai Jiao Tong University , Haibo Wang Huawei , Zhe Zhou Huawei , Zhipeng Tu Huawei , Zhiyao Li Huawei , Guangyu Sun Peking University , Zhuoran Song Shanghai Jiao Tong University , Zhigang Ji Shanghai Jiao Tong University , Jingwen Leng Shanghai Jiao Tong University , Minyi Guo Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

面向多 GPU 系统上 LLM 张量并行的计算感知交换机内计算

## 英文摘要

Tensor parallelism (TP) in large-scale LLM inference and training introduces frequent collective operations that dominate inter-GPU communication. While in-switch computing, exemplified by NVLink SHARP (NVLS), accelerates collective operations by reducing redundant data transfer, its communication-centric design philosophy introduces the mismatch between its communication mode and the memory semantic requirement of LLM’s computation kernel. Such a mismatch isolates the compute and communication phases, resulting in underutilized resources and limited overlap in multi-GPU systems. To address the limitation, we propose CAIS, the first Compute-Aware In-Switch computing framework that aligns communication modes with computation’s memory semantics requirement. CAIS consists of three integral techniques: (1) compute-aware ISA and microarchitecture extension to enable compute-aware in-switch computing. (2) merging-aware TB (Thread Block) coordination to improve the temporal alignment for efficient request merging. (3) graph-level dataflow optimizer to achieve a tight cross-kernel overlap. Evaluations on LLM workloads show that CAIS achieves 1.38× average end-to-end training speedup over the SOTA NVLS-enabled solution, and 1.61× over T3, the SOTA compute-communicate overlap solutions but do not leverage NVLS, demonstrating its effectiveness in accelerating TP on multi-GPU systems.

## 中文摘要

大规模 LLM 推理与训练中的张量并行（TP）引入频繁的集合操作，主导了 GPU 间通信。以 NVLink SHARP（NVLS）为代表的交换机内计算通过减少冗余数据传输来加速集合操作，但其以通信为中心的设计理念使通信模式与 LLM 计算内核的内存语义需求不匹配。这种不匹配将计算与通信阶段割裂，导致资源利用不足，多 GPU 系统中的重叠也十分有限。为解决该局限，我们提出 CAIS，首个计算感知的交换机内计算框架，使通信模式与计算的内存语义需求相一致。CAIS 包含三项关键技术：(1) 计算感知的 ISA 与微架构扩展以支持计算感知的交换机内计算；(2) 感知合并的线程块（TB）协调以改善时间对齐、实现高效的请求合并；(3) 图级数据流优化器以实现紧凑的跨内核重叠。在 LLM 负载上的评估表明，CAIS 相比启用 NVLS 的最先进方案取得平均 1.38 倍的端到端训练加速，相比不利用 NVLS 的最先进计算与通信重叠方案 T3 取得 1.61 倍加速，展示了其在多 GPU 系统上加速 TP 的有效性。
