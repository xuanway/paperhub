---
title: "PuDGhost: Experimental Analysis of Computation Result Corruption in Processing-using-DRAM Operations on Real DRAM Chips and Implications for Future Systems"
description: "ISCA 2026 · Session 3B · PuDGhost: Experimental Analysis of Computation Result Corruption in Processing-using-DRAM Operations on Real DRAM Chips and Implications for Future Systems"
tags:
  - "ISCA2026"
  - "Session 3B"
  - "DRAM and SRAM PIM/PNM"
---

# PuDGhost: Experimental Analysis of Computation Result Corruption in Processing-using-DRAM Operations on Real DRAM Chips and Implications for Future Systems

**中文标题：** PuDGhost: 真实 DRAM 芯片上使用 DRAM 计算的操作结果损坏实验分析及对未来系统的启示

**所属 Session：** [Session 3B](index.md) · [ISCA 2026](../index.md)

**作者：** Daichi Tokuda, İsmail Emir Yüksel, Tatsuya Kubo, Ataberk Olgun, Haocong Luo, Nisa Bostanci, Jikun Wang, A. Giray Yağlıkçı, Shinya Takamaeda-Yamazaki, Onur Mutlu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Processing-using-DRAM (PuD) is a promising computation paradigm to alleviate the frequent data movement between main memory and processing units. The PuD paradigm provides a substrate for highly parallel computation by using each DRAM column as a computation engine via simultaneous multiple-row activation (SiMRA). Unfortunately, DRAM density scaling might hinder PuD’s benefits. This is because denser cell arrays bring rows and columns closer, making even regular DRAM operations susceptible to noise and interference from neighboring cells. PuD repurposes DRAM from a storage device into a parallel computing substrate, yet no prior work investigates whether interference from rows or columns that are not intended to participate in the computation can compromise PuD robustness. In this work, we reveal an interference phenomenon affecting PuD computations, which we call PuDGhost, where a PuD operation in a given column produces erroneous results due to interference from 1) data stored in non-activated DRAM rows and 2) data stored in other columns that perform computations concurrently under the same SiMRA operation. PuDGhost violates the ideal picture of PuD computations, where each column’s computation should depend solely on its own operand data. Thus, PuDGhost threatens the robustness of future PuD systems. We present the first extensive characterization of PuDGhost using 96 real DDR4 DRAM chips from 12 modules, systematically quantifying the impact of these two interference sources under various conditions (i.e., data patterns, temperature, and spatial properties). Among our 15 new empirical observations, we highlight two major results: 1) data in physically adjacent non-activated rows affects SiMRA outputs by up to 10% for random inputs, and 2) data in columns that perform computations concurrently affects SiMRA outputs by up to 48% for random inputs. Guided by these findings, we propose countermeasures against PuDGhost across multiple layers of the PuD computing stack (i.e., microarchitectural, architectural, and system levels). Specifically, we propose and evaluate on real DDR4 DRAM chips: 1) robust column screening that reduces the risk of mistakenly using unreliable columns in the presence of PuDGhost, and 2) a compute row layout that mitigates PuDGhost via dedicated rows between compute rows. Our solutions greatly improve PuD computation accuracy. We hope that our findings provide a foundation for developing solutions to enable future PuD systems that are robust.

## 中文摘要

使用DRAM进行计算（PuD）是一种有前景的计算范式，旨在减轻主存与处理单元之间频繁的数据移动。PuD范式通过同时多行激活（SiMRA）将每个DRAM列用作计算引擎，为高度并行的计算提供了底层平台。不幸的是，DRAM密度缩放可能会阻碍PuD的收益，因为更密集的单元阵列使行和列排布更近，使得即使是常规DRAM操作也容易受到相邻单元的噪声和干扰。PuD将DRAM从存储设备重新定位为并行计算底层平台，然而之前没有工作研究过不参与计算的行或列的干扰是否会损害PuD的鲁棒性。在本工作中，我们揭示了一种影响PuD计算的干扰现象，称之为PuDGhost，其中给定列中的PuD操作会因以下两种干扰而产生错误结果：1) 存储在未激活DRAM行的数据；2) 在同一SiMRA操作下同时执行计算的其他列中存储的数据。PuDGhost违反了PuD计算的理想图景——每个列的计算应仅依赖于其自身的操作数数据。因此，PuDGhost威胁了未来PuD系统的鲁棒性。我们使用来自12个模块的96个真实DDR4 DRAM芯片，首次对PuDGhost进行了广泛表征，系统性地量化了这两种干扰源在各种条件下（数据模式、温度、空间特性）的影响。在我们的15项新经验观察中，我们强调两个主要结果：1) 物理相邻的未激活行中的数据对随机输入的SiMRA输出影响高达10%；2) 同时执行计算的其他列中的数据对随机输入的SiMRA输出影响高达48%。基于这些发现，我们在PuD计算堆栈的多个层次（即微架构层、架构层和系统层）上提出了针对PuDGhost的对策。具体来说，我们在真实DDR4 DRAM芯片上提出并评估了：1) 鲁棒列筛选，降低在PuDGhost存在下错误使用不可靠列的风险；2) 一种计算行布局，通过计算行之间的专用行来缓解PuDGhost。我们的解决方案极大地提高了PuD计算的准确性。我们希望我们的发现为开发解决方案以构建未来鲁棒的PuD系统奠定基础。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2026](../index.md)
