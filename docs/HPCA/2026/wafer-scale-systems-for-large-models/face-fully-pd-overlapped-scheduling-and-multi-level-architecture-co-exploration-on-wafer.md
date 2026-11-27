---
title: "FACE: Fully PD Overlapped Scheduling and Multi-Level Architecture Co-Exploration on Wafer"
description: "HPCA 2026 · Wafer-Scale Systems for Large Models"
tags:
  - "HPCA2026"
  - "Wafer-Scale Systems for Large Models"
---

# FACE: Fully PD Overlapped Scheduling and Multi-Level Architecture Co-Exploration on Wafer

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Wafer-Scale Systems for Large Models。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Wafer-Scale Systems for Large Models</p>
</div>

**论文链接**：
**作者**：Zheng Xu Tsinghua University , Dehao Kong Tsinghua University , Jiaxin Liu Tsinghua University , Dingcheng Jiang Tsinghua University , Xu Dai Shanghai Artificial Intelligence Laboratory , Jinyi Deng Tsinghua University , Yang Hu Tsinghua University , Shouyi Yin Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

FACE：晶圆上完全重叠的 PD 调度与多级架构协同探索

## 英文摘要

The rapid expansion of large language models (LLMs) parameter scales imposes unprecedented demands on compute, memory, and communication resources for inference deployment. Wafer-scale chips, leveraging advanced packaging technologies, deliver high-density integration of compute and memory with high die-to-die (D2D) communication bandwidth, providing a compelling architectural approach to satisfy these resource requirements. However, its unprecedented chip area introduces significant architectural design complexities. Wafer-scale chips feature a multi-level architecture spanning the wafer, die, and core levels, involving numerous critical design parameters and trade-offs, which still lack systematic understanding and exploration. Moreover, this poses major challenges for LLM serving scheduling. Existing methods, largely adapted from GPU-based systems, fail to fully leverage the advantages of wafer-scale chips and mitigate their limitations, making it difficult to efficiently translate massive hardware resources into actual performance gains. To address these challenges, we introduce FACE, a co-exploration framework for jointly optimizing multi-level architecture and serving scheduling. We first establish a flexible and extensible wafer-scale hardware template to systematically explore the optimal architecture and micro-architecture parameters. Leveraging the fine-grained control and high interconnect bandwidth of wafer-scale chips, FACE implements an LLM scheduling strategy that achieves fully overlapped prefill-decode execution and efficient KV cache management, maximizing hardware resource utilization to improve LLM service quality. Our evaluation demonstrates that FACE can achieve an average overall performance improvement of 3.68× across various LLM models and datasets compared to the state-of-the-art (SOTA) LLM serving system on wafer-scale chips.

## 中文摘要

大语言模型（LLM）参数规模的快速扩张，对推理部署的计算、内存与通信资源提出前所未有的需求。晶圆级芯片借助先进封装技术，高密度集成计算与内存并提供高裸片间（D2D）通信带宽，为满足这些需求提供了有吸引力的架构途径。然而其前所未有的芯片面积带来显著的架构设计复杂性：晶圆级芯片具有跨越晶圆、裸片与核心层级的多级架构，涉及大量关键设计参数与折中，目前仍缺乏系统认识与探索。这也为 LLM 服务调度带来重大挑战；现有方法多改编自基于 GPU 的系统，无法充分利用晶圆级芯片的优势并缓解其局限，难以将海量硬件资源高效转化为性能收益。为此，我们提出 FACE，一个联合优化多级架构与服务调度的协同探索框架。我们首先建立灵活可扩展的晶圆级硬件模板，以系统探索最优架构与微架构参数；再借助晶圆级芯片的细粒度控制与高互连带宽，实现预填充—解码完全重叠执行与高效 KV 缓存管理的 LLM 调度策略，最大化硬件资源利用率以提升 LLM 服务质量。评估表明，在多种 LLM 模型与数据集上，相比晶圆级芯片上最先进的 LLM 服务系统，FACE 平均取得 3.68 倍的整体性能提升。
