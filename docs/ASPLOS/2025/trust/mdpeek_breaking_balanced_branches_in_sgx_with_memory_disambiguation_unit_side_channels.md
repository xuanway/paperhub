---
title: "MDPeek: Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels"
description: "ASPLOS 2025 · Trust"
tags:
  - "ASPLOS2025"
  - "Trust"
---

# MDPeek: Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Trust。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Trust</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716004](https://doi.org/10.1145/3676641.3716004)
**作者**：Chang Liu (Tsinghua University), Shuaihu Feng (Zhongguancun Laboratory), Yuan Li (Zhongguancun Laboratory), Dongsheng Wang (Tsinghua University), Wenjian He (Huawei Technologies Co., Ltd.), Yongqiang Lyu (Tsinghua University), Trevor E. Carlson (National University of Singapore)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Trust 场景，围绕 Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels 提出系统化优化方案，重点涉及 MDPeek、Breaking、Balanced 等关键技术点。

## 方法简述

- 以 MDPeek 为核心切入点，构建针对 Trust 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 优化内存访问、分配或一致性路径。

## 主要结果

- 降低内存瓶颈并提升系统效率。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
