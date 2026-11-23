---
title: "AIM: Software and Hardware Co-design for Architecture-level IR-drop Mitigation in High-performance PIM"
description: "ISCA 2025 · Session 5C · AIM: 高性能PIM中架构级IR降压缓解的软硬件协同设计"
tags:
  - "ISCA2025"
  - "Session 5C"
  - "Processing-in-Memory"
---

# AIM: Software and Hardware Co-design for Architecture-level IR-drop Mitigation in High-performance PIM

**中文标题：** AIM: 高性能PIM中架构级IR降压缓解的软硬件协同设计

**所属 Session：** [Session 5C](index.md) · [ISCA 2025](../index.md)

**作者：** Yuanpeng Zhang, Xing Hu, Xi Chen, Zhihang Yuan, Cong Li, Jingchen Zhu, Zhao Wang, Chenguang Zhang, Xin Si, Wei Gao, Qiang Wu, Runsheng Wang, Guangyu Sun

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730987) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

SRAM Processing-in-Memory (PIM) has emerged as the most promis- ing implementation for high-performance PIM, delivering supe- rior computing density, energy efficiency, and computational pre- cision. However, the pursuit of higher performance necessitates more complex circuit designs and increased operating frequencies, which exacerbate IR-drop issues. Severe IR-drop can significantly degrade chip performance and even threaten reliability. Conven- tional circuit-level IR-drop mitigation methods, such as back-end optimizations, are resource-intensive and often compromise power, performance, and area (PPA). To address these challenges, we pro- pose AIM, comprehensive software and hardware co-design for architecture-level IR-drop mitigation in high-performance PIM. Initially, leveraging the bit-serial and in-situ dataflow processing properties of PIM, we introduce Rtog and HR, which establish a direct correlation between PIM workloads and IR-drop. Building on this foundation, we propose LHR and WDS, enabling extensive exploration of architecture-level IR-drop mitigation while main- taining computational accuracy through software optimization. Subsequently, we develop IR-Booster, a dynamic adjustment mech- anism that integrates software-level HR information with hardware- based IR-drop monitoring to adapt the V-f pairs of the PIM macro, achieving enhanced energy efficiency and performance. Finally, we propose the HR-aware task mapping method, bridging software and hardware designs to achieve optimal improvement. Post-layout simulation results on a 7nm 256-TOPS PIM chip demonstrate that AIM achieves up to 69.2% IR-drop mitigation, resulting in 2.29× energy efficiency improvement and 1.152×speedup.

## 中文摘要

SRAM 存内计算（PIM）是高性能存内计算最有前景的实现方案，具备出色的计算密度、能效与计算精度。但为追求更高性能，电路设计愈发复杂、工作频率提升，进而加剧电压降（IR-drop）问题。严重的电压降会大幅降低芯片性能，甚至威胁可靠性。传统电路级电压降缓解手段（例如后端布线优化）资源开销大，往往会损害功耗、性能、面积（PPA）指标。

针对上述难题，本文提出 AIM，一套完备的软硬件协同设计方案，在架构层面缓解高性能存内计算中的电压降问题。首先，利用存内计算的位串行、原位数据流处理特性，提出 Rtog 和 HR，建立存内计算负载与电压降之间的直接关联。在此基础上，提出 LHR 和 WDS，借助软件优化，在保证计算精度的前提下，开展架构层面电压降缓解方案的广泛探索。
然后，本文设计 IR-Booster，一种动态调节机制：融合软件侧HR信息与硬件电压降监测，自适应调整PIM宏单元的电压-频率（V-f）组合，进一步提升能效与性能。最后，提出感知HR的任务映射策略，打通软硬件设计，实现最优收益。
基于7nm工艺、256 TOPS PIM芯片的版图后仿真表明：AIM最多将电压降削弱69.2%，能效提升2.29倍，性能提升1.152倍。

## 英文关键词

Processing-in-memory, IR-drop mitigation, Architecture-level optimization, Software and hardware co-design

## 中文关键词

存内计算, 电压降缓解, 架构级优化, 软硬件协同设计

## 代码与研究制品

- [代码仓库](https://github.com/pku-zyp/LHR-of-AIM-in-ISCA25)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730987)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2025](../index.md)
