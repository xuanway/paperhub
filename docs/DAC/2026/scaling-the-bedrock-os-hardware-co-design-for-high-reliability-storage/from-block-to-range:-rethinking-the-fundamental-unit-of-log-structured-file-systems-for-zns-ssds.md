From Block to Range: Rethinking the Fundamental Unit of Log-Structured File Systems for ZNS SSDs
Authors：
[Zhenhua Tan](https://63dac.conference-program.com/?post_type=page&p=15&uid=4152838259081271645)，[Kan Zhong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1683549744506293238)，[Zhiwang Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0606284309299502237)，[Haorui He](https://63dac.conference-program.com/?post_type=page&p=15&uid=90765274780057738161)，[Linbo Long](https://63dac.conference-program.com/?post_type=page&p=15&uid=2183558410454964151)，[Duo Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=764143)，[Jingcheng Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=36616647747263449281)

## 中文标题

从块到区间：面向 ZNS SSD 重新思考日志结构文件系统的基本单位

## 英文摘要

Log-structured file systems (LFSs) have shown promising potential on emerging Zoned Namespace (ZNS) SSDs. However, current ZNS-enabled LFSs still follow the block-based abstraction inherited from traditional SSDs. This abstraction enforces block-aligned writes and triggers costly read–modify–write operations for unaligned writes. Since ZNS SSDs natively support arbitrary-sized writes, such block alignment is unnecessary and instead results in significant performance degradation. To address this issue, we present RangeLFS, an LFS that replaces fixed-size blocks with flexible ranges to write directly arbitrary-sized file segments without alignment. First, we propose a range-based file structure, where each range directly maps an arbitrary-sized file segment to its device address. These ranges in a file are maintained in an enhanced B+ tree, enabling efficient lookups while reducing cascading address updates and structural modifications. Second, we propose a range-augmented page cache to support partial-page writes and perform range-based writeback, eliminating the traditional page-granularity constraint that would otherwise prevent arbitrary-sized writes. Evaluated on a production ZNS SSD, RangeLFS improves write bandwidth by up to 6.95× compared with block-based LFSs, while maintaining comparable read performance across diverse workloads.

## 中文摘要

日志结构文件系统（LFS）在新兴的分区命名空间（ZNS）SSD 上展现出良好前景。然而，当前支持 ZNS 的 LFS 仍沿用继承自传统 SSD 的块级抽象。该抽象强制按块对齐写，并对非对齐写触发代价高昂的读–改–写操作。由于 ZNS SSD 原生支持任意大小的写，这种块对齐既无必要，反而造成显著的性能下降。为解决该问题，我们提出 RangeLFS，一个以灵活区间取代固定大小块、可直接写入任意大小文件段而无需对齐的 LFS。首先，我们提出基于区间的文件结构，其中每个区间直接将任意大小的文件段映射到其设备地址。文件中的这些区间维护在一棵增强 B+ 树中，在实现高效查找的同时减少级联地址更新和结构修改。其次，我们提出区间增强的页缓存，支持部分页写并执行基于区间的回写，从而消除原本阻碍任意大小写的传统页粒度约束。在生产级 ZNS SSD 上的评估表明，RangeLFS 相比基于块的 LFS 将写带宽提升最高 6.95 倍，同时在多样工作负载下保持相当的读性能。

## 英文关键词

LFSs, ZNS Interface, SSDs

## 中文关键词

LFS、ZNS 接口、SSD
