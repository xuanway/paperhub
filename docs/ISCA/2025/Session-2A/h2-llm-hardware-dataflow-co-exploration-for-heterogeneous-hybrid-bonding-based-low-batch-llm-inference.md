---
title: "H2-LLM: Hardware-Dataflow Co-Exploration for Heterogeneous Hybrid-Bonding-based Low-Batch LLM Inference"
description: "ISCA 2025 · Session 2A · H2-LLM：面向异构混合键合低批量 LLM 推理的硬件—数据流协同探索"
tags:
  - "ISCA2025"
  - "Session 2A"
  - "Best Paper Nominees"
---

# H2-LLM: Hardware-Dataflow Co-Exploration for Heterogeneous Hybrid-Bonding-based Low-Batch LLM Inference

**中文标题：** H2-LLM：面向异构混合键合低批量 LLM 推理的硬件—数据流协同探索

**所属 Session：** [Session 2A](index.md) · [ISCA 2025](../index.md)

**作者：** Cong Li, Yihan Yin, Xintong Wu, Jingchen Zhu, Zhutianya Gao, Dimin Niu, Qiang Wu, Xin Si, Yuan Xie, Chen Zhang, Guangyu Sun

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731008) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Low-batch large language model (LLM) inference has been extensively applied to edge-side generative tasks, such as personal chat helper, virtual assistant, reception bot, private edge server, etc. To efficiently handle both prefill and decoding stages in LLM inference, near-memory processing (NMP) enabled heterogeneous computation paradigm has been proposed. However, existing NMP designs typically embed processing engines into DRAM dies, resulting in limited computation capacity, which in turn restricts their ability to accelerate edge-side low-batch LLM inference.

To tackle this problem, we propose H2-LLM, a Hybrid-bonding-based Heterogeneous accelerator for edge-side low-batch LLM inference. To balance the trade-off between computation capacity and bandwidth intrinsic to hybrid-bonding technology, we propose H2-LLM’s architecture and extract its architecture design space. We further propose a data-centric dataflow abstraction to fully exploit the heterogeneous architecture’s acceleration opportunities in low-batch LLM inference. Based on the whole design space, we propose a design space exploration (DSE) framework to automatically find out the optimal design. Compared with existing in-die NMP-based heterogeneous accelerators, H2-LLM achieves 2.72× geomean speedup and 1.48×geomean better energy efficiency.  H2-LLM’s data-centric dataflow exploration framework is open-sourced at https://github.com/leesou/H2-LLM-ISCA-2025.

## 中文摘要

小批量大语言模型（LLM）推理已广泛应用于边缘端生成式任务，例如个人对话助手、虚拟助理、接待机器人、私有边缘服务器等。为高效支持LLM推理的预填充阶段和解码阶段，研究者提出了近内存计算（NMP）异构计算架构。但现有NMP方案大多将计算引擎集成在DRAM裸片内部，算力受限，难以对边缘端小批量LLM推理形成有效加速。

针对该问题，本文提出H2-LLM：一款基于混合键合技术、面向边缘端小批量LLM推理的异构加速器。为平衡混合键合技术本身算力与带宽之间的权衡关系，我们设计了H2-LLM架构，并挖掘其架构设计空间。本文进一步提出以数据为中心的数据流抽象，充分释放该异构架构在小批量LLM推理场景下的加速潜力。依托完整设计空间，我们搭建设计空间探索（DSE）框架，自动搜索最优配置。对比现有基于裸片内NMP的异构加速器，H2-LLM实现几何平均2.72倍的性能加速，能量效率几何平均提升1.48倍。H2LLM 以数据为中心的数据流探索框架在 https://github.com/leesou/H2-LLM-ISCA-2025 上开源。

## 英文关键词

Large Language Model, Hybrid Bonding, Near-Memory Processing

## 中文关键词

大语言模型, 混合键合, 近存处理

## 代码与研究制品

- [代码仓库](https://github.com/leesou/H2-LLM-ISCA-2025)
- [研究制品](https://doi.org/10.5281/zenodo.15078697)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731008)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 2A](index.md) · [返回 ISCA 2025](../index.md)
