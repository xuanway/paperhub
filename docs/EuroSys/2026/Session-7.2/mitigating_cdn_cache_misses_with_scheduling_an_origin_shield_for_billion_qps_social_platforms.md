---
title: "Mitigating CDN Cache Misses with Scheduling: An Origin Shield for Billion-QPS Social Platforms"
description: "EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control · Zixuan Yang (State Key Laboratory for Novel Software Technology, Nanjing Univers"
tags:
  - "EuroSys2026"
  - "Traffic Engineering, CDNs & Congestion Control"
---

# Mitigating CDN Cache Misses with Scheduling: An Origin Shield for Billion-QPS Social Platforms

**中文标题：** 以调度缓解 CDN 缓存未命中：面向十亿级 QPS 社交平台的源站护盾

**所属 Session：** [Session 7.2: Traffic Engineering, CDNs & Congestion Control](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Traffic Engineering, CDNs & Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control</p>
</div>

**作者**：Zixuan Yang (State Key Laboratory for Novel Software Technology, Nanjing University), Yimeng Xu (State Key Laboratory for Novel Software Technology, Nanjing University), Jiaqi Zheng (State Key Laboratory for Novel Software Technology, Nanjing University), Boxi Liu (School of Computer Science, Central China Normal University), Guihai Chen (State Key Laboratory for Novel Software Technology, Nanjing University), Quan Xia (Tencent), He Lin (Tencent), Zhihai Huang (Tencent), Shangce Yuan (Tencent)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803578)

## 英文摘要

The explosive growth of modern short-video platforms like WeChat Channels — approaching 1.4 billion monthly active users (MAU) while serving over one billion queries per second (QPS) — has exposed fundamental limitations in conventional content delivery network (CDN) architectures, particularly their inability to handle highly dynamic content popularity patterns. The traditional cache-centric approach proves to be catastrophic when faced with ephemeral content exhibiting a "million-item waist" distribution. This phenomenon results in severe cache pollution (manifesting as 5–40% origin miss ratios) and introduces prohibitive back-to-origin bandwidth costs. Our TritonFlow overcomes these challenges by introducing access point scheduling as a novel origin traffic compensator, which reduces the operational cost of back-to-origin fetches by enhancing CDN cache affinity. Through analysis of production traces (peak >1B QPS), we demonstrate that TritonFlow reduces scheduling fluctuations by 96% and decreases back-to-origin traffic caused by non-compulsory cache misses by 35%, all while maintaining sub-200ms fetch latency.

## 中文摘要

微信视频号等现代短视频平台的爆发式增长——月活跃用户（MAU）接近 14 亿、每秒查询数（QPS）超过十亿——暴露了传统内容分发网络（CDN）架构的根本局限，尤其是其无法应对高度动态的内容热度模式。面对呈“百万条目腰部”分布的短时效内容时，以缓存为中心的传统方法被证明是灾难性的。这一现象导致严重的缓存污染（表现为 5–40% 的源站未命中率），并带来难以承受的回源带宽成本。我们的 TritonFlow 通过引入接入点调度作为一种新颖的源站流量补偿器来克服这些挑战，它通过增强 CDN 缓存亲和性降低回源拉取的运营成本。通过对生产环境跟踪数据（峰值 >1B QPS）的分析，我们表明 TritonFlow 将调度波动降低 96%，并将非强制性缓存未命中导致的回源流量降低 35%，同时保持低于 200 ms 的拉取延迟。

**英文关键词：** CDN, Traffic scheduling, Cache affinity, Social platform

**中文关键词：** CDN、流量调度、缓存亲和性、社交平台

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
