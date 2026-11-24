---
title: "HaSiS: A Hardware-assisted Single-index Store for Hybrid Transactional and Analytical Processing"
description: "FAST 2025 · Hardware Assist · 以透明压缩 CSD 支撑单个 B+-树索引，让 HTAP 分析查询看到即时的交易更新"
tags:
  - "FAST2025"
  - "Hardware Assist"
  - "HTAP"
  - "computational storage drive"
---

# HaSiS: A Hardware-assisted Single-index Store for Hybrid Transactional and Analytical Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">HTAP 通常维护行式与列式两套索引并跨域迁移数据，分析新鲜度延迟达 20ms 到 8min，迁移还带来写放大。HaSiS 改用一个 B+-树，靠带透明压缩的计算存储盘支持 128KB 大页与页内稀疏列式打包，相同负载占用 71.2GB 而非 168.7GB。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Hardware Assist</p>
</div>

**中文标题**：HaSiS：面向混合事务与分析处理的硬件辅助单索引存储

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/huang](https://www.usenix.org/conference/fast25/presentation/huang)

**论文 PDF**：[fast25-huang.pdf](https://www.usenix.org/system/files/fast25-huang.pdf)

**作者**：Kecheng Huang（The Chinese University of Hong Kong）；Zhaoyan Shen（Shandong University）；Zili Shao（The Chinese University of Hong Kong）；Feng Chen（Indiana University Bloomington）；Tong Zhang（Rensselaer Polytechnic Institute and ScaleFlux Inc.）

**会议**：FAST 2025 · Santa Clara, CA · 第 305–320 页

**Session**：Hardware Assist · 2025-02-26 10:50–12:30 · Chair：Kiran Kumar Muniswamy Reddy（Amazon）

**所属 Session**：[Hardware Assist](index.md) · [FAST 2025](../index.md)

**关键词**：HTAP, computational storage drive, B+-tree, transparent compression, PAX page layout

---

## 英文摘要

Driven by the exploding demands for real-time data analytics, hybrid transactional and analytical processing (HTAP) has become a topic of great interest in academia and the database industry. To address the well-known conflict between optimal storage formats for online transactional processing (OLTP) and online analytical processing (OLAP), the conventional practice employs a mixture of at least two distinct index data structures (e.g., B+-tree and column-store) and dynamically migrates data across different index domains. Unfortunately, such a multi-index design is notably subject to non-trivial trade-offs among OLTP performance, OLAP performance, and OLAP data freshness. In contrast to prior work that centered around exploring the multi-index design space, this work advocates a single-index design for a paradigm shift towards much more effectively serving HTAP workloads. This is made possible by computational storage drives (CSDs) with built-in transparent compression that are emerging on the commercial market. The key is to exploit the fact that compression-capable CSDs enable data management software to purposefully employ sparsely filled storage data blocks without sacrificing physical storage capacity. Leveraging this unique feature, we have developed an HTAP-oriented B+-tree design that can effectively serve HTAP workloads and in the meantime can achieve almost instant OLAP data freshness. We have developed and open-sourced a fully functional prototype. Our results show that compared to the state-of-the-art solutions, such a CSD-assisted single-index design can ensure data freshness and deliver high performance for HTAP workloads.

## 中文摘要

在实时数据分析需求的爆炸式增长推动下，混合事务与分析处理（HTAP）已成为学术界与数据库产业高度关注的话题。为解决在线事务处理（OLTP）与在线分析处理（OLAP）各自最优存储格式之间众所周知的冲突，传统做法采用至少两种不同索引数据结构（例如 B+-树与列存）的混合，并在不同索引域之间动态迁移数据。遗憾的是，这种多索引设计在 OLTP 性能、OLAP 性能与 OLAP 数据新鲜度之间带来显著的取舍。与此前围绕多索引设计空间展开探索的工作不同，本文倡导单索引设计，以推动范式转变、更有效地服务 HTAP 负载。这一设计之所以可行，得益于商业市场上出现的、内置透明压缩的计算存储盘（CSD）。关键在于利用这样一个事实：具备压缩能力的 CSD 使数据管理软件能够有目的地使用稀疏填充的存储数据块，而不牺牲物理存储容量。借助这一独特特性，本文开发了一种面向 HTAP 的 B+-树设计，能够有效服务 HTAP 负载，同时实现几乎即时的 OLAP 数据新鲜度。本文开发并开源了一个功能完整的原型。结果表明，相比最先进的方案，这种 CSD 辅助的单索引设计能够保证数据新鲜度，并为 HTAP 负载提供高性能。

## 一句话总结

> 把和解行列格式冲突的任务交给压缩盘：故意留空的 4KB 逻辑块不花物理容量，于是一个大页 B+-树就能同时服务交易与分析。

## 研究背景与问题

- **格式冲突**：OLTP 是小事务高并发，偏爱元组连续存放的行式 B+-树；OLAP 是跨大表的列查询，偏爱列式存储。HTAP 要同时满足两者，还要保证 OLAP 数据新鲜度这一实时分析的关键指标。
- **多索引多存储的代价**：ByteHTAP、PolarDB-IMCI、VEGITO、BatchDB、TiDB 等靠日志搬运或 ETL 迁移数据，报告的新鲜度延迟从 20ms 到 8min；若让分析查询直接读行存，则要穿过多套索引结构，产生严重读放大。
- **多索引单存储的代价**：SAP HANA、Hyper、MemSQL 把行式 delta 层架在列式主存上，能做到即时新鲜度，但查询要同时访问两个数据源，索引与读放大叠加；其内存属性掩盖了问题，一旦数据集超出内存性能就明显退化。
- **单索引的物理障碍**：传统 B+-树写放大与页大小成正比，所以 OLTP 库用小页（Oracle、PostgreSQL 8KB，MySQL 16KB），这对 OLAP 极为不利；跨索引域迁移又是 I/O 密集型操作，写放大与前后台干扰随更新强度上升。

## 核心贡献

- **单索引 HTAP 设计**：只用一个 B+-树同时承载事务与分析访问，从根上消除跨索引域的数据迁移，从而取得几乎即时的 OLAP 数据新鲜度。
- **页大小与写放大解耦**：借助压缩盘的特性放宽写放大对页大小的依赖，使 B+-树可以采用远大于常规的页（如 128KB）而不显著牺牲 OLTP 性能。
- **页内稀疏列式打包**：在每个大页内部按 PAX 原则以列式存放元组，并利用压缩盘故意稀疏填充各列，压低列式访问的存储 I/O 读放大而不浪费物理容量。
- **每页聚簇的多版本记录**：同样借压缩盘按页存放并索引多版本记录，无需额外元数据或索引即可支持多版本并发控制，且不牺牲分析速度。

## 方法与技术要点

- **透明压缩 CSD 的底层机制**：控制器内的专用硬件引擎在 I/O 路径上对每个 4KB LBA 块做压缩与解压，FTL 负责把变长的压缩后块组织到闪存上，LPN 到 PPN 是 N 对一映射，主机 CPU 不参与压缩与变长块管理。
- **虚拟空间与稀疏填充**：压缩盘对外暴露远超物理容量的虚拟逻辑空间（如 32TB 虚拟对 4TB 物理），软件可以只写 1KB 真实数据、其余补零，从而在不消耗真实物理容量的前提下稀疏填充 4KB 逻辑块。
- **读放大建模**：页内列大小为 lc、读取该列需取 s 个连续的 4KB LBA 块时，读放大为 γ = s·4KB / lc；因此要么增大页内元组数（大页），要么让列布局按 4KB 边界对齐来减小 s。
- **大页与页内日志**：HaSiS 用大页承载更多元组，并在页内维护日志以暂存被 OLAP 查询阻塞的更新（delta pages）；全局日志按段组织，段大小可调，直接影响 OLTP 吞吐与崩溃恢复时要重放的日志量。
- **实现与开源**：基于商用 ScaleFlux CSD-3310 实现功能完整的原型并开源，页内多版本记录与列式打包均在既有 B+-树上叠加，不改变索引语义。

## 评估与主要结果

- **评测配置**：在商用透明压缩 CSD（ScaleFlux CSD-3310）上运行，对比最先进的 HTAP 数据库 TiDB、行存与列存两种基线实现，以及 MySQL、PostgreSQL、Parquet 等行/列存储；负载取自 TPC-C 与 TPC-H。
- **CSD 的必要性**：同一份 HaSiS 部署在 CSD-3310 与 1TB Western Digital SN570 NVMe SSD 上，TP 吞吐 139.6 与 139.4 KOPS、AP 响应时间 3.12 与 3.11 sec/op 基本持平，但空间占用为 71.2GB 对 168.7GB——没有透明压缩时稀疏管理的页内日志会吃掉两倍以上的物理空间。
- **更细粒度分区的收益**：分区变小后每次操作触及的分区更少，锁粒度更细，实测 OLTP 与 OLAP 的锁持有时长分别从 61.7µs/op 降到 3.14µs/op、从 2.31s/op 降到 1.12s/op。
- **全局日志段的权衡**：段大小从 50MB 增到 1,000MB 时，增至 100MB 使 OLTP 性能提升 91.2%，此后收益递减；OLAP 性能稳定（波动不超过 2.64%）；恢复时间随段增大从 4.1ms 升到 155.5ms。
- **最坏情况**：按 10:1 到 500:1 的 TP 重复比把 OLTP 更新插入 TPC-C 请求以制造热点区，被 OLAP 查询阻塞的更新退化为 delta pages；在 TPC-H 的 Q3 上 OLTP 与 OLAP 性能反而改善，Q5、Q10 趋势类似。

[返回 Hardware Assist](index.md) · [返回 FAST 2025](../index.md)
