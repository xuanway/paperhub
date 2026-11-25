---
title: "EMVOD: Elastic Multi-Path QUIC Scheduling for CDN Video-on-Demand Service"
description: "EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control · ZiQi Wei (Tsinghua Shenzhen International Graduate School), Qing Li (Peng Cheng "
tags:
  - "EuroSys2026"
  - "Traffic Engineering, CDNs & Congestion Control"
---

# EMVOD: Elastic Multi-Path QUIC Scheduling for CDN Video-on-Demand Service

**中文标题：** EMVOD：面向 CDN 视频点播服务的弹性多路径 QUIC 调度

**所属 Session：** [Session 7.2: Traffic Engineering, CDNs & Congestion Control](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Traffic Engineering, CDNs & Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control</p>
</div>

**作者**：ZiQi Wei (Tsinghua Shenzhen International Graduate School), Qing Li (Peng Cheng Laboratory), TianYun Zhao (Tsinghua Shenzhen International Graduate School), Cheng Luo (Tencent), ChangKui OuYang (Tencent), XiaoFei Yu (Tencent), DaYi Zhao (Peng Cheng Laboratory), Yong Jiang (Tsinghua Shenzhen International Graduate School)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803585)

## 英文摘要

Video-on-demand (VoD) is one of the core CDN services, yet current VoD services commonly face video stuttering and long first-frame latency due to poor transmission path conditions. Existing solutions using Multi-path QUIC (MPQUIC) to address these issues cannot activate cellular paths on demand, causing massive traffic waste; additionally, some solutions depend on dedicated clients for application-layer information, precluding large-scale deployment. To address these limitations, we propose EMVOD, an elastic multi-path QUIC scheme deployed only on CDN edge nodes. It parses client-requested videos, dynamically activates cellular networks on demand, and prioritizes smooth video playback with minimal cellular traffic, while significantly reducing stuttering duration and first-frame latency.

We evaluated EMVOD under different network conditions using a controlled testbed. Experimental results demonstrate that: 1) Compared to conventional multi-path QUIC scheduling schemes, EMVOD saves up to 97.5% of cellular bandwidth. 2) EMVOD consistently reduces video stuttering duration and first-frame latency across all tested scenarios. Under ideal conditions, it eliminates video stuttering entirely and reduces first-frame latency by 45.40% compared to single-path transmission and by 34.21% compared to other multi-path baselines.

## 中文摘要

视频点播（VoD）是 CDN 的核心服务之一，然而当前 VoD 服务常因传输路径状况不佳而面临视频卡顿与首帧延迟过长的问题。现有使用多路径 QUIC（MPQUIC）解决这些问题的方案无法按需激活蜂窝路径，造成大量流量浪费；此外，部分方案依赖专用客户端获取应用层信息，难以大规模部署。为克服这些局限，我们提出 EMVOD，一种仅部署在 CDN 边缘节点上的弹性多路径 QUIC 方案。它解析客户端请求的视频，按需动态激活蜂窝网络，并以最少的蜂窝流量优先保障视频播放的流畅性，同时显著降低卡顿时长与首帧延迟。

我们在受控测试床上评估了 EMVOD 在不同网络条件下的表现。实验结果表明：1）与传统多路径 QUIC 调度方案相比，EMVOD 最多可节省 97.5% 的蜂窝带宽；2）EMVOD 在所有测试场景中均能持续降低视频卡顿时长与首帧延迟。在理想条件下，它完全消除了视频卡顿，相比单路径传输将首帧延迟降低 45.40%，相比其他多路径基线降低 34.21%。

**英文关键词：** QUIC, Multipath Transmission, Content Delivery Network, Video on Demand

**中文关键词：** QUIC、多路径传输、内容分发网络、视频点播

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
