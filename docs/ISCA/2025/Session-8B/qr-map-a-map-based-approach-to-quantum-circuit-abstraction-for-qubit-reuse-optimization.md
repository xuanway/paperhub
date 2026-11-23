---
title: "QR-Map: A Map-Based Approach to Quantum Circuit Abstraction for Qubit Reuse Optimization"
description: "ISCA 2025 · Session 8B · QR-Map: 基于地图的量子电路抽象与量子比特复用优化"
tags:
  - "ISCA2025"
  - "Session 8B"
  - "Quantum III"
---

# QR-Map: A Map-Based Approach to Quantum Circuit Abstraction for Qubit Reuse Optimization

**中文标题：** QR-Map: 基于地图的量子电路抽象与量子比特复用优化

**所属 Session：** [Session 8B](index.md) · [ISCA 2025](../index.md)

**作者：** Hyungseok Kim, Enhyeok Jang, Seungwoo Choi, Youngmin Kim, Won Woo Ro

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731020) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Recent advances in quantum computing introduce the ability to reuse qubits through mid-circuit measurements, thereby enhanc- ing the efficiency of quantum devices with limited computational resources. However, identifying optimal reuse opportunities in quantum circuits remains challenging due to the intricate depen- dencies between quantum gates. Existing frameworks address this by either directly searching for reuse opportunities or converting circuits into directed acyclic graphs (DAGs). Unfortunately, these frameworks may require exponential search complexity or may not always ensure optimal results due to their non-deterministic property. To overcome these challenges, we propose QR-Map (Qubit Reuse Map), a map-based framework that abstracts computational Won Woo Ro Yonsei University Seoul, Republic of Korea [wro@yonsei.ac.kr](mailto:wro@yonsei.ac.kr) ACM Reference Format: Hyungseok Kim, Enhyeok Jang, Seungwoo Choi, Youngmin Kim, and Won Woo Ro. 2025. QR-Map: A Map-Based Approach to Quantum Circuit Ab- straction for Qubit Reuse Optimization. In Proceedings of the 52nd An- nual International Symposium on Computer Architecture (ISCA ’25), June 21–25, 2025, Tokyo, Japan. ACM, New York, NY, USA, 15 pages. https: //doi.org/10.1145/3695053.3731020 dependencies for efficient qubit reuse. By extracting and aligning two-qubit gates, QR-Map facilitates dependency detection and en- sures qubit savings without incurring excessive idle time. This approach achieves an optimal balance between gate serialization depth and crosstalk reduction. Evaluations with various quantum circuit benchmarks demonstrate that quantum circuits optimized with QR-Map achieve average reductions of 20% in qubit usage, 25% in circuit depth, and 22% in SWAP insertions compared to those optimized with the state-of-the-art framework.

## 中文摘要

量子计算的最新进展引入了通过电路中途测量重用量子比特的能力，从而提高了计算资源有限的量子设备的效率。然而，由于量子门之间复杂的依赖性，确定量子电路中的最佳重用机会仍然具有挑战性。现有框架通过直接搜索重用机会或将电路转换为有向无环图（DAG）来解决这个问题。不幸的是，这些框架可能需要指数级的搜索复杂性，或者由于其不确定性属性，可能无法始终确保最佳结果。为了克服这些挑战，我们提出了QR-Map（量子比特重用地图），这是一种基于地图的框架，它抽象了计算依赖性以实现高效的量子比特重用。通过提取和对齐双量子比特门，QR-Map 有助于依赖性检测并确保节省量子比特，而不会产生过多的空闲时间。

这种方法实现了门串行化深度和串扰减少之间的最佳平衡。对各种量子电路基准的评估表明，与使用最先进的框架优化的量子电路相比，使用 QR-Map 优化的量子电路的量子比特使用量平均减少 20%，电路深度平均减少 25%，SWAP 插入平均减少 22%。

## 英文关键词

quantum compiler, qubit reuse, quantum circuit optimization, mid-circuit measurement, quantum circuit abstraction

## 中文关键词

量子编译器, 量子比特复用, 量子电路优化, 电路中间测量, 量子电路抽象

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731020)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8B](index.md) · [返回 ISCA 2025](../index.md)
