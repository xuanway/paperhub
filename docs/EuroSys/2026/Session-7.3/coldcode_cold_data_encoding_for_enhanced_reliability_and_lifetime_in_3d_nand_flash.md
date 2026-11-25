---
title: "ColdCode: Cold Data Encoding for Enhanced Reliability and Lifetime in 3D NAND Flash"
description: "EuroSys 2026 · Storage Systems · Qiao Li (Mohamed bin Zayed University of Artificial Intelligence), Shangyu Wu (M"
tags:
  - "EuroSys2026"
  - "Storage Systems"
---

# ColdCode: Cold Data Encoding for Enhanced Reliability and Lifetime in 3D NAND Flash

**中文标题：** ColdCode：面向 3D NAND 闪存可靠性与寿命提升的冷数据编码

**所属 Session：** [Session 7.3: Storage Systems](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Storage Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Storage Systems</p>
</div>

**作者**：Qiao Li (Mohamed bin Zayed University of Artificial Intelligence), Shangyu Wu (Mohamed bin Zayed University of Artificial Intelligence), Zheng Wan (Xiamen University), Yufei Cui (McGill University), Jie Zhang (Peking University), Chun Jason Xue (Mohamed bin Zayed University of Artificial Intelligence)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769388)

## 英文摘要

Cold storage, which stores rarely accessed data, dominates modern data centers but is poorly served by NAND flash’s data randomization. As a common practice today by flash vendors, data randomization is applied in NAND flash chips to avoid extreme data patterns that generate the worst-case raw bit error rate (RBER). However, this paper demonstrates that data randomization rules out the opportunity to explore data patterns with very low RBERs, through a comprehensive analysis on data randomization in 3D NAND flash chips (across 8 models). Motivated by this, we propose ColdCode, a novel data coding framework to replace the conventional randomizer in 3D high-density flash for cold data storage. Using a tag that indicates coldness information passed from the file system to solid-state drive (SSD) controllers, the controller encodes cold data to enhance reliability and extend the lifetime. ColdCode employs two coding techniques: skewed coding and reversed Huffman coding, applied based on the data entropy. These techniques effectively reduce the RBER of encoded data compared to conventional randomization. Experimental results on real high-density 3D flash chips show that, under the same error conditions, the skewed coding and reversed Huffman coding reduce the average RBER by 42% and 30%, respectively. Consequently, the lifetime of the flash chips is prolonged by factors of 2.97× and 1.7×, respectively, compared to data randomization.

## 中文摘要

冷存储用于存放很少访问的数据，在现代数据中心中占据主导地位，但 NAND 闪存的数据随机化难以为其提供良好服务。作为闪存厂商目前的常见做法，NAND 闪存芯片中应用数据随机化以避免产生最差原始误码率（RBER）的极端数据模式。然而，本文通过对 3D NAND 闪存芯片（涵盖 8 种型号）中数据随机化的全面分析表明，数据随机化排除了探索具有极低 RBER 的数据模式的机会。受此启发，我们提出 ColdCode，一种新的数据编码框架，用于在面向冷数据存储的 3D 高密度闪存中替代传统随机化器。利用从文件系统传递到固态硬盘（SSD）控制器的表示冷度的标签，控制器对冷数据进行编码以增强可靠性并延长寿命。ColdCode 根据数据熵采用两种编码技术：偏斜编码和反向霍夫曼编码。与传统随机化相比，这些技术有效降低了编码数据的 RBER。在真实高密度 3D 闪存芯片上的实验结果表明，在相同错误条件下，偏斜编码和反向霍夫曼编码分别将平均 RBER 降低 42% 和 30%。因此，与数据随机化相比，闪存芯片的寿命分别延长 2.97× 和 1.7×。

**英文关键词：** Flash reliability, Randomization, Data coding, Cold storage

**中文关键词：** 闪存可靠性、随机化、数据编码、冷存储

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
