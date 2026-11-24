---
title: "Make Updates Faster: A Fast Multi-Stripe Updates Framework in Erasure-Coded Storage Clusters"
description: "SC 2025 · System Software and Cloud · Hai Zhou; Dan Feng"
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# Make Updates Faster: A Fast Multi-Stripe Updates Framework in Erasure-Coded Storage Clusters

**中文标题：** 加速更新：纠删码存储集群中的快速多条带更新框架

**所属 Session：** [System Software and Cloud](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Hai Zhou; Dan Feng

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap307&sess=sess287)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Erasure coding is widely adopted to maintain data reliability, yet it introduces a significant update penalty. We analyze real-world traces and observe several challenges that are not addressed by existing studies, which thereby restrict the performance gains. We propose FastUpdate, an efficient multi-stripe updates framework that assists existing update schemes for fast updates. FastUpdate comprises three key designs: (1) it perceives the update locality and carefully merges multiple update requests accessing the same stripe to reduce the incurred network traffic; (2) it abstracts the existing update schemes into collector selection and tree construction, greedily generates the update solution for each stripe to balance the transmission load across nodes; (3) it dynamically schedules appropriate stripes to update in heterogeneous and dynamic networks to fully saturate the bandwidth resources. Comprehensive evaluations verify the effectiveness of FastUpdate on Alibaba ECS. It can incre

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
