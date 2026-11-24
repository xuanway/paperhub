---
title: "SuperFE: A Scalable and Flexible Feature Extractor for ML-based Traffic Analysis Applications"
description: "EuroSys 2025 · ML systems · Menghao Zhang (Beihang University), Guanyu Li (Tsinghua University), Cheng Guo ("
tags:
  - "EuroSys2025"
  - "ML systems"
---

# SuperFE: A Scalable and Flexible Feature Extractor for ML-based Traffic Analysis Applications

**中文标题：** 面向机器学习流量分析应用的可扩展灵活特征提取器

**所属 Session：** [Session 6.1: ML systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML systems</p>
</div>

**作者**：Menghao Zhang (Beihang University), Guanyu Li (Tsinghua University), Cheng Guo (Tsinghua University), Renyu Yang (Beihang University), Shicheng Wang (Tsinghua University), Han Bao (Tsinghua University), Xiao Li (Tsinghua University), Mingwei Xu (Tsinghua University), Tianyu Wo (Beihang University), Chunming Hu (Beihang University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696081)

## 英文摘要

The feature extractor component in today’s ML-based traffic analysis applications is becoming a key bottleneck. While mainstream software-based approaches can support flexible feature extraction, they fail to scale to multi-100Gbps network speed easily. Meanwhile, hardware-accelerated solutions can scale to high throughput, but cannot flexibly support generic traffic analysis applications. In this paper, we propose SuperFE, a feature extraction framework that allows users to extract traffic features efficiently and flexibly. SuperFE leverages the capabilities of both new-generation programmable switches and SmartNICs, with three key designs. First, SuperFE presents a user-friendly and extensible interface to support customized feature extraction policies, shielding underlying hardware implementation details and complexities. Second, SuperFE introduces a high-performance multi-granularity key-vector cache system in the programmable switches to batch necessary feature metadata for massive amounts of packets. Third, SuperFE exploits the multi-core parallel and hierarchical memory of SoC-based SmartNICs to achieve efficient feature computation with diverse streaming algorithms. Evaluations using our prototype demonstrate that SuperFE enables various state-of-the-art traffic analysis applications to efficiently extract features from multi-100Gbps raw traffic without compromising detection accuracy, and achieves nearly two orders of magnitude higher throughput than the software-based counterparts.

## 中文摘要

如今基于 ML 的流量分析应用中的特征提取组件正成为关键瓶颈。主流基于软件的方法虽能支持灵活的特征提取，却难以轻松扩展到数百 Gbps 的网络速率。同时，硬件加速方案可扩展到高吞吐，但无法灵活支持通用的流量分析应用。本文提出 SuperFE，一个使用户能够高效、灵活地提取流量特征的特征提取框架。SuperFE 同时利用新一代可编程交换机和 SmartNIC 的能力，包含三项关键设计。第一，SuperFE 提供用户友好且可扩展的接口以支持定制化的特征提取策略，屏蔽底层硬件实现细节与复杂性。第二，SuperFE 在可编程交换机中引入高性能的多粒度键值缓存系统，为海量数据包批量汇集必要的特征元数据。第三，SuperFE 利用基于 SoC 的 SmartNIC 的多核并行与层次化内存，以多种流式算法实现高效的特征计算。基于我们原型的评估表明，SuperFE 使多种最先进的流量分析应用能够从数百 Gbps 的原始流量中高效提取特征而不损失检测精度，并且相比基于软件的同类方案实现了近两个数量级的吞吐提升。

**英文关键词：** Traffic Analysis, Feature Extractor, Programmable Switches, SmartNICs

**中文关键词：** 流量分析、特征提取器、可编程交换机、SmartNIC

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
