---
title: "AxCore: A Quantization-Aware Approximate GEMM Unit for LLM Inference"
description: "MICRO 2025 · Systems for AI (Quantization)"
tags:
  - "MICRO2025"
  - "Systems for AI (Quantization)"
---

# AxCore: A Quantization-Aware Approximate GEMM Unit for LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 MICRO 2025，所属 Track: Systems for AI (Quantization)。</p>
<p class="paper-seo-summary__tags">MICRO 2025 · Systems for AI (Quantization)</p>
</div>

**论文链接**：
**作者**：Jiaxiang Zou, Yonghao Chen, Xingyu Chen, Chenxi Xu, Xinyu Chen (The Hong Kong Univ. of Science and Technology (Guangzhou))
**会议**：MICRO 2025

---

## 一句话总结

> 该工作面向 Systems for AI (Quantization) 场景，围绕 A Quantization-Aware Approximate GEMM Unit for LLM Inference 提出系统化优化方案，重点涉及 AxCore、Quantization-Aware、Approximate 等关键技术点。

## 方法简述

- 以 AxCore 为核心切入点，构建针对 Systems for AI (Quantization) 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 结合大模型推理/训练链路进行系统级优化。

## 主要结果

- 突出吞吐、时延与成本的综合改进。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
