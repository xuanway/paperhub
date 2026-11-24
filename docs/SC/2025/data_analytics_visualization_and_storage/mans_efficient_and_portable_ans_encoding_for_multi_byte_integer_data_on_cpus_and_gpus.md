---
title: "MANS: Efficient and Portable ANS Encoding for Multi-Byte Integer Data on CPUs and GPUs"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Wenjing Huang; Jinwu Yang; Shengquan Yin; Haoxu Li; Yida Gu; Zedong Liu; Xing Ji"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# MANS: Efficient and Portable ANS Encoding for Multi-Byte Integer Data on CPUs and GPUs

**中文标题：** 面向 CPU 和 GPU 上多字节整数数据的高效可移植 ANS 编码

**所属 Session：** [Data Analytics, Visualization, and Storage](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Wenjing Huang; Jinwu Yang; Shengquan Yin; Haoxu Li; Yida Gu; Zedong Liu; Xing Jing; Zheng Wei; Shiyuan Fu; Hao Hu; Guangming Tan; Dingwen Tao

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap449&sess=sess283)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Lossless compression is a classic technique for reducing data storage and transmission requirements. Asymmetric numeral systems (ANS) is a high-throughput, high-ratio lossless compression algorithm, but it lacks effective support for multi-byte data and cross-platform compatibility. To address this issue, we propose an adaptive data mapping (ADM) scheme, which maps multi-byte integer data into single-byte space based on the data's characteristics, improving the compression ratio of ANS while maintaining low encoding redundancy. We also optimize the ADM algorithm and the ANS encoder for GPU and CPU architectures, respectively, and combine them to create an efficient and portable ANS encoding method for multi-byte integer data, called MANS. Experimental results show that MANS improves compression ratios by an average of 1.24$\times$, achieves 870.27MB/s throughput on CPUs, and delivers up to 288.45$\times$ and 135.86$\times$ speedups on an NVIDIA A100 and an AMD MI210 GPU compared to the

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
