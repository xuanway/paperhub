---
title: "RpcNIC: Enabling Efficient Datacenter RPC Offloading on PCIe-attached SmartNICs"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# RpcNIC: Enabling Efficient Datacenter RPC Offloading on PCIe-attached SmartNICs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Jie Zhang (Zhejiang University), Hongjing Huang (Zhejiang University), Xuzheng Chen (Zhejiang university), Xiang Li (Zhejiang University), Jieru Zhao (Department of Computer Science and Engineering, Shanghai Jiao Tong University), Ming Liu (University of Wisconsin-Madison), Zeke Wang (Zhejiang University)
**会议**：HPCA 2025

---

## 中文标题

RpcNIC：在 PCIe 挂载的 SmartNIC 上实现高效数据中心 RPC 卸载

## 英文摘要

The emerging microservice/serverless-based cloud programming paradigm and the rising networking speeds leave the RPC stack as the predominant data center tax. Domain-specific hardware acceleration holds the potential to disentangle the overhead and save host CPU cycles. However, state-of-the-art RPC accelerators integrate RPC logic into the CPU or use specialized low-latency interconnects, hardly adopted in commodity servers. To this end, we design and implement RpcNIC, a software-hardware co-designed SmartNIC that enables efficient RPC layer offloading and reconfigurable RPC kernel offloading. RpcNIC connects to the server through the most widely used PCIe interconnect. To grapple with the ramifications of PCIe-induced challenges, RpcNIC introduces three techniques: (a) a target-aware deserializer that effectively batches cross-PCIe writes on the SmartNIC’s SRAM using compacted hardware data structures; (b) a memory-affinity CPU-SmartNIC collaborative serializer, which trades additional host memory copies for slow cross PCIe-transfers; (c) an automatic field update technique that transparently codifies the schema based on dynamic reconfigure RPC kernels to minimize superfluous PCIe traversals. We prototype RpcNIC using the Xilinx U280 FPGA card. On HyperProtoBench, RpcNIC achieves an average of 2.3× lower RPC layer processing time than a comparable RPC accelerator baseline and demonstrates 2.6× achievable throughput improvement in the end-to-end cloud workload.

## 中文摘要

新兴的基于微服务/无服务器的云编程范式与不断提升的网络速率，使 RPC 栈成为数据中心的主要开销。领域专用硬件加速有望化解该开销并节省主机 CPU 周期。然而最先进的 RPC 加速器或将 RPC 逻辑集成到 CPU 中，或采用专用低时延互连，难以在商用服务器中部署。为此，我们设计并实现了 RpcNIC，一个软硬件协同设计的 SmartNIC，可实现高效的 RPC 层卸载与可重构的 RPC 内核卸载。RpcNIC 通过最广泛使用的 PCIe 互连与服务器相连。为应对 PCIe 引入的种种影响，RpcNIC 引入三项技术：(a) 目标感知的反序列化器，利用紧凑的硬件数据结构在 SmartNIC 的 SRAM 上有效批量处理跨 PCIe 写；(b) 内存亲和性驱动的 CPU-SmartNIC 协同序列化器，用额外的主机内存拷贝换取缓慢的跨 PCIe 传输；(c) 自动字段更新技术，基于动态可重构的 RPC 内核透明地编码 schema，以最小化多余的 PCIe 穿越。我们使用 Xilinx U280 FPGA 卡实现了 RpcNIC 原型。在 HyperProtoBench 上，RpcNIC 的 RPC 层处理时间比同类 RPC 加速器基线平均降低 2.3 倍，并在端到端云负载中展现出 2.6 倍的可达吞吐提升。
