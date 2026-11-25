---
title: "Not A DPU in Name Only! Unleashing RDMA-capable DPUs in Multi-Tenant Serverless Clouds with NADINO"
description: "EuroSys 2026 · Datacenter Network Fabrics & RDMA · Shixiong Qi (University of Kentucky), Songyu Zhang (University of California, Ri"
tags:
  - "EuroSys2026"
  - "Datacenter Network Fabrics & RDMA"
---

# Not A DPU in Name Only! Unleashing RDMA-capable DPUs in Multi-Tenant Serverless Clouds with NADINO

**中文标题：** 不只是名义上的 DPU！用 NADINO 在多租户无服务器云中释放支持 RDMA 的 DPU 潜能

**所属 Session：** [Session 3.2: Datacenter Network Fabrics & RDMA](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Datacenter Network Fabrics & RDMA。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Datacenter Network Fabrics & RDMA</p>
</div>

**作者**：Shixiong Qi (University of Kentucky), Songyu Zhang (University of California, Riverside), K. K. Ramakrishnan (University of California, Riverside), Diman Zad Tootaghaj (Hewlett Packard Enterprise Labs), Hardik Soni (Hewlett Packard Labs), Puneet Sharma (Hewlett Packard Labs)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769386)

## 英文摘要

Serverless computing promises enhanced resource efficiency and lower user costs, yet is burdened by a heavyweight, CPU-bound data plane. Prior efforts exploiting shared memory reduce overhead locally but fall short when scaling across nodes. Furthermore, serverless environments can have unpredictable and large-scale multi-tenancy, leading to contention for shared network resources.

We present NADINO, a DPU-centric serverless data plane that reduces the CPU burden and enables efficient, zero-copy communication in multi-tenant serverless clouds. Despite the limited general-purpose processing capability of the DPU cores, NADINO strategically exploits the DPU’s potential by (1) offloading data transmission to high-performance NIC cores via RDMA, combined with intra-node shared memory to eliminate data copies across nodes, and (2) enabling cross-processor (CPU-DPU) shared memory to eliminate redundant data movement, which overwhelms wimpy DPU cores. At the core of NADINO is the DPU-enabled network engine (DNE) – a lightweight reverse proxy that isolates RDMA resources from tenant functions, orchestrates internode RDMA flows, and enforces fairness under contention.

To further reduce CPU involvement, NADINO performs early HTTP/TCP-to-RDMA transport conversion at the cloud ingress, bridging the protocol mismatch before client traffic enters the RDMA fabric, thus avoiding costly protocol translation along the critical path. We show that careful selection of RDMA primitives (i.e., two-sided instead of one-sided) significantly affects the zero-copy data plane.

Our preliminary experimental results show that enabling DPU offloading in NADINO improves RPS by 20.9×. The latency is reduced by a factor of 21× in the best case, all the while saving up to 7 CPU cores, and only consuming two wimpy DPU cores.

## 中文摘要

无服务器计算承诺更高的资源效率和更低的用户成本，却受制于一个重量级、CPU 密集的数据平面。先前利用共享内存的工作在本地降低了开销，但在跨节点扩展时效果不佳。此外，无服务器环境可能具有不可预测且大规模的多租户特性，从而导致对共享网络资源的争用。

我们提出 NADINO，一个以 DPU 为中心的无服务器数据平面，它减轻 CPU 负担，并在多租户无服务器云中实现高效的零拷贝通信。尽管 DPU 核心的通用处理能力有限，NADINO 仍策略性地挖掘 DPU 的潜力：(1) 通过 RDMA 将数据传输卸载到高性能网卡核心，并结合节点内共享内存消除跨节点的数据拷贝；(2) 启用跨处理器（CPU-DPU）共享内存，以消除会压垮孱弱 DPU 核心的冗余数据移动。NADINO 的核心是 DPU 赋能的网络引擎（DNE）——一个轻量级反向代理，它将 RDMA 资源与租户函数隔离、编排节点间 RDMA 流，并在争用时保障公平性。

为进一步减少 CPU 参与，NADINO 在云入口处提前完成 HTTP/TCP 到 RDMA 的传输转换，在客户端流量进入 RDMA 网络之前弥合协议不匹配，从而避免关键路径上昂贵的协议转换。我们表明，谨慎选择 RDMA 原语（即双边而非单边）会显著影响零拷贝数据平面。

初步实验结果表明，在 NADINO 中启用 DPU 卸载可将 RPS 提升 20.9 倍。最佳情况下延迟降低 21 倍，同时节省多达 7 个 CPU 核心，而仅消耗两个孱弱的 DPU 核心。

**英文关键词：** DPU, RDMA, Multi-tenancy, Serverless

**中文关键词：** DPU、RDMA、多租户、无服务器

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
