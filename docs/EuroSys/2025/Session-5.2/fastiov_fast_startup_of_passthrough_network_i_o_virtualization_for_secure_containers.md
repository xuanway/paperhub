---
title: "FastIOV: Fast Startup of Passthrough Network I/O Virtualization for Secure Containers"
description: "EuroSys 2025 · Virtualization · Yunzhuo Liu (Shanghai Jiao Tong University & Alibaba Cloud), Junchen Guo (Alibab"
tags:
  - "EuroSys2025"
  - "Virtualization"
---

# FastIOV: Fast Startup of Passthrough Network I/O Virtualization for Secure Containers

**中文标题：** 加速安全容器直通网络 I/O 虚拟化的启动

**所属 Session：** [Session 5.2: Virtualization](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Virtualization</p>
</div>

**作者**：Yunzhuo Liu (Shanghai Jiao Tong University & Alibaba Cloud), Junchen Guo (Alibaba Cloud), Bo Jiang (Shanghai Jiao Tong University), Yang Song (Alibaba Cloud), Pengyu Zhang (Alibaba Cloud), Rong Wen (Alibaba Cloud), Biao Lyu (Zhejiang University & Alibaba Cloud), Shunmin Zhu (Hangzhou Feitian Cloud & Alibaba Cloud), Xinbing Wang (Shanghai Jiao Tong University), Song Yang (Alibaba Group)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696066)

## 英文摘要

Single Root I/O Virtualization (SR-IOV) technology has advanced in recent years and can simultaneously satisfy the network requirements of high data plane performance, high deployment density, and fast startup for applications in traditional containers. However, it falls short with secure containers, which have become the mainstream choice in multi-tenant clouds. SR-IOV requires secure containers to use passthrough I/O for higher data plane performance, which hinders the container startup performance and prevents its usage in time-sensitive tasks like serverless computing. In this paper, we advocate that the startup performance of SR-IOV enabled secure containers can be further boosted, making SR-IOV suitable for building a Container Network Interface (CNI) for secure containers. We first dissect the end-to-end concurrent startup process and identify three key bottlenecks that lead to the slow startup, including Virtual Function I/O device set management, Direct Memory Access memory mapping, and Virtual Function (VF) driver initialization. We then propose a CNI named FastIOV that addresses these bottlenecks through lock decomposition, unnecessary mapping skipping, decoupled zeroing, and asynchronous VF driver initialization. Our evaluation shows that FastIOV reduces the overhead of enabling SR-IOV for secure containers by 96.1%, achieving 65.7% and 75.4% reductions in the average and 99th percentile end-to-end startup time.

## 中文摘要

单根 I/O 虚拟化（SR-IOV）技术近年来取得进展，能够同时满足传统容器中应用对高数据面性能、高部署密度和快速启动的网络需求。然而，对于已成为多租户云主流选择的安全容器，它却力有不逮。SR-IOV 要求安全容器使用直通 I/O 以获得更高的数据面性能，这阻碍了容器的启动性能，使其无法用于无服务器计算等时间敏感任务。本文主张，启用 SR-IOV 的安全容器的启动性能可以进一步提升，从而使 SR-IOV 适合为安全容器构建容器网络接口（CNI）。我们首先剖析端到端的并发启动过程，识别出导致启动缓慢的三个关键瓶颈，包括虚拟功能 I/O 设备集管理、直接内存访问内存映射以及虚拟功能（VF）驱动初始化。随后，我们提出名为 FastIOV 的 CNI，通过锁分解、跳过不必要的映射、解耦清零和异步 VF 驱动初始化来解决这些瓶颈。我们的评估表明，FastIOV 将安全容器启用 SR-IOV 的开销降低了 96.1%，端到端启动时间的平均值和第 99 百分位分别降低 65.7% 和 75.4%。

**英文关键词：** Container Network, Passthrough I/O Virtualization, SR-IOV, Secure Container, Overlay Network Startup

**中文关键词：** 容器网络、直通 I/O 虚拟化、SR-IOV、安全容器、覆盖网络启动

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
