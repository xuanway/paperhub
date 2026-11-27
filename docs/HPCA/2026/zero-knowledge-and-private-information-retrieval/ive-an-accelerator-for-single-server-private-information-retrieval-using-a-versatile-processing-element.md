---
title: "IVE: An Accelerator for Single-Server Private Information Retrieval Using a Versatile Processing Element"
description: "HPCA 2026 · Zero-Knowledge and Private Information Retrieval"
tags:
  - "HPCA2026"
  - "Zero-Knowledge and Private Information Retrieval"
---

# IVE: An Accelerator for Single-Server Private Information Retrieval Using a Versatile Processing Element

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Zero-Knowledge and Private Information Retrieval。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Zero-Knowledge and Private Information Retrieval</p>
</div>

**论文链接**：[https://arxiv.org/abs/2512.01574](https://arxiv.org/abs/2512.01574)
**作者**：Sangpyo Kim Seoul National University , Hyesung Ji Seoul National University , Jongmin Kim Seoul National University , Jaiyoung Park Seoul National University , Wonseok Choi Seoul National University , Jung Ho Ahn Seoul National University
**会议**：HPCA 2026

---

## 中文标题

IVE：基于通用处理单元的单服务器隐私信息检索加速器

## 英文摘要

Private information retrieval (PIR) is an essential cryptographic protocol for privacy-preserving applications, enabling a client to retrieve a record from a server’s database without revealing which record was requested. Single-server PIR based on homomorphic encryption has particularly gained immense attention for its ease of deployment and reduced trust assumptions. However, single-server PIR remains impractical due to its high computational and memory bandwidth demands. Specifically, reading the entirety of large databases from storage, such as SSDs, severely limits its performance. To address this, we propose IVE, an accelerator for single-server PIR with a systematic extension that enables practical retrieval from large databases using DRAM. Recent advances in DRAM capacity allow PIR for large databases to be served entirely from DRAM, removing its dependence on storage bandwidth. Although the memory bandwidth bottleneck still remains, multi-client batching effectively amortizes database access costs across concurrent requests to improve throughput. However, client-specific data remains a bottleneck, whose bandwidth requirements ultimately limits performance. IVE overcomes this by employing a large on-chip scratchpad with an operation scheduling algorithm that maximizes data reuse, further boosting throughput. Additionally, we introduce sysNTTU, a versatile functional unit that enhances area efficiency without sacrificing performance. We also propose a heterogeneous memory system architecture, which enables a linear scaling of database sizes without a throughput degradation. Consequently, IVE achieves up to 1,275× higher throughput compared to prior PIR hardware solutions.

## 中文摘要

隐私信息检索（PIR）是隐私保护应用中必不可少的密码协议，使客户端能从服务器数据库取回记录而不泄露所请求的记录。基于同态加密的单服务器 PIR 因易于部署且信任假设更少而尤受关注，但其高昂的计算与内存带宽需求仍使其实用性受限：从 SSD 等存储读取整个大型数据库严重限制性能。为此，我们提出 IVE，一种单服务器 PIR 加速器，并提供系统性扩展，使大型数据库可借助 DRAM 实用化检索。DRAM 容量的近期进展使大型数据库的 PIR 可完全由 DRAM 服务，消除对存储带宽的依赖；内存带宽瓶颈虽仍存在，多客户端批处理能有效将数据库访问开销分摊到并发请求上以提升吞吐。然而客户端专属数据仍是瓶颈，其带宽需求最终限制性能；IVE 通过大容量片上便笺存储器与最大化数据复用的操作调度算法克服这一问题，进一步提升吞吐。此外，我们提出 sysNTTU，一种多功能功能单元，在不牺牲性能的前提下提升面积效率，并提出异构内存系统架构，使数据库规模可线性扩展而不引起吞吐下降。因此，相比先前的 PIR 硬件方案，IVE 的吞吐最高提升 1,275 倍。
