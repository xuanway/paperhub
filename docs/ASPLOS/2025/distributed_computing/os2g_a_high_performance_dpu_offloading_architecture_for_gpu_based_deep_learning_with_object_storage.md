---
title: "OS2G: A High-Performance DPU Offloading Architecture for GPU-based Deep Learning with Object Storage"
description: "ASPLOS 2025 · Distributed Computing"
tags:
  - "ASPLOS2025"
  - "Distributed Computing"
---

# OS2G: A High-Performance DPU Offloading Architecture for GPU-based Deep Learning with Object Storage

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Distributed Computing。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Distributed Computing</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716265](https://doi.org/10.1145/3676641.3716265)
**作者**：Zhen Jin (Zhejiang University,Alibaba Group), Yiquan Chen (Alibaba Group), Mingxu Liang (Alibaba Group), Yijing Wang (Alibaba Group), Guoju Fang (Alibaba Group), Ao Zhou (Alibaba Group), Keyao Zhang (Zhejiang University), Jiexiong Xu (Zhejiang University), Wenhai Lin (Zhejiang University), Yiquan Lin (Zhejiang University), Shushu Zhao (Alibaba Group), Wenkai Shi (Alibaba Group), Zhenhua He (Alibaba Group), Shishun Cai (Alibaba Group), Wenzhi Chen (Zhejiang University)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Distributed Computing 场景，围绕 OS2G、High-Performance 相关关键问题 提出系统化优化方案，重点涉及 OS2G、High-Performance、DPU 等关键技术点。

## 方法简述

- 以 OS2G 为核心切入点，构建针对 Distributed Computing 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 在 GPU 执行与调度路径上引入针对性优化。

## 主要结果

- 提升并行执行效率与资源利用率。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
