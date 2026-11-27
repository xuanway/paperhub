---
title: "Conflux: A High-Performance Keyword Private Retrieval System for Dynamic Datasets"
description: "HPCA 2026 · Zero-Knowledge and Private Information Retrieval"
tags:
  - "HPCA2026"
  - "Zero-Knowledge and Private Information Retrieval"
---

# Conflux: A High-Performance Keyword Private Retrieval System for Dynamic Datasets

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Zero-Knowledge and Private Information Retrieval。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Zero-Knowledge and Private Information Retrieval</p>
</div>

**论文链接**：
**作者**：Zehao Chen Shandong University , Zhaoyan Shen Shandong University , Qian Wei Shandong University , Hang Lu Institute of Computing Technology, Chinese Academy of Sciences , Lei Ju Shandong University
**会议**：HPCA 2026

---

## 中文标题

Conflux：面向动态数据集的高性能关键字隐私检索系统

## 英文摘要

Homomorphic Encryption (HE)–based Private Information Retrieval (PIR) allows clients to retrieve plaintext records from untrusted servers without revealing query content. While promising in theory, existing solutions fall short in practice due to two fundamental limitations: (1) poor support for dynamic datasets, which limits applicability in real-world, evolving workloads; and (2) excessive I/O overhead from full-database scans. These bottlenecks prevent current designs from bridging the gap between cryptographic privacy and system efficiency. In this paper, we introduce Conflux, an efficient keyword PIR system for dynamic data environments through a protocol-architecture co-design approach. At the protocol level, Conflux employs a novel two-phase retrieval mechanism, consisting of an oblivious filtering phase followed by a precise retrieval phase. This design natively supports efficient online insertions, deletions, and updates, while maintaining near-optimal computational complexity. At the system level, Conflux adopts a heterogeneous accelerator architecture that tightly couples computational storage devices and incorporates software–hardware co-optimization techniques to mitigate I/O bottlenecks. Experimental results show that Conflux reduces query processing time by up to 2.64× compared to the state-of-the-art methods, while retaining full support for dynamic datasets.

## 中文摘要

基于同态加密（HE）的隐私信息检索（PIR）允许客户端从不可信服务器取回明文记录而不泄露查询内容。尽管理论上颇具前景，现有方案在实践中仍受两个根本局限制约：（1）对动态数据集支持不足，限制了其在真实、不断演化的负载中的适用性；（2）全数据库扫描带来过高 I/O 开销。这些瓶颈使现有设计无法弥合密码学隐私与系统效率之间的差距。本文通过协议与架构协同设计，提出面向动态数据环境的高效关键字 PIR 系统 Conflux。在协议层面，Conflux 采用新颖的两阶段检索机制，包括不经意过滤阶段与随后的精确检索阶段，该设计原生支持高效的在线插入、删除与更新，同时保持接近最优的计算复杂度。在系统层面，Conflux 采用紧密耦合计算存储设备的异构加速器架构，并结合软硬件协同优化技术缓解 I/O 瓶颈。实验结果表明，相比最先进方法，Conflux 将查询处理时间最多缩短 2.64 倍，同时完整保留对动态数据集的支持。
