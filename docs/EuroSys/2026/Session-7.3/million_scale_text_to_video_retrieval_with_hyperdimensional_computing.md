---
title: "Million-Scale Text-to-Video Retrieval with Hyperdimensional Computing"
description: "EuroSys 2026 · Storage Systems · Hyunsei Lee (DGIST), Jaewoo Gwak (DGIST), Shinhyoung Jang (DGIST), Junyoung Lee "
tags:
  - "EuroSys2026"
  - "Storage Systems"
---

# Million-Scale Text-to-Video Retrieval with Hyperdimensional Computing

**中文标题：** 基于超维计算的百万级文本到视频检索

**所属 Session：** [Session 7.3: Storage Systems](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Storage Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Storage Systems</p>
</div>

**作者**：Hyunsei Lee (DGIST), Jaewoo Gwak (DGIST), Shinhyoung Jang (DGIST), Junyoung Lee (DGIST), Yeseong Kim (DGIST)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803610)

## 英文摘要

Scalable video retrieval is increasingly challenging as datasets reach tens of millions of videos. Current text-to-video retrieval (T2VR) methods either compress videos into single dense vectors, losing segment-level detail, or expand them into multi-frame representations, incurring prohibitive storage and search costs. We propose a binary hyperdimensional representation that encodes each video into a compact 3,072-dimension hypervector, preserving semantic fidelity while reducing memory via bit-packing. To leverage the properties of hypervectors for sublinear search, we introduce Hypervector Retrieval (HVR), a frequency-aware inverted index that prioritizes rare informative positions and refines candidates using GPU-accelerated Hamming search. Experiments show that our approach matches or exceeds dense baselines for T2VR and surpasses state-of-the-art partially relevant video retrieval (PRVR) by over 5% Recall@10 on ActivityNet. At scale, HVR processes over 2,000 queries per second on 10M videos, maintains recall within 1% of exact search, and achieves 5.3× greater storage capacity than CLIP4Clip and over 2,116× over MS-SL.

## 中文摘要

随着数据集规模达到数千万个视频，可扩展的视频检索日益具有挑战性。当前的文本到视频检索（T2VR）方法要么将视频压缩为单个稠密向量，丢失片段级细节，要么将其扩展为多帧表示，带来高昂的存储与搜索开销。我们提出一种二值超维表示，将每个视频编码为紧凑的 3,072 维超向量，在保持语义保真度的同时通过位打包减少内存占用。为利用超向量的特性实现亚线性搜索，我们引入超向量检索（HVR），一种频率感知的倒排索引，它优先关注稀有但信息量大的位置，并使用 GPU 加速的汉明搜索精化候选。实验表明，我们的方法在 T2VR 上达到或超过稠密基线，并在 ActivityNet 上将部分相关视频检索（PRVR）的 Recall@10 超过最先进方法 5% 以上。在大规模场景下，HVR 在 1000 万个视频上每秒处理超过 2,000 次查询，召回率与精确搜索的差距保持在 1% 以内，存储容量达到 CLIP4Clip 的 5.3 倍、MS-SL 的 2,116 倍以上。

**英文关键词：** Video retrieval, Text-to-video retrieval, Partially relevant video retrieval, Hyperdimensional computing

**中文关键词：** 视频检索、文本到视频检索、部分相关视频检索、超维计算

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
