---
title: "Warped-Compaction: Maximizing GPU Register File Bandwidth Utilization via Operand Compaction"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# Warped-Compaction: Maximizing GPU Register File Bandwidth Utilization via Operand Compaction

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Eunbi Jeong (Ewha Womans University), Ipoom Jeong (Yonsei University), Myung Kuk Yoon (Ewha Womans University), Nam Sung Kim (UIUC)
**会议**：HPCA 2025

---

## 中文标题

Warped-Compaction：通过操作数压缩最大化 GPU 寄存器堆带宽利用率

## 英文摘要

The GPU has been successfully used for diverse emerging compute-intensive applications, including imaging, computer vision, and more recently, deep learning, to name a few. To offer high performance for such applications, it is provisioned with massive Register Files (RFs) to exploit high Thread-Level Parallelism (TLP). As RFs are designed to store thousands of contexts and provide very high bandwidth for uninterrupted supply of operands to hundreds of compute units for high TLP, they have become one of the most power-hungry components in the GPU. Meanwhile, faced with the end of Dennard scaling, it is more important than ever to innovate the microarchitecture of (powerconstrained) GPUs to continuously improve the performance of future compute-intensive applications. In this work, we propose a GPU microarchitecture, Warped-Compaction, designed to utilize given RFs more efficiently, instead of relying on larger-capacity and/or higher-bandwidth RFs to further improve GPU performance. Specifically, first, we reverse-engineer the latest GPU’s RF organization through microbenchmarking. This uncovers that each sub-core within a streaming multiprocessor contains only two dual-ported RF banks, and accesses to these banks are arbitrated solely based on register IDs. We also reveal that, despite the modest configurations, RF banks are largely underutilized, staying inactive for 33.5% of the time. Second, we observe that previously proposed RF optimization techniques, data forwarding and dead register elimination, cannot address this underutilization problem. This is mainly due to the (R1) insufficient RF access requests from a limited number of Operand Collector Units (OCUs) and (R2) inefficient operand distribution by the conventional RF bank arbitration. Third, we present two architectural solutions to tackle the observed inefficiency: (S1) OCU sharing and (S2) skewed arbitrator. Building on enhanced OCU early allocation for partially ready instructions and operand forwarding to OCUs, OCU sharing allows two different warp instructions to share a single OCU, and skewed arbitrator evenly distributes register accesses across RF banks, maximizing the utilization of given RF bandwidth. The synergistic integration of these techniques, forming Warped-Compaction, results in 26.1% higher performance and 21.7% better energy efficiency of RF and OCU compared to baseline high-end GPU.

## 中文摘要

GPU 已成功用于成像、计算机视觉以及近期的深度学习等新兴计算密集型应用。为提供高性能，GPU 配备大规模寄存器堆（RF）以挖掘高线程级并行性（TLP）；RF 需存储数千个上下文并提供极高带宽，因而成为 GPU 中功耗最高的部件之一。面对 Dennard 缩放终结，创新受功耗约束的 GPU 微架构愈发重要。本工作提出微架构 Warped-Compaction，旨在高效利用既有 RF，而非依赖更大容量或更高带宽的 RF。首先，微基准测试显示，流式多处理器中每个子核仅有两个双端口 RF 体（bank），访问仅依据寄存器 ID 仲裁；尽管配置有限，RF 体有 33.5% 时间处于空闲。其次，已有 RF 优化技术（数据转发与死寄存器消除）无法解决该利用不足，主要因为（R1）有限数量的操作数收集单元（OCU）提供的 RF 访问请求不足，以及（R2）传统 RF 体仲裁导致的操作数分配低效。第三，我们提出（S1）OCU 共享与（S2）倾斜仲裁器两种方案：基于针对部分就绪指令增强的 OCU 提前分配与操作数转发，OCU 共享允许两个不同的线程束（warp）指令共享单个 OCU；倾斜仲裁器则把寄存器访问均匀分布到各 RF 体，最大化给定 RF 带宽的利用率。二者协同形成 Warped-Compaction，相较基线高端 GPU 实现 26.1% 性能提升与 RF、OCU 21.7% 能效提升。
