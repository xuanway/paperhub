---
title: "AGILE: Lightweight and Efficient Asynchronous GPU-SSD Integration"
description: "SC 2025 · Programming Frameworks · Zhuoping Yang; Jinming Zhuang; Xingzhen Chen; Alex Jones; Peipei Zhou"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# AGILE: Lightweight and Efficient Asynchronous GPU-SSD Integration

**中文标题：** 轻量高效的异步 GPU-SSD 集成

**所属 Session：** [Programming Frameworks](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Zhuoping Yang; Jinming Zhuang; Xingzhen Chen; Alex Jones; Peipei Zhou

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap168&sess=sess294)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Graphics processing units have become essential for computationally intensive applications. However, emerging workloads often involve processing data exceeding GPU on-chip memory capacity. To mitigate this issue, existing solutions enable GPUs to use CPU DRAM or SSDs as external memory. Among them, the GPU-centric approach lets GPU threads directly access SSDs, eliminating CPU intervention overhead over traditional methods. However, the existing work adopts a synchronous model, and threads must tolerate the long communication latency before starting any tasks. In this work, we propose AGILE, a lightweight and efficient asynchronous library allowing GPU threads to access SSDs asynchronously. We demonstrate that AGILE achieves up to 1.88x improvement in workloads with different CTCs. Additionally, AGILE achieves 1.75x performance improvement on DLRMs against the SOTA work BaM. AGILE also exhibits low API overhead on graph applications. Lastly, AGILE consumes fewer registers and requires

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
