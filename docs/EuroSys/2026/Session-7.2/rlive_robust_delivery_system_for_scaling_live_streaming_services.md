---
title: "RLive: Robust Delivery System for Scaling Live Streaming Services"
description: "EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control · Yu Tian (Institute of Computing Technology, University of Chinese Academy of Sci"
tags:
  - "EuroSys2026"
  - "Traffic Engineering, CDNs & Congestion Control"
---

# RLive: Robust Delivery System for Scaling Live Streaming Services

**中文标题：** RLive：用于扩展直播服务的鲁棒分发系统

**所属 Session：** [Session 7.2: Traffic Engineering, CDNs & Congestion Control](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Traffic Engineering, CDNs & Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control</p>
</div>

**作者**：Yu Tian (Institute of Computing Technology, University of Chinese Academy of Sciences), Gerui Lv (ICT, CAS), Qinghua Wu (ICT/CAS), Ruili Fang (ByteDance), Yajie Peng (ByteDance), Zhichen Xue (Bytedance), Rui Han (ByteDance Ltd. Beijing), Chuanqing Lin (ICT, CAS; UCAS, China), Xiaofei Pang (ByteDance), Ri Lu (ByteDance), Zhenyu Li (ICT, CAS)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769360)

## 英文摘要

As the demand for streaming services surges, content delivery network (CDN) operators face increasing pressure to scale live video delivery without proportionally increasing infrastructure costs. While best-effort edge resources offer a cost-effective extension to traditional CDN capacity, their limited bandwidth and unstable performance pose significant challenges. Our operational experience shows that naively layering such resources onto existing CDN infrastructure falls short in meeting performance and scalability demands. This paper presents RLive, a robust delivery system that scales CDN capacity by integrating best-effort edge resources. RLive features a redundancy-free multi-source data plane to support reliable and cost-efficient live streaming, along with a multi-layer collaborative control plane that combines the global view with local adaptability for scalable user-to-node mapping. Deployed in ByteDance CDN to support large-scale live streaming services with hundreds of millions of daily viewers, RLive has tripled delivery capacity while reducing rebuffering events by 14.9–20.1%.

## 中文摘要

随着流媒体服务需求的激增，内容分发网络（CDN）运营商面临着在不按比例增加基础设施成本的前提下扩展直播视频分发的越来越大的压力。尽力而为的边缘资源为传统CDN容量提供了一种高性价比的扩展，但其有限的带宽和不稳定的性能带来了重大挑战。我们的运维经验表明，将此类资源简单叠加到现有CDN基础设施之上无法满足性能与可扩展性需求。本文提出RLive，一个通过整合尽力而为边缘资源来扩展CDN容量的鲁棒分发系统。RLive具有无冗余的多源数据平面，以支持可靠且高性价比的直播，并配有多层协同控制平面，将全局视图与局部适应性相结合，实现可扩展的用户到节点映射。RLive部署在字节跳动CDN中，支撑每日数亿观众的规模化直播服务，将分发容量提升至三倍，同时将卡顿事件减少14.9%–20.1%。

**英文关键词：** Content delivery network, Live streaming services, Distributed system, Quality of experience (QoE)

**中文关键词：** 内容分发网络、直播服务、分布式系统、体验质量（QoE）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
