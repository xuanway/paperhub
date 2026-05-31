---
title: "vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention"
description: "ASPLOS 2025 · Memory Management"
tags:
  - "ASPLOS2025"
  - "Memory Management"
---

# vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Memory Management。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Memory Management</p>
</div>

**论文链接**：[https://doi.org/10.1145/3669940.3707256](https://doi.org/10.1145/3669940.3707256)
**作者**：Ramya Prabhu (Microsoft Research), Ajay Nayak (Indian Institute of Science), Jayashree Mohan (Microsoft Research), Ramachandran Ramjee (Microsoft Research), Ashish Panwar (Microsoft Research)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Memory Management 场景，围绕 Dynamic Memory Management for Serving LLMs without PagedAttention 提出系统化优化方案，重点涉及 vAttention、Dynamic、Memory 等关键技术点。

## 方法简述

- 以 vAttention 为核心切入点，构建针对 Memory Management 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 结合大模型推理/训练链路进行系统级优化。

## 主要结果

- 突出吞吐、时延与成本的综合改进。
- 降低内存瓶颈并提升系统效率。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
