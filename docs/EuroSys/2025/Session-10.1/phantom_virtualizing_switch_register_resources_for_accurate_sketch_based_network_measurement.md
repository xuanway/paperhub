---
title: "Phantom: Virtualizing Switch Register Resources for Accurate Sketch-based Network Measurement"
description: "EuroSys 2025 · Network - Van Oldebarneveldt · Xiang Chen (Zhejiang University), Hongyan Liu (Zhejiang University), Zhengyan Zh"
tags:
  - "EuroSys2025"
  - "Network - Van Oldebarneveldt"
---

# Phantom: Virtualizing Switch Register Resources for Accurate Sketch-based Network Measurement

**中文标题：** 虚拟化交换机寄存器资源，实现精确的基于草图的网络测量

**所属 Session：** [Session 10.1: Network](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Network - Van Oldebarneveldt。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Network - Van Oldebarneveldt</p>
</div>

**作者**：Xiang Chen (Zhejiang University), Hongyan Liu (Zhejiang University), Zhengyan Zhou (Zhejiang University), Xi Sun (Zhejiang University), Wenbin Zhang (Zhejiang University), Hongyang Du (The University of Hong Kong), Dong Zhang (Fuzhou University), Xuan Liu (Yangzhou University and Southeast University), Haifeng Zhou (Zhejiang University), Dusit Niyato (Nanyang Technological University), Qun Huang (Peking University), Chunming Wu (Zhejiang University), Kui Ren (Zhejiang University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696077)

## 英文摘要

Sketches have proven to be useful for measuring traffic. They store measurement results in the registers of data plane switches. However, they suffer from the short of switch register resources, limiting their measurement accuracy.

We propose Phantom, a framework that virtualizes register resources on programmable switches. We observe that in addition to original register resources, switches also offer the capability of data recirculation. Such a capability can be utilized to store some measurement data of sketches, enabling Phantom to realize virtual registers. We realize this insight by building Phantom on a 64×100 Gbps Tofino switch. Our testbed experiments indicate that Phantom can virtualize O(106) registers under Tbps-level traffic, which brings up to 86% accuracy improvement to sketches.

## 中文摘要

Sketch 已被证明可用于流量测量。它们将测量结果存储在数据平面交换机的寄存器中。然而，它们受制于交换机寄存器资源不足，测量精度因此受到限制。

我们提出 Phantom，一个在可编程交换机上虚拟化寄存器资源的框架。我们观察到，除了原有的寄存器资源之外，交换机还提供数据再循环的能力。这种能力可用于存储 sketch 的部分测量数据，使 Phantom 得以实现虚拟寄存器。我们在一台 64×100 Gbps 的 Tofino 交换机上构建 Phantom，实现了这一思路。测试床实验表明，Phantom 可在 Tbps 级流量下虚拟化 O(10^6) 个寄存器，为 sketch 带来最高 86% 的精度提升。

**英文关键词：** Network Measurement; Sketch; Network-Wide Deployment

**中文关键词：** 网络测量、Sketch、全网部署

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
