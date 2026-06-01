---
title: "Scaling Out Chip Interconnect Networks with Implicit Sequence Numbers"
description: "SC 2025 · Architectures and Networks: Networking · Giyong Jung; Saeid Gorgin; John Kim; Jungrae Kim"
tags:
  - "SC2025"
  - "Architectures and Networks: Networking"
---

# Scaling Out Chip Interconnect Networks with Implicit Sequence Numbers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Networking。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Networking</p>
</div>

**作者**：Giyong Jung; Saeid Gorgin; John Kim; Jungrae Kim

**会议**：SC 2025 · St. Louis, MO

## 摘要

As AI models exceed single-processor limits, cross-chip interconnects are essential for scalable computing. These links transfer cache-line–sized data at high rates, driving adoption of protocols like CXL, NVLink, and UALink for high bandwidth and small payloads. Faster transfers, however, increase error risk. Standard methods such as CRC and FEC ensure link reliability, but scaling to multi-node systems introduces new challenges, including detecting silently dropped flits in switches. We present Implicit Sequence Number (ISN), which enables precise flit drop detection and in-order delivery without header overhead. We also propose Reliability Extended Link (RXL), a CXL extension integrating ISN to support scalable, reliable multi-node interconnects while preserving flit format. RXL elevates CRC to a transport-layer role for end-to-end data and sequence integrity, while FEC handles link-layer correction. This approach delivers robust reliability and scalability without reducing bandwidt

---

## 一句话总结

> 该工作属于 Architectures and Networks: Networking 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Architectures and Networks: Networking 领域贡献新的设计范式或评估框架。
