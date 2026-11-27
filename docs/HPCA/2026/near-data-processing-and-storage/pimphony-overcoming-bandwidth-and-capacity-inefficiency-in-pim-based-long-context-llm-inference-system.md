---
title: "PIMphony: Overcoming Bandwidth and Capacity Inefficiency in PIM-based Long-Context LLM Inference System"
description: "HPCA 2026 · Near-Data Processing and Storage"
tags:
  - "HPCA2026"
  - "Near-Data Processing and Storage"
---

# PIMphony: Overcoming Bandwidth and Capacity Inefficiency in PIM-based Long-Context LLM Inference System

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Near-Data Processing and Storage。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Near-Data Processing and Storage</p>
</div>

**论文链接**：
**作者**：hyucksung kwon Hanyang University , Kyungmo Koo Hanyang University , Janghyeon Kim Hanyang University , Woongkyu Lee Hanyang University , Minjae Lee Hanyang University , Gyeonggeun Jung KAIST , Hyungdeok Lee Solution Advanced Technology, SK hynix , Yousub Jung Solution Advanced Technology, SK hynix , Jaehan Park Solution Advanced Technology, SK hynix , Yosub Song Solution Advanced Technology, SK hynix , Byeongsu Yang Solution Advanced Technology, SK hynix , Haerang Choi Solution Advanced Technology, SK hynix , Guhyun Kim Solution Advanced Technology, SK hynix , Jongsoon Won Solution Advanced Technology, SK hynix , Woojae Shin Solution Advanced Technology, SK hynix , Changhyun Kim Solution Advanced Technology, SK hynix , Shin Gyeongcheol Solution Advanced Technology, SK hynix , Yongkee Kwon Tenstorrent , Ilkon Kim Solution Advanced Technology, SK hynix , Euicheol Lim SK hynix , John Kim KAIST , Jungwook Choi Hanyang University
**会议**：HPCA 2026

---

## 中文标题

PIMphony：克服基于 PIM 的长上下文 LLM 推理系统的带宽与容量低效

## 英文摘要

The expansion of long-context Large Language Models (LLMs) creates significant memory system challenges. While Processing-in-Memory (PIM) is a promising accelerator, we identify that it suffers from critical inefficiencies when scaled to long contexts: severe channel underutilization, performance-limiting I/O bottlenecks, and massive memory waste from static KV cache management. In this work, we propose PIMphony, a PIM orchestrator that systematically resolves these issues with three co-designed techniques. First, Token-Centric PIM Partitioning (TCP) ensures high channel utilization regardless of batch size. Second, Dynamic PIM Command Scheduling (DCS) mitigates the I/O bottleneck by overlapping data movement and computation. Finally, a Dynamic PIM Access (DPA) controller enables dynamic memory management to eliminate static memory waste. Implemented via an MLIR-based compiler and evaluated on a cycle-accurate simulator, PIMphony significantly improves throughput for long-context LLM inference (up to 72B parameters and 1M context length). Our evaluations show performance boosts of up to 11.3× on PIM-only systems and 8.4× on xPU+PIM systems, enabling more efficient deployment of LLMs in real-world long-context applications.

## 中文摘要

长上下文大语言模型（LLM）的扩展给内存系统带来严峻挑战。存内处理（PIM）是一种有前景的加速器，但我们发现，当它扩展到长上下文时会遭受严重的低效：通道利用率不足、限制性能的 I/O 瓶颈，以及静态 KV 缓存管理造成的大量内存浪费。为此我们提出 PIMphony，一个 PIM 编排器，通过三项协同设计的技术系统性地解决这些问题。第一，以 token 为中心的 PIM 划分（TCP）保证任意批量大小下都有较高的通道利用率。第二，动态 PIM 命令调度（DCS）通过重叠数据搬运与计算来缓解 I/O 瓶颈。最后，动态 PIM 访问（DPA）控制器实现动态内存管理，消除静态内存浪费。PIMphony 通过基于 MLIR 的编译器实现，并在周期级精确模拟器上评估，显著提升了长上下文 LLM 推理的吞吐（最高 720 亿参数、100 万上下文长度）。评估显示，在纯 PIM 系统上最高提升 11.3 倍，在 xPU+PIM 系统上最高提升 8.4 倍，使 LLM 能在真实长上下文应用中更高效地部署。
