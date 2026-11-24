---
title: "Optimizing Data Acquisitions in Multi-Robot Systems"
description: "SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search · Yanhao Li; Zijun Xu; Xuanjun Wen; Yanjie Song; Guancheng Li; Shu Yin"
tags:
  - "SC2025"
  - "Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search"
---

# Optimizing Data Acquisitions in Multi-Robot Systems

**中文标题：** 优化多机器人系统中的数据采集

**所属 Session：** [Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search</p>
</div>

**作者**：Yanhao Li; Zijun Xu; Xuanjun Wen; Yanjie Song; Guancheng Li; Shu Yin

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap170&sess=sess163)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

We present ROSfs, a novel user-level file system designed to address critical data query inefficiencies in multi-robot systems (MRS). ROSfs introduces an innovative file organization model where robot data is structured as labeled sub-files, coupled with a time-indexed architecture that enables efficient querying of actively modified data. This design enables real-time cross-robot data acquisition and collaboration capabilities previously unattainable in MRS deployments. Our implementation integrates seamlessly with the Robot Operating System (ROS) and has been extensively evaluated using both physical UAV/UGV platforms and data servers. Experimental results demonstrate that ROSfs achieves a 7x reduction in online data query latency under wireless network conditions compared to conventional ROS storage methods, while simultaneously improving data freshness (Age of Information) by up to 271x. These advancements position ROSfs as a transformative solution for high-performance robotic dat

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
