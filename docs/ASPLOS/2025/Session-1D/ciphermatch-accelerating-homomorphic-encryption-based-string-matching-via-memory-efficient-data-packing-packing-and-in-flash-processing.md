---
title: "CIPHERMATCH: Accelerating Homomorphic Encryption-Based String Matching via Memory-Efficient Data Packing Packing and In-Flash Processing"
description: "ASPLOS 2025 · Session 1D · CIPHERMATCH：通过内存高效数据打包与闪存内处理加速基于同态加密的字符串匹配"
tags:
  - "ASPLOS2025"
  - "Session 1D"
  - "Homomorphic Encryption"
---

# CIPHERMATCH: Accelerating Homomorphic Encryption-Based String Matching via Memory-Efficient Data Packing Packing and In-Flash Processing

**中文标题：** CIPHERMATCH：通过内存高效数据打包与闪存内处理加速基于同态加密的字符串匹配

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Mayank Kabra (ETH Zurich), Rakesh Nadig (ETH Zurich), Harshita Gupta (ETH Zurich), Manos Frouzakis (ETH Zurich), Rahul Bera (ETH Zurich), Vamanan Arulchelvan (ETH Zurich), Yu Liang (ETH Zurich), Haiyu Mao (ETH Zurich), Mohammad Sadrosadati (ETH Zurich), Onur Mutlu (ETH Zurich)

**单位：** ETH Zurich

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716251) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Homomorphic encryption (HE) allows secure computation on encrypted data without revealing the original data, providing significant benefits for privacy-sensitive applications. Many cloud computing applications (e.g., DNA read mapping, biometric matching, web search) use exact string matching as a key operation. However, prior string matching algorithms that use homomorphic encryption are limited by high computational latency caused by the use of complex operations and data movement bottlenecks due to the large encrypted data size. In this work, we provide an efficient algorithm-hardware codesign to accelerate HE-based secure exact string matching. We propose CIPHERMATCH, which (i) reduces the increase in memory footprint after encryption using an optimized software-based data packing scheme, (ii) eliminates the use of costly homomorphic operations (e.g., multiplication and rotation), and (iii) reduces data movement by designing a new in-flash processing (IFP) architecture. CIPHERMATCH improves the software-based data packing scheme of an existing HE scheme and performs secure string matching using only homomorphic addition. This packing method reduces the memory footprint after encryption and improves the performance of the algorithm. To reduce the data movement overhead, we design an IFP architecture to accelerate homomorphic addition by leveraging the array-level and bit-level parallelism of NANDflash-based solid-state drives (SSDs). We demonstrate the benefits of CIPHERMATCH using two case studies: (1) Exact DNA string matching and (2) encrypted database search. Our pure software-based CIPHERMATCH implementation that uses our memory-efficient data packing scheme improves performance and reduces energy consumption by 42.9× and 17.6×, respectively, compared to the state-of-the-art software baseline. Integrating CIPHERMATCH with IFP improves performance and reduces energy consumption by 136.9× and 256.4×, respectively, compared to the software-based CIPHERMATCH implementation.

## 中文摘要

同态加密（HE）允许在加密数据上进行安全计算而不暴露原始数据，为隐私敏感型应用带来了显著收益。许多云计算应用（例如 DNA 读段比对、生物特征匹配、网络搜索）都将精确字符串匹配作为关键操作。然而，已有的使用同态加密的字符串匹配算法受限于两方面：一是使用复杂操作所导致的高计算延迟，二是加密数据规模庞大所造成的数据移动瓶颈。在本工作中，我们提出一种高效的算法—硬件协同设计，用于加速基于 HE 的安全精确字符串匹配。我们提出 CIPHERMATCH，它 (i) 使用优化的软件数据打包方案，降低加密后内存占用的增长；(ii) 消除代价高昂的同态操作（例如乘法与旋转）的使用；(iii) 通过设计一种新的闪存内处理（IFP）架构来减少数据移动。CIPHERMATCH 改进了现有 HE 方案的软件数据打包方案，并仅使用同态加法完成安全字符串匹配。该打包方法降低了加密后的内存占用，并提升了算法性能。为降低数据移动开销，我们设计了一种 IFP 架构，利用基于 NAND 闪存的固态硬盘（SSD）的阵列级与位级并行性来加速同态加法。我们通过两个案例研究展示了 CIPHERMATCH 的收益：(1) 精确 DNA 字符串匹配；(2) 加密数据库搜索。与最先进的软件基线相比，采用我们内存高效数据打包方案的纯软件 CIPHERMATCH 实现将性能提升 42.9×、将能耗降低 17.6×。与基于软件的 CIPHERMATCH 实现相比，将 CIPHERMATCH 与 IFP 集成后可将性能提升 136.9×、将能耗降低 256.4×。

## 英文关键词

Homomorphic Encryption, Secure String Matching, Storage Systems, Near-Data Processing

## 中文关键词

同态加密；安全字符串匹配；存储系统；近数据处理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716251)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2025](../index.md)
