---
title: "Daredevil: Rescue Your Flash Storage from Inflexible Kernel Storage Stack"
description: "EuroSys 2025 · Storage · Junzhe Li (The University of Hong Kong), Ran Shu (Microsoft Research), Jiayi Lin"
tags:
  - "EuroSys2025"
  - "Storage"
---

# Daredevil: Rescue Your Flash Storage from Inflexible Kernel Storage Stack

**中文标题：** 从僵化的内核存储栈中解救闪存存储

**所属 Session：** [Session 7.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Junzhe Li (The University of Hong Kong), Ran Shu (Microsoft Research), Jiayi Lin (The University of Hong Kong), Qingyu Zhang (The University of Hong Kong), Ziyue Yang (Microsoft Research), Jie Zhang (Peking University), Yongqiang Xiong (Microsoft Research), Chenxiong Qian (The University of Hong Kong)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717482)

## 英文摘要

Existing kernel storage stacks for NVMe SSDs struggle to address performance interference between I/O requests from tenants with different SLAs, leading to the multi-tenancy issue. Addressing this requires separating their I/O requests within the NVMe I/O queues (NQs). However, our analysis reveals that the static CPU core-NQ bindings of current storage stacks restrict their flexibility to achieve this goal.

We propose daredevil, a novel kernel storage stack, which addresses this issue by decoupling the static bindings and allowing full connectivity between cores and NQs. Therefore, it grants multi-tenancy control the flexibility to freely route requests among NQs according to their SLAs. Moreover, it incorporates multi-tenancy-aware scheduling on NQs to facilitate efficient request routing. Our evaluation shows that daredevil can reduce I/O request latency by up to 3-170× compared to current kernel storage stacks, while maintaining comparable throughput.

## 中文摘要

现有面向 NVMe SSD 的内核存储栈难以处理来自具有不同 SLA 的租户的 I/O 请求之间的性能干扰，从而导致多租户问题。解决这一问题需要在 NVMe I/O 队列（NQ）内分离它们的 I/O 请求。然而，我们的分析揭示，当前存储栈静态的 CPU 核与 NQ 绑定限制了实现该目标的灵活性。

我们提出 daredevil，一种新颖的内核存储栈，它通过解耦静态绑定并允许核与 NQ 之间完全连通来解决这一问题。因此，它赋予多租户控制按其 SLA 在 NQ 之间自由路由请求的灵活性。此外，它在 NQ 上引入了多租户感知的调度，以促进高效的请求路由。我们的评估表明，与当前的内核存储栈相比，daredevil 可将 I/O 请求延迟降低最高 3 至 170 倍，同时保持相当的吞吐量。

**英文关键词：** Storage systems, Solid-state drives, Linux kernel

**中文关键词：** 存储系统、固态硬盘、Linux 内核

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
