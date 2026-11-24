# FDP-Rocks: An Effective Use Case of FDP in RocksDB

**中文标题**：FDP-Rocks：FDP 在 RocksDB 中的一个有效用例

**所属 Session**：[Session 6: Storage and File Systems](index.md) · [ATC 2026](../index.md)

**作者**：Jian Zhou (The University of Texas at Arlington), Inho Song (Virginia Tech), Chen Zhong (The University of texas at arlington), Peiran Du (The University of Texas at Arlington), Lingfeng Xiang (The University of Texas at Arlington), Sam H. Noh (Virginia Tech), Wenguang Wang (Broadcom Inc.), Jia Rao (The University of Texas at Arlington), Song Jiang (The University of Texas at Arlington)

## 英文摘要
While Flexible Data Placement (FDP) presents a promising opportunity to reduce device-level write amplification (DLWA) in SSDs, using this feature effectively remains challenging. A major obstacle is that the effectiveness of FDP still relies on accurate data lifetime characterization. As RocksDB is a dominant data management system powering many data center services and already provides built-in FDP support, it serves as an ideal case study. In this work, we demonstrate that RocksDB’s native level-based file placement, an intuitive and seemingly unmistakable design choice, ironically leads to unexpected data misplacement and is ineffective at reducing DLWA. To address this, we present FDP-Rocks, a system designed for effective FDP use in RocksDB by leveraging ML-model-based file lifetime classification and a custom SSTable compaction candidate selection policy to unlock the full potential of FDP. We implement FDP-Rocks in RocksDB. Experiments on diverse workloads demonstrate that FDP-Rocks can improve overall throughput by up to 37% and reduce DLWA by up to 43% over RocksDB with FDP enabled.

## 中文摘要
尽管灵活数据放置（Flexible Data Placement，FDP）为降低 SSD 中的设备级写放大（DLWA）提供了有前景的机会，但有效利用这一特性仍然充满挑战。一个主要障碍在于，FDP 的效果仍依赖于准确的数据生命周期刻画。由于 RocksDB 是支撑众多数据中心服务的主流数据管理系统，并且已经内置了 FDP 支持，因此它成为理想的研究案例。本工作表明，RocksDB 原生的基于层级的文件放置这一直观且看似不会出错的设计选择，讽刺性地导致了意外的数据错置，并且在降低 DLWA 上并不有效。为解决这一问题，我们提出 FDP-Rocks，一个通过基于机器学习模型的文件生命周期分类以及定制的 SSTable 压缩候选选择策略来释放 FDP 全部潜力的系统，以便在 RocksDB 中有效使用 FDP。我们在 RocksDB 中实现了 FDP-Rocks。在多样工作负载上的实验表明，与启用 FDP 的 RocksDB 相比，FDP-Rocks 可将整体吞吐最多提升 37%，并将 DLWA 最多降低 43%。

## 英文关键词
RocksDB, Flexible Data Placement, Write Amplification

## 中文关键词
RocksDB，灵活数据放置，写放大

[返回 Session 6](index.md) · [返回 ATC 2026](../index.md)
