---
title: "Folded Banks: 3D-Stacked HBM Design for Fine-Grained Random-Access Bandwidth"
description: "ISCA 2025 · Session 9C · Folded Banks: 面向细粒度随机访问带宽的3D堆叠HBM设计"
tags:
  - "ISCA2025"
  - "Session 9C"
  - "Memory Technology"
---

# Folded Banks: 3D-Stacked HBM Design for Fine-Grained Random-Access Bandwidth

**中文标题：** Folded Banks: 面向细粒度随机访问带宽的3D堆叠HBM设计

**所属 Session：** [Session 9C](index.md) · [ISCA 2025](../index.md)

**作者：** Vignesh Adhinarayanan, Brad Beckmann, Wantong Li, Mohammad Seyedzadeh, Sergey Blagodurov, Derrick Aguren, Hayden Hyungdong Lee

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731111) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Despite significant improvements in peak bandwidth, the HBM in- dustry has neglected random-access (irregular) bandwidth, limiting performance in many real-world applications. Improving effective HBM bandwidth is challenging due to power-constrained activa- tions and coarse-grained, long-distance data movement. Rather than addressing these issues directly, hardware vendors have opted for incremental changes, achieving a 6.4×increase in sequential access bandwidth over two generations while leaving the irregular bandwidth challenges unresolved. To remedy this, we introduce Folded Banks (FB-HBM), a novel 3D bank design that redistributes bank subarrays (“folds”) across multiple dies and relocates command, control, and global sense amplifiers to an additional base layer. By implementing this logic in a new base layer, we eliminate the DRAM die overheads inherent in previous designs. This architecture enables vertical routing of intra-bank wires—column select lines (CSLs) and master data lines (MDLs)—through thin-pitch through-silicon vias (TSVs) and hy- brid bonds, significantly reducing RC power losses. By employing self-timed sense amplifiers, we eliminate costly dummy subarrays previously required for reference voltages. Furthermore, our dis- tributed TSV architecture minimizes inter-bank data movement and we reduce HBM row size and activation energy by selectively disabling memory arrays (MATs) within a bank. Compared to a projected HBM4 design, FB-HBM achieves a 6.7× improvement in random-access performance with a conservative 5 µm TSV pitch. This architectural advantage translates to a 2.28× speedup across high-performance computing (HPC) and sparse machine learning applications.

## 中文摘要

尽管峰值带宽持续提升，但HBM行业长期忽视随机（不规则访问）带宽，导致大量真实应用的性能受限。受功耗约束的存储激活、粗粒度且长距离的数据搬运，使得提升HBM有效带宽难度很高。硬件厂商并未从根源解决该问题，只做渐进式改良：两代产品间顺序访问带宽提升6.4倍，但不规则访问带宽的瓶颈依旧存在。

为解决该问题，本文提出**折叠存储体FB-HBM（Folded Banks）**，一种全新的3D存储体架构：将存储体子阵列（“折叠段”）分布在多个裸片上，并把命令、控制电路与全局灵敏放大器移至额外的底层基片。将这部分逻辑放到新增基片后，可以消除以往方案中DRAM裸片上的电路开销。
该架构借助窄间距硅通孔（TSV）与混合键合，实现存储体内部信号线——列选线（CSL）、主数据线（MDL）的垂直走线，大幅降低RC功耗损耗。同时采用自定时灵敏放大器，不再需要为生成参考电压而设置开销巨大的虚拟子阵列。此外，分布式TSV架构可以减少存储体之间的数据迁移；通过选择性关闭存储体内的存储阵列（MAT），FB-HBM还能减小HBM行粒度、降低激活能耗。对标预测版HBM4设计，在保守的5 µm TSV间距条件下，FB-HBM随机访问性能提升6.7倍；在高性能计算（HPC）与稀疏机器学习负载上，整体性能平均提速2.28倍。

## 英文关键词

HBM, 3D-stacked memory, random access, memory bandwidth

## 中文关键词

三维堆叠 HBM, 随机访问带宽, 混合键合

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731111)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9C](index.md) · [返回 ISCA 2025](../index.md)
