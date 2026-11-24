---
title: "Toleo: Scaling Freshness to Tera-scale Memory Using CXL and PIM"
description: "ASPLOS 2025 · Session 9B · Toleo：利用 CXL 与 PIM 将新鲜性保障扩展至太字节级内存"
tags:
  - "ASPLOS2025"
  - "Session 9B"
  - "Processing in Memory"
---

# Toleo: Scaling Freshness to Tera-scale Memory Using CXL and PIM

**中文标题：** Toleo：利用 CXL 与 PIM 将新鲜性保障扩展至太字节级内存

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Juechu Dong (University of Michigan), Jonah Rosenblum (University of Michigan), Satish Narayanasamy (University of Michigan)

**单位：** University of Michigan

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674180) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Trusted hardware's freshness guarantee ensures that an adversary cannot replay an old value in response to a memory read request. They rely on maintaining a version number for each cache block and ensuring their integrity using a Merkle tree. However, these existing solutions protect only a small amount of main memory (few MBs), as the extraneous memory accesses to the Merkle tree increase prohibitively with the protected memory size. We present Toleo, which uses trusted smart memory connected through a secure CXL IDE network to safely store version numbers. Toleo eliminates the need for an unscalable Merkle tree to protect the integrity of version numbers by instead using smart memory as the root of trust. Additionally, Toleo ensures version confidentiality which enables stealth versions that reduce the version storage overhead in half. Furthermore, in the absence of Merkle tree imposed constraints, we effectively exploit version locality at page granularity to compress version number by a factor of 240. These space optimizations make it feasible for one 168 GB Toleo smart memory device to provide freshness to a 28 TB CXLexpanded main memory pool in a rack server for a negligible performance overhead. We analyze the benefits of Toleo using several privacy-sensitive genomics, graph, generative AI, and database workloads.

## 中文摘要

可信硬件的新鲜性（freshness）保证确保攻击者无法针对一次内存读请求重放旧值。此类方案依赖为每个缓存块维护版本号，并使用 Merkle 树保证其完整性。然而，由于随着被保护内存规模的增大，对 Merkle 树的额外内存访问会增长到难以为继的程度，现有方案只能保护少量主存（数 MB）。我们提出 Toleo，它使用通过安全 CXL IDE 网络连接的可信智能内存（smart memory）来安全地存储版本号。Toleo 通过改用智能内存作为信任根，消除了以不可扩展的 Merkle 树来保护版本号完整性的需求。此外，Toleo 保证版本机密性，从而支持"隐蔽版本"（stealth versions），将版本存储开销减半。更进一步，在不受 Merkle 树所施加约束的情况下，我们有效利用页粒度的版本局部性，将版本号压缩 240 倍。这些空间优化使单个 168 GB 的 Toleo 智能内存设备能够以可忽略的性能开销，为机架服务器中 28 TB 的 CXL 扩展主存池提供新鲜性保障。我们使用若干隐私敏感的基因组、图、生成式 AI 与数据库工作负载分析了 Toleo 的收益。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674180)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2025](../index.md)
