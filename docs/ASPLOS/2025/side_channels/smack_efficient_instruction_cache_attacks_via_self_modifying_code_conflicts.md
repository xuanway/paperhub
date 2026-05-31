---
title: "SMaCk: Efficient Instruction Cache Attacks via Self-Modifying Code Conflicts"
description: "ASPLOS 2025 · Side Channels"
tags:
  - "ASPLOS2025"
  - "Side Channels"
---

# SMaCk: Efficient Instruction Cache Attacks via Self-Modifying Code Conflicts

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Side Channels。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Side Channels</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716274](https://doi.org/10.1145/3676641.3716274)
**作者**：Seonghun Son (Iowa State University), Daniel Moghimi (Google), Berk Gulmezoglu (Iowa State University)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Side Channels 场景，围绕 Efficient Instruction Cache Attacks via Self-Modifying Code Conflicts 提出系统化优化方案，重点涉及 SMaCk、Instruction、Cache 等关键技术点。

## 方法简述

- 以 SMaCk 为核心切入点，构建针对 Side Channels 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 针对缓存层次与数据复用策略进行改进。

## 主要结果

- 降低访存开销并改善性能稳定性。
- 目标是降低时延并提升吞吐/可扩展性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
