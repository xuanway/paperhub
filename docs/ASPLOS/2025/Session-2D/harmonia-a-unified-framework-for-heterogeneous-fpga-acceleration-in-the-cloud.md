---
title: "Harmonia: A Unified Framework for Heterogeneous FPGA Acceleration in the Cloud"
description: "ASPLOS 2025 · Session 2D · Harmonia：面向云中异构 FPGA 加速的统一框架"
tags:
  - "ASPLOS2025"
  - "Session 2D"
  - "FPGAs"
---

# Harmonia: A Unified Framework for Heterogeneous FPGA Acceleration in the Cloud

**中文标题：** Harmonia：面向云中异构 FPGA 加速的统一框架

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Luyang Li (Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Heng Pan (Computer Network Information Center, Chinese Academy of Sciences), Xinchen Wan (Hong Kong University of Science and Technology), Kai Lv (Institute of Computing Technology, Chinese Academy of Sciences), Zilong Wang (Hong Kong University of Science and Technology), Qian Zhao (Douyin Co., Ltd.), Feng Ning (Douyin Co., Ltd.), Qingsong Ning (Douyin Co., Ltd.), Shideng Zhang (Douyin Co., Ltd.), Zhenyu Li (Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Layong Luo (Researcher), Gaogang Xie (Computer Network Information Center, Chinese Academy of Sciences,University of Chinese Academy of Sciences)

**单位：** Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences；Computer Network Information Center, Chinese Academy of Sciences；Hong Kong University of Science and Technology；Institute of Computing Technology, Chinese Academy of Sciences；Douyin Co., Ltd.；Researcher；Computer Network Information Center, Chinese Academy of Sciences,University of Chinese Academy of Sciences

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716259) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

FPGAs are gaining popularity in the cloud as accelerators for various applications. To make FPGAs more accessible for users and streamline system management, cloud providers have widely adopted the shell-role architecture on their ho- mogeneous FPGA servers. However, the increasing hetero- geneity of cloud FPGAs poses new challenges for this ar- chitecture. Previous studies either focus on homogeneous FPGAs or only partially address the portability issues for roles, while still requiring laborious shell development for providers and ad-hoc software modifications for users. This paper presents Harmonia, a unified framework for heterogeneous FPGA acceleration in the cloud. Harmonia op- erates on two layers: a platform-specific layer that abstracts hardware differences and a platform-independent layer that provides a unified shell for diverse roles and host software. In detail, Harmonia provides automated platform adapters and lightweight interface wrappers to manage hardware differences. Next, it builds a modularized shell composed of Reusable Building Blocks and employs hierarchical tai- loring to provide a resource-efficient and easy-to-use shell for different roles. Finally, it presents a command-based in- terface to minimize software modifications across distinct platforms. Harmonia has been deployed in a large service provider, Douyin, for several years. It reduces shell develop- ment workloads by 69%-93% and simplifies role and software configurations with negligible overhead (<0.63%). Compared with other frameworks, Harmonia supports cross-vendor FPGAs, reduces resource consumption by 3.5%-14.9% and simplifies software configurations by 15-23× while maintain- ing comparable performance.

## 中文摘要

FPGA 作为各类应用的加速器在云中日益受到欢迎。为了让用户更易使用 FPGA 并简化系统管理，云厂商已在同构 FPGA 服务器上广泛采用 shell-role 架构。然而，云 FPGA 日益增强的异构性给该架构带来了新的挑战。已有研究要么只关注同构 FPGA，要么仅部分解决了 role 的可移植性问题，同时仍然需要厂商进行繁重的 shell 开发、用户进行临时性的软件修改。本文提出 Harmonia，一个面向云中异构 FPGA 加速的统一框架。Harmonia 在两个层次上运作：抽象硬件差异的平台相关层，以及为多样化 role 与主机软件提供统一 shell 的平台无关层。具体而言，Harmonia 提供自动化的平台适配器和轻量级接口封装来管理硬件差异。接着，它构建由可复用构建块（Reusable Building Blocks）组成的模块化 shell，并采用分层裁剪（hierarchical tailoring）为不同 role 提供资源高效且易用的 shell。最后，它提出基于命令的接口，以最小化不同平台之间的软件修改。Harmonia 已在大型服务提供商抖音（Douyin）部署数年。它将 shell 开发工作量减少 69%-93%，并以可忽略的开销（<0.63%）简化 role 与软件配置。与其他框架相比，Harmonia 支持跨厂商 FPGA，将资源消耗降低 3.5%-14.9%，并将软件配置简化 15-23×，同时保持相当的性能。

## 英文关键词

Heterogeneous FPGA; Shell-Role Architecture; Cloud Framework; Reusability

## 中文关键词

异构 FPGA；Shell-Role 架构；云框架；可复用性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716259)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2025](../index.md)
