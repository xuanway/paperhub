---
title: "OPAL: On-demand Progressive Accelerated Scientific Lossy Compression"
description: "HPDC 2026 · Session 6 — Scientific Data Compression"
tags:
  - "HPDC2026"
  - "Session 6"
  - "Scientific Data Compression"
---

# OPAL: On-demand Progressive Accelerated Scientific Lossy Compression

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 6 — Scientific Data Compression（2026年7月15日 11:30–12:30 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 6</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807577)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ZhangLYUDWLHCZ26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ZhangLYUDWLHCZ26)

**作者**：Longtao Zhang, Ruoyu Li, Zhuoxun Yang, Robert Underwood, Sheng Di, Daoce Wang, Jinyang Liu, Jiajun Huang, Franck Cappello, Kai Zhao

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 6 — Scientific Data Compression（2026年7月15日 11:30–12:30 · Session Chair：Jay Lofstead）

---

## 英文摘要

Scientific applications generate massive amounts of data, necessitating effective data reduction techniques like error-bounded lossy compression. While state-of-the-art error-bounded lossy compressors effectively reduce storage footprint, they typically treat the compressed data as monolithic blobs, forcing analysts to decompress large volumes just to access specific data modalities. Conversely, existing storage solutions designed for flexible access lack the efficiency of modern compression. To bridge this gap between efficient compression and flexible data retrieval, we propose OPAL, a unified system that harmonizes high-performance compression with flexible, on-demand data access. Our first contribution is the OPAL universal framework, an adaptive architecture that endows generic lossy compressors with on-demand retrieval capabilities, enabling flexible and progressive access across multiple spatial regions, resolutions, and precisions. Our second contribution is OPALI, a customized compression algorithm designed natively with flexible data access in mind. By leveraging novel mechanisms such as shadow anchors, hybrid storage, and grouped bit-plane coding, OPALI eliminates the overhead inherent in generic wrappers. Extensive evaluations on real-world scientific datasets demonstrate that OPAL transforms standard compressors into flexible retrieval engines, while OPALI achieves superior compression ratios and retrieval performance, significantly accelerating scientific discovery.

## 中文摘要

科学应用产生海量数据，因此需要诸如误差有界有损压缩之类的有效数据缩减技术。虽然最先进的误差有界有损压缩器能有效降低存储占用，但它们通常将压缩数据视为不可分割的整体，迫使分析人员为了访问特定数据模态而解压大量数据。相反，为灵活访问而设计的现有存储方案又缺乏现代压缩的效率。为弥合高效压缩与灵活数据检索之间的鸿沟，我们提出 OPAL，一个将高性能压缩与灵活按需数据访问统一的系统。我们的第一项贡献是 OPAL 通用框架——一种自适应架构，为通用有损压缩器赋予按需检索能力，支持跨多个空间区域、分辨率和精度的灵活、渐进式访问。第二项贡献是 OPALI——一种在设计之初就考虑灵活数据访问的定制压缩算法。通过利用影子锚点、混合存储和分组位平面编码等新机制，OPALI 消除了通用封装固有的开销。在真实科学数据集上的大量评估表明，OPAL 将标准压缩器转变为灵活的检索引擎，而 OPALI 取得更优的压缩比与检索性能，显著加速科学发现。

## 英文关键词

error-bounded lossy compression, scientific data management

## 中文关键词

误差有界有损压缩，科学数据管理

---

[← 返回 Session 6 — Scientific Data Compression](index.md)
