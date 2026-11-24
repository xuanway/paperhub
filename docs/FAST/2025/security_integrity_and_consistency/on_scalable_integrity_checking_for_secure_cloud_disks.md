---
title: "On Scalable Integrity Checking for Secure Cloud Disks"
description: "FAST 2025 · Security, Integrity, and Consistency · 把完整性哈希树改成随访问热度自调整的不平衡结构，吞吐最高提升 2.2 倍"
tags:
  - "FAST2025"
  - "Security, Integrity, and Consistency"
  - "Merkle hash tree"
  - "integrity checking"
---

# On Scalable Integrity Checking for Secure Cloud Disks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Merkle 哈希树保护云盘完整性，但树高随容量增长，1 TB 盘每次 I/O 至少算 28 个哈希。作者在 AWS EC2 与 NVMe 上量化开销，提出按访问偏斜自调整的 Dynamic Merkle Trees，达到最优吞吐的 85% 以上，吞吐与延迟最多改善 2.2 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Security, Integrity, and Consistency</p>
</div>

**中文标题**：面向安全云盘的可扩展完整性校验

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/burke](https://www.usenix.org/conference/fast25/presentation/burke)

**论文 PDF**：[fast25-burke.pdf](https://www.usenix.org/system/files/fast25-burke.pdf)

**作者**：Quinn Burke、Ryan Sheatsley、Rachel King、Owen Hines、Michael Swift、Patrick McDaniel（University of Wisconsin–Madison）

**会议**：FAST 2025 · Santa Clara, CA · 第 391–405 页

**Session**：Security, Integrity, and Consistency · 2025-02-26 14:00–15:40 · Chair：Hyungon Moon（UNIST (Ulsan National Institute of Science and Technology)）

**所属 Session**：[Security, Integrity, and Consistency](index.md) · [FAST 2025](../index.md)

**关键词**：Merkle hash tree, integrity checking, cloud block storage, confidential VM, splay tree, hash cache

---

## 英文摘要

Merkle hash trees are the standard method to protect the integrity and freshness of stored data. However, hash trees introduce additional compute and I/O costs on the I/O critical path, and prior efforts have not fully characterized these costs. In this paper, we quantify performance overheads of storage-level hash trees in realistic settings. We then design an optimized tree structure called Dynamic Merkle Trees (DMTs) based on an analysis of root causes of overheads. DMTs exploit patterns in workloads to deliver up to a 2.2X throughput and latency improvement over the state of the art. Our novel approach provides a promising new direction to achieve integrity guarantees in storage efficiently and at scale.

## 中文摘要

Merkle 哈希树是保护存储数据完整性与新鲜性的标准方法。然而，哈希树在 I/O 关键路径上引入了额外的计算与 I/O 开销，而此前工作尚未完整刻画这些开销。本文在真实环境中量化存储级哈希树的性能开销，并基于对开销根因的分析，设计了一种优化的树结构——动态 Merkle 树（DMT）。DMT 利用工作负载中的模式，相比最先进方案带来最高 2.2 倍的吞吐与延迟改善。本文的新方法为实现高效、可扩展的存储完整性保证提供了有前景的新方向。

## 一句话总结

> 哈希树的主要开销是 CPU 哈希而不是元数据 I/O；把树做成随热块自调整的 splay 结构，开销就会随负载偏斜一起降下来。

## 研究背景与问题

- **可信云盘的必备组件**：Merkle 哈希树同时提供真实性与新鲜性，是 Linux dm-verity 校验启动盘、机密虚拟机保护挂载盘的标准做法，根哈希存放在 TPM 或片上持久寄存器里。
- **开销随容量对数增长**：1 TB 盘约有 268 M 个 4 KB 块，对应的平衡二叉树树高为 28，任何一次读写都至少要算 28 个哈希；取元数据加验证哈希的总耗时可以超过数百 µs，而高性能设备上数据访问本身低于 60 µs。
- **已有结论搬不过来**：Penglai、FastVer、VAULT 等工作表明缓存与提高树度数能在小容量等场景降低开销，但其语境主要是安全内存；块存储的容量、写密集比例与缓存行为都不同，部分工作还在更新时抑制缓存或只评估读密集、只读负载，回避了写路径的真实开销。
- **本文的切入点**：先量化根因、确认瓶颈在 CPU 哈希，再把“最优哈希树”归约为无损压缩中的“最优前缀树”问题，并用在线学习逼近它。

## 核心贡献

- **开销的实测刻画**：在 AWS EC2 与 NVMe 设备的真实环境中，按容量、读写比、I/O 大小、缓存大小系统测量存储级哈希树的吞吐与延迟，给出容量从 16 MB 到 4 TB 的衰减曲线。
- **根因定位**：把写路径拆成数据 I/O、取元数据与哈希更新三段，证明 CPU 哈希成本才是主要瓶颈，而不是取哈希的元数据 I/O。
- **最优树的等价刻画**：证明在已知负载分布下，寻找最优哈希树等价于构造最优前缀码，从而说明最优树远非平衡——热块应当拥有更短的验证与更新路径。
- **Dynamic Merkle Trees（DMT）**：以 splay 树为基础、节点带热度计数的动态不平衡哈希树，无需先验知识即可在线逼近最优结构，作为块设备驱动可直接插入 Linux。

## 方法与技术要点

- **部署位置**：实现为包裹下层驱动的块设备驱动，向文件系统暴露 /dev/XXX，与 dm-verity 所处的位置一致；写时沿认证路径更新叶到根并保存新的根哈希。
- **读路径与缓存**：读块先校验 MAC，再取兄弟哈希构成证明；安全内存中的哈希缓存支持提前返回，命中已认证节点即停止向上验证，因此读密集负载的缓存命中率超过 99%。
- **写路径是主战场**：写密集负载下每次写都要重算路径上全部哈希，无法像读那样靠提前返回省掉，DMT 因此把优化目标放在缩短热块的路径长度上。
- **自调整结构**：节点带 hotness 计数器，以 splay 树的自调整方式把频繁访问的块向根方向提升，使树形随访问偏斜演化；树不再平衡，节点必须显式保存父子指针（整数 node ID）。
- **不放松安全语义**：只做立即验证、不使用 lazy verification，根哈希仍存放在安全位置，因此新鲜性保证与基线一致，优化全部来自树形与缓存。

## 评估与主要结果

- **平台与负载**：AWS EC2 实例加 NVMe 设备；负载包括 Zipfian 系列（如 Zipf(2.5)、读比例 1%、I/O 32 KB、缓存 10%）、Alibaba 数据集 trace 与 Filebench OLTP，并按容量、读写比、I/O 大小扫参数。
- **基线失效**：dm-verity 式平衡二叉树在全部实验中平均只跑到最优吞吐的 50% 以下；容量 16 MB 时吞吐损失接近 60%，到 4 TB 升为 75%，结论中给出的上界是 80%。
- **DMT 效果**：达到最优吞吐的 85% 以上，吞吐与延迟相对现有最优方案最多改善 2.2 倍。
- **缓存经济性**：DMT 在 0.1% 的缓存预算下即优于二叉树在 1% 缓存下的表现，说明收益来自树形而非堆缓存。

[返回 Security, Integrity, and Consistency](index.md) · [返回 FAST 2025](../index.md)
