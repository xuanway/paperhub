---
title: "AGILE: Lightweight and Efficient Asynchronous GPU-SSD Integration"
description: "SC 2025 · Programming Frameworks · Zhuoping Yang; Jinming Zhuang; Xingzhen Chen; Alex Jones; Peipei Zhou"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# AGILE: Lightweight and Efficient Asynchronous GPU-SSD Integration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Zhuoping Yang; Jinming Zhuang; Xingzhen Chen; Alex Jones; Peipei Zhou

**会议**：SC 2025 · St. Louis, MO

## 摘要

Graphics processing units have become essential for computationally intensive applications. However, emerging workloads often involve processing data exceeding GPU on-chip memory capacity. To mitigate this issue, existing solutions enable GPUs to use CPU DRAM or SSDs as external memory. Among them, the GPU-centric approach lets GPU threads directly access SSDs, eliminating CPU intervention overhead over traditional methods. However, the existing work adopts a synchronous model, and threads must tolerate the long communication latency before starting any tasks. In this work, we propose AGILE, a lightweight and efficient asynchronous library allowing GPU threads to access SSDs asynchronously. We demonstrate that AGILE achieves up to 1.88x improvement in workloads with different CTCs. Additionally, AGILE achieves 1.75x performance improvement on DLRMs against the SOTA work BaM. AGILE also exhibits low API overhead on graph applications. Lastly, AGILE consumes fewer registers and requires 

---

## 一句话总结

> 该工作属于 Programming Frameworks 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Programming Frameworks 领域贡献新的设计范式或评估框架。
