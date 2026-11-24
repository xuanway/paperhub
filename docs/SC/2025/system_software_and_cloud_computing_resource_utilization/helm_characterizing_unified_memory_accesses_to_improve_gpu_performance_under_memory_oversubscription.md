---
title: "HELM: Characterizing Unified Memory Accesses to Improve GPU Performance Under Memory Oversubscription"
description: "SC 2025 · System Software and Cloud Computing: Resource Utilization · Nathan Jones; Tyler Allen; Rong Ge"
tags:
  - "SC2025"
  - "System Software and Cloud Computing: Resource Utilization"
---

# HELM: Characterizing Unified Memory Accesses to Improve GPU Performance Under Memory Oversubscription

**中文标题：** 刻画统一内存访问以提高内存超额使用情况下的 GPU 性能

**所属 Session：** [System Software and Cloud Computing: Resource Utilization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud Computing: Resource Utilization。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud Computing: Resource Utilization</p>
</div>

**作者**：Nathan Jones; Tyler Allen; Rong Ge

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap340&sess=sess370)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Unified memory (UM) technologies simplify memory management across CPU and GPU domains in GPU-accelerated heterogeneous architectures through transparent data migration. However, the default migration mechanism can severely degrade performance when applications oversubscribe GPU memory. Existing approaches to mitigating this performance degradation often fail to generalize, as they target specific application types, require specialized hardware, or integrate opaque classification methods. We introduce HEterogeneous Locality Metrics (HELM), a novel set of semantically meaningful metrics designed to characterize UM access patterns across diverse applications. These metrics are quantified using readily accessible UM driver telemetry data, providing users with tractable and interpretable UM memory characterizations. Such insight is critical for selecting optimal UM migration and placement policies under oversubscription. We demonstrate HELM’s accuracy and interpretability through access pa

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
