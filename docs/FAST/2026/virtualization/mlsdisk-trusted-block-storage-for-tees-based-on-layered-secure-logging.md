---
title: "MlsDisk: Trusted Block Storage for TEEs Based on Layered Secure Logging"
description: "FAST 2026 · Virtualization · 第 443–460 页"
tags:
  - "FAST2026"
  - "Virtualization"
---

# MlsDisk: Trusted Block Storage for TEEs Based on Layered Secure Logging

**中文标题**：MlsDisk：基于分层安全日志的 TEE 可信块存储

**Session**：Virtualization · 2026-02-25 16:10–17:30 · Chair：Mai Zheng（Iowa State University）

**作者**：Erci Xu, Shanghai Jiao Tong University; Xinyi Yu, Lujia Yin, and Xinyuan Luo, NICE Lab, Xiamen University; Shaowei Song, Qingsong Chen, and Shoumeng Yan, Ant Group; Jiwu Shu, Tsinghua University; Hongliang Tian, Ant Group; Yiming Zhang, Shanghai Jiao Tong University and NICE Lab, Xiamen University

**会议**：FAST 2026 · Santa Clara, CA · 第 443–460 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/xu](https://www.usenix.org/conference/fast26/presentation/xu)

**论文 PDF**：[fast26-xu.pdf](https://www.usenix.org/system/files/fast26-xu.pdf)

---

## 英文摘要

Trusted Execution Environments (TEEs) enable users to run sensitive applications in private memory regions. SGX-PFS is the state-of-the-art secure storage solution for TEEs that ensures data confidentiality, integrity, freshness, and consistency (CIFC). Unfortunately, SGX-PFS uses Merkle Hash Trees to protect in-place persisted data and suffers from poor I/O performance and is thus of limited use in practice.

This paper presents MlsDisk, a secure virtual disk that adopts out-of-place logging to provide efficient trusted block storage for TEEs. The challenge is that the complexity of indexing and garbage collection (GC) in log-structured storage makes it difficult to ensure security. We therefore adopt a layered design to break down the indexing and GC into four layers of abstractions, which facilitates reasoning about CIFC properties. Evaluation shows that MlsDisk, with CIFC guarantees, outperforms SGX-PFS by 7.3×–21.1× on microbenchmarks and 1.4×–3.6× on trace-driven workloads.

## 中文摘要

可信执行环境（TEE）使用户能够在私有内存区域中运行敏感应用。SGX-PFS 是面向 TEE 的最先进安全存储方案，可确保数据机密性、完整性、新鲜性和一致性（CIFC）。遗憾的是，SGX-PFS 使用 Merkle 哈希树来保护原地持久化数据，I/O 性能较差，因而在实际应用中用途有限。

本文提出 MlsDisk，一种采用异地日志为 TEE 提供高效可信块存储的安全虚拟磁盘。其挑战在于，日志结构存储中索引和垃圾回收（GC）的复杂性使得确保安全性变得困难。因此，我们采用分层设计，将索引和 GC 分解为四层抽象，从而便于推理 CIFC 属性。评估表明，在具备 CIFC 保证的情况下，MlsDisk 在微基准上比 SGX-PFS 快 7.3–21.1 倍，在跟踪驱动负载上快 1.4–3.6 倍。
