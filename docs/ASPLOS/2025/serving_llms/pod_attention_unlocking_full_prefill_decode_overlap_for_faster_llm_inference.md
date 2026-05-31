---
title: "POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference"
description: "ASPLOS 2025 · Serving LLMs"
tags:
  - "ASPLOS2025"
  - "Serving LLMs"
---

# POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Serving LLMs。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Serving LLMs</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3715996](https://doi.org/10.1145/3676641.3715996)
**作者**：Aditya K Kamath (Paul G Allen School of Computer Science and Engineering, University of Washington), Ramya Prabhu (Microsoft Research India), Jayashree Mohan (Microsoft Research India), Simon Peter (Paul G Allen School of Computer Science and Engineering, University of Washington), Ramachandran Ramjee (Microsoft Research India), Ashish Panwar (Microsoft Research India)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Serving LLMs 场景，围绕 Unlocking Full Prefill-Decode Overlap for Faster LLM Inference 提出系统化优化方案，重点涉及 POD-Attention、Unlocking、Full 等关键技术点。

## 方法简述

- 以 POD-Attention 为核心切入点，构建针对 Serving LLMs 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 结合大模型推理/训练链路进行系统级优化。

## 主要结果

- 突出吞吐、时延与成本的综合改进。
- 目标是降低时延并提升吞吐/可扩展性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
