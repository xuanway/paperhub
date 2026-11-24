---
title: "Breaking the System Noise Barrier at Exascale"
description: "SC 2025 · State of the Practice · Edgar A. Leon; Joseph Glenski; Mark Stock; Kim McMahon; William Loewe; Clark Sny"
tags:
  - "SC2025"
  - "State of the Practice"
---

# Breaking the System Noise Barrier at Exascale

**中文标题：** 在百亿亿次规模突破系统噪声屏障

**所属 Session：** [State of the Practice](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：State of the Practice。</p>
<p class="paper-seo-summary__tags">SC 2025 · State of the Practice</p>
</div>

**作者**：Edgar A. Leon; Joseph Glenski; Mark Stock; Kim McMahon; William Loewe; Clark Snyder; Larry Kaplan; Srinath Vadlamani; Timothy I. Mattox; Trent D'Hooge; Brian Behlendorf; Nathan Hanford; Ramesh Pankajakshan; Matthew L. Leininger

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap257&sess=sess301)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

To meet the increasing demands of parallel scientific applications, supercomputers continue to grow in both scale and complexity. The fastest supercomputer in the world, El Capitan, features over a million CPU cores and tens of thousands of GPUs. Applications running on such large-scale systems are particularly susceptible to system noise or interference caused by the operating system (OS) and other services running on the same compute nodes as the application. In this paper, we address this critical performance and scalability challenge on El Capitan, enabling scientific applications to better leverage the benefits of the world's fastest supercomputer. Our strategy comprises two key components: (1) isolating system services from applications and (2) applying OS-level tuning to maintain minimal application interference. As part of this effort, we provide a distribution-independent tuning guide applicable to any Linux system, and we propose and evaluate general strategies for isolating

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
