---
title: "Scaling Out Chip Interconnect Networks with Implicit Sequence Numbers"
description: "SC 2025 · Architectures and Networks: Networking · Giyong Jung; Saeid Gorgin; John Kim; Jungrae Kim"
tags:
  - "SC2025"
  - "Architectures and Networks: Networking"
---

# Scaling Out Chip Interconnect Networks with Implicit Sequence Numbers

**中文标题：** 利用隐式序列号横向扩展芯片互连网络

**所属 Session：** [Architectures and Networks: Networking](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Networking。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Networking</p>
</div>

**作者**：Giyong Jung; Saeid Gorgin; John Kim; Jungrae Kim

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap552&sess=sess192)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

As AI models exceed single-processor limits, cross-chip interconnects are essential for scalable computing. These links transfer cache-line–sized data at high rates, driving adoption of protocols like CXL, NVLink, and UALink for high bandwidth and small payloads. Faster transfers, however, increase error risk. Standard methods such as CRC and FEC ensure link reliability, but scaling to multi-node systems introduces new challenges, including detecting silently dropped flits in switches. We present Implicit Sequence Number (ISN), which enables precise flit drop detection and in-order delivery without header overhead. We also propose Reliability Extended Link (RXL), a CXL extension integrating ISN to support scalable, reliable multi-node interconnects while preserving flit format. RXL elevates CRC to a transport-layer role for end-to-end data and sequence integrity, while FEC handles link-layer correction. This approach delivers robust reliability and scalability without reducing bandwidt

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
