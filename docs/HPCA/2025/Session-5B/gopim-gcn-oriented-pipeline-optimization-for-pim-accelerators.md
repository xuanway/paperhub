---
title: "GOPIM: GCN-Oriented Pipeline Optimization for PIM Accelerators"
description: "HPCA 2025 · Doubling Down with PIM"
tags:
  - "HPCA2025"
  - "Doubling Down with PIM"
---

# GOPIM: GCN-Oriented Pipeline Optimization for PIM Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Doubling Down with PIM。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Doubling Down with PIM</p>
</div>

**论文链接**：
**作者**：Siling Yang (Zhejiang University), Shuibing He (Zhejiang University), Wenjiong Wang (Zhejiang University), Yanlong Yin (Zhejiang University), Tong Wu (Zhejiang University), Weijian Chen (Zhejiang University), Xuechen Zhang (Washington State University Vancouver), Xian-He Sun (Illinois Institute of Technology), Dan Feng (Huazhong University of Science and Technology)
**会议**：HPCA 2025

---

## 中文标题

GOPIM：面向 GCN 的 PIM 加速器流水线优化

## 英文摘要

Graph convolutional networks (GCNs) are popular for a variety of graph learning tasks. ReRAM-based processing-in-memory (PIM) accelerators are promising to expedite GCN training owing to their in-situ computing capability. However, existing accelerators can be severely underutilized even with pipelines, due to the oversight of the skewed execution times of various GCN stages and the ignorance of skewed degrees of graph vertices. In this work, we propose GOPIM, a GCN-oriented pipeline optimization for PIM accelerators to expedite GCN training. First, GOPIM proposes an ML-based scheme that allocates crossbar resources to the most needed stages to streamline the overall pipeline. Second, GOPIM utilizes a selective vertex updating technique that evenly distributes vertices on crossbars by interleaved mapping. These techniques collectively reduce the overall execution time without losing much accuracy. We also provide a practical architecture design for GOPIM. Our experimental results show that, GOPIM achieves up to 191× speedup and 16.1× energy saving, compared to the state-of-the-art work.

## 中文摘要

图卷积网络（GCN）在各类图学习任务中广受欢迎。基于 ReRAM 的存内处理（PIM）加速器凭借其原位计算能力，有望加速 GCN 训练。然而，现有加速器即便采用流水线也可能被严重闲置，其原因是忽略了各 GCN 阶段执行时间的偏斜，也忽视了图顶点度数的偏斜。在本工作中，我们提出 GOPIM，一种面向 GCN 的 PIM 加速器流水线优化方法，用以加速 GCN 训练。首先，GOPIM 提出基于机器学习的方案，将交叉阵列资源分配给最需要的阶段，以理顺整体流水线。其次，GOPIM 采用选择性顶点更新技术，通过交错映射将顶点均匀分布到各交叉阵列上。这些技术共同减少了整体执行时间，且不损失太多精度。我们还给出了 GOPIM 的实用架构设计。实验结果表明，与最先进的工作相比，GOPIM 取得最高 191× 的加速比与 16.1× 的节能。
