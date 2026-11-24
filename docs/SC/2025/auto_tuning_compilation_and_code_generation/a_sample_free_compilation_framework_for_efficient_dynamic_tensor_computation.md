---
title: "A Sample-Free Compilation Framework for Efficient Dynamic Tensor Computation"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Yangjie Zhou; Honglin Zhu; Qian Qiu; Weihao Cui; Zihan Liu; Peng Chen; Mohamed W"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# A Sample-Free Compilation Framework for Efficient Dynamic Tensor Computation

**中文标题：** 面向高效动态张量计算的无采样编译框架

**所属 Session：** [Auto-Tuning, Compilation, and Code Generation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Yangjie Zhou; Honglin Zhu; Qian Qiu; Weihao Cui; Zihan Liu; Peng Chen; Mohamed Wahib; Cong Guo; Siyuan Feng; Jintao Meng; Haidong Lan; Jingwen Leng; Yun Lin; Jin Song Dong; Wenxi Zhu; Minwen Deng

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap169&sess=sess290)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Dynamic-shape tensor computation poses challenges for shape-specific compilation due to variable input dimensions. Existing compilers rely on shape samples, incurring high tuning costs and degraded performance on unseen inputs. We present Helix, a dynamic tensor framework with sample-free and architecture-guided compilation for compilation efficiency and shape-general performance. To avoid shape sampling, Helix constructs shape-agnostic compilation by decomposing computations across architectural layers. A bidirectional strategy combines top-down abstraction, aligning tensor computations with architectural hierarchies, and bottom-up kernel construction, building efficient execution strategies from reusable, architecture-aligned micro-kernels. A hybrid analyzer ensures accuracy through profiling at lower architectural levels, and achieves scalability through architecture-informed modeling at higher levels and runtime. This hierarchical design eliminates shape-specific tuning and enables

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
