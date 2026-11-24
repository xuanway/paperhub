# REFlash: Reducing Total Endurance Cost in Flash-Based Tiering via Cross-Tier Write Balancing

**中文标题**：REFlash：通过跨层写平衡降低基于闪存的分层存储总耐久性成本

**所属 Session**：[Session 6: Storage and File Systems](index.md) · [ATC 2026](../index.md)

**作者**：Sejun Kwon (Samsung Electronics and Seoul National University), Minwook Kim (Seoul National University), Jin-Soo Kim (Seoul National University)

## 英文摘要
QLC SSDs offer high density and low cost per byte, but their limited write endurance remains a critical barrier to widespread deployment. Flash-based tiering mitigates this limitation by placing a higher-endurance SSD as a buffer tier in front of a QLC capacity tier. However, existing schemes fail to jointly optimize write-induced wear across tiers: in-place-update schemes incur high device-level write amplification, while log-structured schemes leave the trade-off between buffer-tier garbage collection (GC) and capacity-tier flush writes unoptimized. This paper presents REFlash, a cost-aware log-structured buffering scheme for SSD-SSD tiered storage. REFlash introduces Total Endurance Cost (TEC), a unified metric that captures the asymmetric replacement cost across the buffer and capacity tiers, and uses it to dynamically choose between host-level GC and flush during segment reclamation. REFlash further reduces GC overhead by exploiting the bounded lifetime of buffered data. Implemented as a block device driver on an FDP-enabled TLC SSD and a QLC SSD, REFlash reduces TEC by up to 31% over existing log-structured tiering schemes while maintaining write throughput comparable to the best-performing baseline.

## 中文摘要
QLC SSD 提供了高密度和低每字节成本，但其有限的写入耐久性仍是其被广泛部署的关键障碍。基于闪存的分层存储通过在 QLC 容量层之前放置一块耐久性更高的 SSD 作为缓冲层来缓解这一限制。然而，现有方案未能联合优化各层之间由写操作引起的磨损：原地更新（in-place-update）方案会带来较高的设备级写放大，而日志结构（log-structured）方案则使缓冲层垃圾回收（GC）与容量层刷写（flush）写入之间的权衡得不到优化。本文提出 REFlash，一个面向 SSD–SSD 分层存储的成本感知日志结构缓冲方案。REFlash 引入总耐久性成本（Total Endurance Cost，TEC）这一统一指标，用于刻画缓冲层与容量层之间不对称的替换成本，并用它在段回收时在主机级 GC 与刷写之间动态选择。REFlash 还利用缓冲数据有限的存活时间进一步降低 GC 开销。REFlash 作为块设备驱动实现在一块支持 FDP 的 TLC SSD 和一块 QLC SSD 上，与现有日志结构分层方案相比，它将 TEC 最多降低 31%，同时保持与表现最好的基线相当的写吞吐。

## 英文关键词
flash-based tiering, SSD endurance, write amplification

## 中文关键词
基于闪存的分层存储，SSD 耐久性，写放大

[返回 Session 6](index.md) · [返回 ATC 2026](../index.md)
