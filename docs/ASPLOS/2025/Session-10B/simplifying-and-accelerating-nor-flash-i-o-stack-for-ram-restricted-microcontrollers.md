---
title: "Simplifying and Accelerating NOR Flash I/O Stack for RAM-Restricted Microcontrollers"
description: "ASPLOS 2025 · Session 10B · 面向 RAM 受限微控制器的 NOR Flash I/O 栈简化与加速"
tags:
  - "ASPLOS2025"
  - "Session 10B"
  - "Solid State Storage"
---

# Simplifying and Accelerating NOR Flash I/O Stack for RAM-Restricted Microcontrollers

**中文标题：** 面向 RAM 受限微控制器的 NOR Flash I/O 栈简化与加速

**所属 Session：** [Session 10B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Hao Huang (Harbin Institute of Technology, Shenzhen), Yanqi Pan (Harbin Institute of Technology, Shenzhen), Wen Xia (Harbin Institute of Technology, Shenzhen), Xiangyu Zou (Harbin Institute of Technology, Shenzhen), Darong Yang (Harbin Institute of Technology, Shenzhen), Liang Shi (East China Normal University), Hongwei Du (Harbin Institute of Technology, Shenzhen)

**单位：** Harbin Institute of Technology, Shenzhen；East China Normal University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716272) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

NOR flash has been increasingly popular for RAM-restricted microcontrollers due to its small package, high reliability, etc. To satisfy RAM restrictions, existing NOR flash file systems migrate their functionalities, i.e., block-level data organization and wear leveling (WL), from RAM to NOR flash. However, such fine-grained block-level management introduces frequent index updates and NOR flash scanning, leading to severe I/O amplification, which further deteriorates as they are decoupled in existing NOR flash file systems. To address the problem, we propose NF2FS, a NOR flashfriendly file system. Our key insight is that applications running on NOR flash usually have (1) small file sizes, therefore block-based data organization can be converted to flat file layout (for fast file/dir scanning); (2) deterministic I/O patterns, thereby WL can be achieved through coarse file swapping. As a result, NF2FS relaxes data organization and WL to a coarse-grained file level, which are then cooperated within the file system. We implement NF2FS in FreeRTOS using a range of techniques, including the all-logging layout, along with efficient layout management approaches such as dual bitmap space allocator and soft-update-like crash consistency. Experiments suggest that NF2FS significantly outperforms existing works and can prevent quick NOR flash wear-out.

## 中文摘要

NOR flash 因其小封装、高可靠性等特点，在 RAM 受限的微控制器中日益流行。为满足 RAM 限制，现有的 NOR flash 文件系统将其功能（即块级数据组织和磨损均衡（WL））从 RAM 迁移到 NOR flash。然而，这种细粒度的块级管理引入了频繁的索引更新和 NOR flash 扫描，导致严重的 I/O 放大，而由于这些功能在现有 NOR flash 文件系统中相互解耦，该问题进一步恶化。为解决该问题，我们提出了 NF2FS，一种对 NOR flash 友好的文件系统。我们的核心洞察是：运行在 NOR flash 上的应用通常具有（1）较小的文件尺寸，因此基于块的数据组织可以转换为扁平文件布局（用于快速的文件/目录扫描）；（2）确定性的 I/O 模式，因此 WL 可以通过粗粒度的文件交换来实现。由此，NF2FS 将数据组织和 WL 放宽到粗粒度的文件级别，并在文件系统内部对其加以协同。我们在 FreeRTOS 中使用一系列技术实现了 NF2FS，包括全日志布局，以及诸如双位图空间分配器和类 soft-update 崩溃一致性等高效的布局管理方法。实验表明，NF2FS 显著优于现有工作，并能防止 NOR flash 快速磨损。

## 英文关键词

NOR flash, embedded file system, I/O stack

## 中文关键词

NOR flash；嵌入式文件系统；I/O 栈

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716272)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10B](index.md) · [返回 ASPLOS 2025](../index.md)
