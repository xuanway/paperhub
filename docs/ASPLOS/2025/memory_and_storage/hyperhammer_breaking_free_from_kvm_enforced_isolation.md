---
title: "HyperHammer: Breaking Free from KVM-Enforced Isolation"
description: "ASPLOS 2025 · Memory & Storage"
tags:
  - "ASPLOS2025"
  - "Memory & Storage"
---

# HyperHammer: Breaking Free from KVM-Enforced Isolation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Memory & Storage。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Memory & Storage</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716002](https://doi.org/10.1145/3676641.3716002)
**作者**：Wei Chen (Peking University), Zhi Zhang (University of Western Australia), Xin Zhang (Peking University), Qingni Shen (Peking University), Yuval Yarom (Ruhr University Bochum), Daniel Genkin (Georgia Institute of Technology), Chen Yan (Peking University), Zhe Wang (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,Zhongguancun Laboratory)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Memory & Storage 场景，围绕 Breaking Free from KVM-Enforced Isolation 提出系统化优化方案，重点涉及 HyperHammer、Breaking、Free 等关键技术点。

## 方法简述

- 以 HyperHammer 为核心切入点，构建针对 Memory & Storage 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过模块化设计保持方案可迁移性与工程可落地性。

## 主要结果

- 在性能、能效或可扩展性指标上预期优于基线方案。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
