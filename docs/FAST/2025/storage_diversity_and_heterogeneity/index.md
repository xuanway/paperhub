---
title: "Storage Diversity and Heterogeneity · FAST 2025"
description: "FAST 2025 · Storage Diversity and Heterogeneity · 4 篇论文"
tags:
  - "FAST2025"
  - "Storage Diversity and Heterogeneity"
---

# Storage Diversity and Heterogeneity · FAST 2025

**中文主题**：存储多样性与异构性

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-27 10:50–12:10 · **Chair**：Avani Wildani（Cloudflare and Emory University）

这四篇论文面对同一类失配：存储介质与数据形态都不再齐整——图上的全距离草图放不进内存，PM、NVMe、SATA 混装在一台机器里，DNA 既要承接海量冷数据，又要像块设备一样被寻址和更新。四条路线分别是把数据搬出内存（Oasis）、把存储设备从金字塔改成平面（PolyStore）、把 DNA 合成与测序包装成可更新的块设备（LiqSD）、用生成模型直接设计 DNA 编码（Motif 生成工具），共同点是改系统抽象而非改介质。结果被压成具体倍数：13.8 倍内存节省、9.38 倍吞吐提升、2,927 倍写代价下降，说明异构不是可用性问题，而是可量化的设计取舍。

本 Session 共收录 **4** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| [Oasis: An Out-of-core Approximate Graph System via All-Distances Sketches](oasis_an_out_of_core_approximate_graph_system_via_all_distances_sketches.md) ([code](https://github.com/tsunyuyang/Oasis)) | Oasis：基于全距离草图的外存近似图系统 | ADS 的瓶颈不是精度而是内存：把草图放进外存、按内存预算分区构图，就能用 1.8 倍时间换 13.8 倍内存。 | [页面](https://www.usenix.org/conference/fast25/presentation/yang) · [PDF](https://www.usenix.org/system/files/fast25-yang.pdf) |
| [PolyStore: Exploiting Combined Capabilities of Heterogeneous Storage](polystore_exploiting_combined_capabilities_of_heterogeneous_storage.md) ([code](https://github.com/RutgersCSSystems/PolyStore)) | PolyStore：发挥异构存储的联合能力 | 把 PM、NVMe、SATA 摆成同一层而不是叠成金字塔，让多线程写也能同时吃满所有设备的合计带宽。 | [页面](https://www.usenix.org/conference/fast25/presentation/ren) · [PDF](https://www.usenix.org/system/files/fast25-ren.pdf) |
| [Liquid-State Drive: A Case for DNA Block Device for Enormous Data](liquid_state_drive_a_case_for_dna_block_device_for_enormous_data.md) | 液态驱动器：面向海量数据的 DNA 块设备探索 | DNA 块设备的难点不是合成速度，而是别让 PB 级元数据跟着每次写进 DNA：轻量翻译表放进 SSD，失效推迟到读。 | [页面](https://www.usenix.org/conference/fast25/presentation/zhou-jiahao) · [PDF](https://www.usenix.org/system/files/fast25-zhou-jiahao.pdf) |
| [DNA data storage: A generative tool for Motif-based DNA storage](dna_data_storage_a_generative_tool_for_motif_based_dna_storage.md) | DNA 数据存储：面向基序编码 DNA 存储的生成式工具 | 把 motif 设计写成逐碱基的奖励采样：越接近约束边界惩罚越重，于是键与载荷无论怎么拼接都合法。 | [页面](https://www.usenix.org/conference/fast25/presentation/brunmayr) · [PDF](https://www.usenix.org/system/files/fast25-brunmayr.pdf) |

[返回 FAST 2025](../index.md)
