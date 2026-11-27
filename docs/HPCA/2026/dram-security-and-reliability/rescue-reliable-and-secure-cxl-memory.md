---
title: "ReScue: Reliable and Secure CXL Memory"
description: "HPCA 2026 · DRAM Security and Reliability"
tags:
  - "HPCA2026"
  - "DRAM Security and Reliability"
---

# ReScue: Reliable and Secure CXL Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: DRAM Security and Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM Security and Reliability</p>
</div>

**论文链接**：
**作者**：Chihun Song UIUC , Austin Antony Cruz UIUC , Michael Jaemin Kim Meta , Minbok Wi Seoul National University , Gaohan Ye UIUC , Kyungsan Kim Samsung Electronics , Sangyeol Lee Samsung Electronics , Jung Ho Ahn Seoul National University , Nam Sung Kim UIUC
**会议**：HPCA 2026

---

## 中文标题

ReScue：可靠且安全的 CXL 内存

## 英文摘要

Compute Express Link (CXL) fundamentally shifts the memory abstraction boundary, moving memory management functions from the host CPU to external controllers. While this decoupling allows hyperscalers to integrate diverse media, such as cost-effective, recycled DDR4 modules, it transforms the memory controller into a complex system with new integration challenges. First, we uncover that integrating CXL and memory controller IPs via the industry-standard AXI interconnect creates critical bottlenecks. We demonstrate that variable access latency and out-of-order responses, essential for CXL, can quickly saturate the limited AXI tag space, limiting bandwidth and even causing system hangs in commercial platforms. However, this decoupled architecture also creates a unique opportunity: the CXL controller can exploit its support for variable-latency responses and near-memory processing to implement transparent reliability and security mechanisms. We propose ReScue, a suite of hardware solutions implemented and validated on an Intel Agilex platform. ReScue-R leverages CXL’s variable access latency and out-of-order responses to transparently retrieve remapping addresses stored within faulty blocks. By utilizing a Bloom filter to predict faults and minimize overhead, it achieves fault tolerance 9.6 × 104 times higher than standard SECDED ECC with only 0.2% performance degradation. ReScue-S addresses security; after demonstrating the first successful Row Hammer (RH) bit flips and physicaladdress reconstruction on a CXL system, we show that ReScue-S can shape response latencies to prevent timing-based side-channel attacks with only 1.1% performance degradation. Finally, we propose a solution to the discovered AXI-induced system hangs to ensure stable CXL operation.

## 中文摘要

计算快速链路（CXL）根本性地改变了内存抽象边界，将内存管理功能从宿主 CPU 移至外部控制器。这种解耦使超大规模厂商可集成多样介质（如经济可回收的 DDR4 模块），也使内存控制器演变为具有新集成挑战的复杂系统。我们发现通过业界标准 AXI 互连集成 CXL 与内存控制器 IP 会造成关键瓶颈：CXL 必不可少的可变访问时延与乱序响应会迅速耗尽有限的 AXI 标签空间，限制带宽，甚至在商用平台导致系统挂起。但解耦也带来机遇：CXL 控制器可利用对可变时延响应与近内存处理的支持，实现透明的可靠性与安全机制。我们提出 ReScue，一套在 Intel Agilex 平台上实现并验证的硬件方案。ReScue-R 利用可变访问时延与乱序响应透明取回故障块内存储的重映射地址，借 Bloom 过滤器预测故障，实现比标准 SECDED ECC 高 9.6 × 104 倍的容错，性能仅下降 0.2%。ReScue-S 面向安全：在首次于 CXL 系统上演示 Row Hammer（RH）位翻转与物理地址重构之后，我们表明它可通过塑造响应时延阻止时序侧信道攻击，性能仅下降 1.1%。最后我们针对 AXI 引发的系统挂起提出解决方案，以保证 CXL 稳定运行。
