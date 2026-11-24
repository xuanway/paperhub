---
title: "lsCOMP: Efficient Light Source Compression"
description: "SC 2025 · Compression and Data Reduction 1 · Yafan Huang; Sheng Di; Robert Underwood; Peco Myint; Miaoqi Chu; Guanpeng Li; Ni"
tags:
  - "SC2025"
  - "Compression and Data Reduction 1"
---

# lsCOMP: Efficient Light Source Compression

**中文标题：** 高效光源数据压缩

**所属 Session：** [Compression and Data Reduction 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 1</p>
</div>

**作者**：Yafan Huang; Sheng Di; Robert Underwood; Peco Myint; Miaoqi Chu; Guanpeng Li; Nicholas Schwarz; Franck Cappello

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap374&sess=sess162)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Light source facilities, which generate X-rays for probing microstructures and dynamic processes, produce intense data streams, reaching up to 250 GB/s and projected to exceed 1 TB/s by the end of this decade. Managing such massive data poses critical challenges due to limited local processing capacity and bandwidth constraints when offloading data to HPC systems. To address these challenges, we propose lsCOMP, a GPU compressor that operates within a single kernel. lsCOMP supports both lossless and configurable lossy compression, ensuring high compression ratios and preserved data quality across diverse light source applications. On one NVIDIA A100 GPU, lsCOMP achieves compression throughputs of 380.89 to 509.21 GB/s in lossless mode, delivering up to 20 times higher performance than industry-leading GPU compressors while achieving superior compression ratios. In lossy modes, lsCOMP further improves throughput and ratios significantly. Additionally, lsCOMP demonstrates versatile perfor

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
