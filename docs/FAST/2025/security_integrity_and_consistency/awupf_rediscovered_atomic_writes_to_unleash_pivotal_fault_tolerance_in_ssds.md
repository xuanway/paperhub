---
title: "AWUPF Rediscovered: Atomic Writes to Unleash Pivotal Fault-Tolerance in SSDs"
description: "FAST 2025 · Security, Integrity, and Consistency · 用 NVMe 的 4 KB AWUPF 原子写替掉日志，随机写最高提升 3.6 倍"
tags:
  - "FAST2025"
  - "Security, Integrity, and Consistency"
  - "AWUPF"
  - "atomic write"
---

# AWUPF Rediscovered: Atomic Writes to Unleash Pivotal Fault-Tolerance in SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">SSD 的页级原子性已标准化为 NVMe 的 AWUPF，多数盘为 4 KB，主机侧几乎没用起来。作者在 Poseidon OS 的 Log-RAID 上让 AWUPF 内的映射更新绕过 journal 直写 mpage，更大更新仍走日志，随机写最高提升 3.6 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Security, Integrity, and Consistency</p>
</div>

**中文标题**：重新发现 AWUPF：以原子写释放 SSD 的关键容错能力

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/jeon](https://www.usenix.org/conference/fast25/presentation/jeon)

**论文 PDF**：[fast25-jeon.pdf](https://www.usenix.org/system/files/fast25-jeon.pdf)

**作者**：Jiyune Jeon、Jongseok Kim（Sungkyunkwan University）；Sam H. Noh（Virginia Tech）；Euiseong Seo（Sungkyunkwan University）

**会议**：FAST 2025 · Santa Clara, CA · 第 441–448 页

**Session**：Security, Integrity, and Consistency · 2025-02-26 14:00–15:40 · Chair：Hyungon Moon（UNIST (Ulsan National Institute of Science and Technology)）

**所属 Session**：[Security, Integrity, and Consistency](index.md) · [FAST 2025](../index.md)

**关键词**：AWUPF, atomic write, Log-RAID, journaling, crash consistency, NVMe

---

## 英文摘要

From their inception, SSDs have ensured the atomicity of writes at the flash page level, guaranteeing their completion even during power failures. This functionality has been standardized as Atomic Write Unit Power Fail (AWUPF) in the NVMe standard. Despite SSDs providing AWUPF ranging from several to tens of KBs, there has been little effort on the host side to utilize this capability. For instance, if a transaction is smaller than the AWUPF size, leveraging AWUPF can eliminate the need for write-ahead logging or journaling. In this paper, we showcase how AWUPF reduces the overhead of host-side transactional writes through a light-weight crash consistency implementation for log-structured RAID (Log-RAID). Log-RAID manages the mapping of externally-exposed logical block numbers to their dynamically changing physical locations. Our approach bypasses journaling for updates of these mappings within the AWUPF limit, allowing direct writes instead. For larger updates, conventional journaling is applied. Additionally, our approach addresses the ordering issues between these two update paths. The evaluation of the proposed approach on Poseidon OS showed up to 3.6x improvement in random write performance.

## 中文摘要

SSD 自诞生起就在 flash page 级别保证写的原子性，即使发生掉电也能保证完成。该功能已在 NVMe 标准中被定义为 Atomic Write Unit Power Fail（AWUPF）。尽管 SSD 提供的 AWUPF 从几 KB 到数十 KB 不等，主机侧却鲜有利用这一能力的努力。例如，当事务小于 AWUPF 大小时，利用 AWUPF 可以省去 write-ahead logging 或 journaling。本文以日志结构 RAID（Log-RAID）为例，通过一种轻量级的崩溃一致性实现，展示 AWUPF 如何降低主机侧事务写的开销。Log-RAID 管理外部暴露的逻辑块号到其动态变化的物理位置的映射。本文的方法对 AWUPF 限制内的映射更新绕过 journaling，允许直接写入；对于更大的更新，则仍采用传统 journaling。此外，本文的方法处理了这两条更新路径之间的顺序问题。在 Poseidon OS 上的评估表明，所提方法的随机写性能最高提升 3.6 倍。

## 一句话总结

> SSD 本来就保证 flash page 级原子写；把不超过 AWUPF 的映射更新从日志里改为直写，就省掉了 journal 的重复写。

## 研究背景与问题

- **SSD 的原子性被闲置**：page 是 flash 的最小写单位，FTL 更新映射后写才对主机可见，因此 SSD 天然具备页级原子写；NVMe 把它标准化为 AWUPF（按命名空间为 NAWUPF），掉电后读回的是全旧或全新数据，不会是新旧混合。作者查询手中的盘后发现多数提供 4 KB，个别为 512B，还有一个 NAWUPF 达 256KB 的特例；实验所用 SSD（WD Ultrastar DC ZN540）为 4 KB。
- **主机侧仍要双写**：文件系统与 DBMS 用 journaling 或 WAL 保证崩溃一致性，同一份数据先写日志再写实际位置，带来性能损失与写放大。
- **已有利用方式要改设备**：X-FTL 在 FTL 内做事务化的页映射表并扩展 SATA 接口，CFS 则依赖这种事务写接口，二者都要求修改 FTL 或引入新的主机接口。
- **Log-RAID 是最合适的落点**：条带的物理位置随每次更新变化，映射元数据必须写日志才能防住部分更新；而映射更新通常落在小的连续区域，容易塞进 AWUPF 的尺寸。

## 核心贡献

- **不改设备地复用 AWUPF**：只调整主机侧软件栈，把一串写的原子性负担交给 SSD，既不需要改 FTL，也不需要新的主机接口。
- **双路径更新策略**：修改后的元数据不超过 AWUPF 时直接更新 RAID 元数据，超过时退回传统 journaling，最坏情况下性能不劣于原方案。
- **两条路径的顺序处理**：分析同一个 mpage 既被 journal 更新又被直写更新时崩溃恢复可能出现的异常，并给出相应的顺序保证。
- **在 Poseidon OS 上落地**：在开源 AFA 存储栈中实现，用 FIO 与 Filebench 在顺序写、随机写与多种请求大小下评估。

## 方法与技术要点

- **Log-RAID 的元数据结构**：Poseidon OS 把阵列分为元数据分区（RAID-10，含 journal 区与映射区）和数据分区，元数据以 4 KB 的 mpage 为单位写入；映射分两级，第一级是虚拟条带地址（VSID 加偏移）的 VSA map，第二级是逻辑条带地址（LSID 加偏移）的 stripe map。
- **粒度换算**：VSA map 的一项对应虚拟盘的一个 4 KB 逻辑块，因此一个 mpage 覆盖约 2 MB 的虚拟盘空间；一次写只要改动的项落在一个 mpage 内且不超过 4 KB，就具备直写条件。
- **直写路径**：满足条件的写不再提交 journal，而是直接把 mpage 写到元数据区，由 AWUPF 保证掉电后读到的是全旧或全新版本。
- **顺序约束**：同一个 mpage 可能先被 journal 路径改、再被直写路径改（或顺序相反），崩溃恢复时两个版本会打架；方案据此约束两条路径的提交与恢复顺序（见第 3.2 节）。
- **只对 VSA map 用 AWUPF**：stripe map 只在条带写满时更新、频率低、对日志开销影响小；而且单条写命令无法同时更新 VSA map 与 stripe map，所以直写只用于 VSA map。

## 评估与主要结果

- **平台与负载**：在 Poseidon OS 上实现，用 FIO 的多种请求大小与读写模式，以及 Filebench 的 varmail、fileserver、OLTP、tpcso 评估，文件池预分配约 100 GB。
- **总体**：在 Poseidon OS 上，随机写性能最高提升 3.6 倍。
- **Filebench 细分**：OLTP 从 16 线程的 21% 提升到 32 线程的 73%；varmail 在 32 线程下比 journaling 高 14%，纯直写基线则高 31%；fileserver 因大于 512 KB 的请求占请求数 45%、占写流量 94%，两条路径差距不明显。
- **边界行为**：请求越大 checkpoint 开销被摊得越薄，2 MB 写时直写占比高、性能接近纯直写；若所有请求都超过 AWUPF，性能仍不劣于传统方案。

[返回 Security, Integrity, and Consistency](index.md) · [返回 FAST 2025](../index.md)
