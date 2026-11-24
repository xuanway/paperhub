---
title: "Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference"
description: "ISCA 2026 · Session 10C · Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference"
tags:
  - "ISCA2026"
  - "Session 10C"
  - "PIM/PNM, cont."
---

# Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference

**中文标题：** Raptor 早期芯片：首个面向生成式推理的 3D-DRAM 加速器

**所属 Session：** [Session 10C](index.md) · [ISCA 2026](../index.md)

**作者：** Prashant J. Nair, Ramyad Hadidi, Subramani Ganesh, Sangamesh Kodge, Shubhankit Rathore, Neil Thanawala, Nikitha Reddy, Gyanesh Saharia, Vinayak Patankar, Arun Tiruvur, Nithesh Kurella, Sudeep Bhoja

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Generative Inference is largely memory-bound. Autoregressive decoding dominates inference runtime and thus drives memory bandwidth and capacity demands. SRAM-based accelerators offer high bandwidth but limited capacity, while HBM DRAM provides capacity but is constrained by bandwidth and power. 3D-stacked logic-on-DRAM (3D-DRAM) helps close this gap, but integrating 3D-DRAM with accelerator logic introduces four challenges: (1) workload-aware mapping to exploit parallelism, (2) power optimization without burst-based data bus inversion (DBI), (3) resilience with high bank counts, and (4) thermal reliability at elevated junction temperatures. This paper distills lessons from the early silicon of Raptor, the first commercial generative inference accelerator with 3D-stacked DRAM (3D-DRAM). This paper introduces four key architectural features to enable practical 3D-DRAM integration. First, stream-blocking maps KV-cache streams onto configurable 3D-DRAM channels, sustaining up to 100 TB/s per card while preserving bank-level parallelism. Second, pinless DBI on the single-cycle µbump interface reduces memory-subsystem energy. Third, topology-preserving redundancy with thermal-aware refresh. Fourth, interleaved ECC for reliability at high temperatures. Across Llama-3.1 70B, DeepSeek-V3, Kimi K2, GPT-OSS, Whisper, and Canary, Raptor 3D-DRAM gives 4.71× and 2.44× higher throughput than with HBM and SRAM, respectively, while being less sensitive to network latency and bandwidth.

## 中文摘要

生成式推理在很大程度上受内存限制。自回归解码在推理运行时间中占主导，因而驱动了内存带宽与容量需求。基于 SRAM 的加速器提供高带宽但容量有限，而 HBM DRAM 提供容量却受带宽与功耗制约。3D 堆叠的逻辑叠 DRAM（3D-DRAM）有助于弥合这一差距，但将 3D-DRAM 与加速器逻辑集成会带来四个挑战：(1) 感知工作负载的映射以利用并行性；(2) 在没有基于突发的数据总线反转（DBI）的情况下进行功耗优化；(3) 高 bank 数量下的可靠性；(4) 结温升高时的热可靠性。本文总结了 Raptor 早期硅片的经验教训——Raptor 是首个采用 3D 堆叠 DRAM（3D-DRAM）的商用生成式推理加速器。本文提出四项关键架构特性，以实现实用的 3D-DRAM 集成。第一，流式分块（stream-blocking）将 KV-cache 流映射到可配置的 3D-DRAM 通道上，在保持 bank 级并行性的同时，每张卡可维持高达 100 TB/s 的带宽。第二，在单周期 µbump 接口上采用无引脚 DBI，降低内存子系统能耗。第三，保持拓扑的冗余配合热感知刷新。第四，面向高温可靠性的交织式 ECC。在 Llama-3.1 70B、DeepSeek-V3、Kimi K2、GPT-OSS、Whisper 和 Canary 上，Raptor 3D-DRAM 的吞吐量分别比使用 HBM 和 SRAM 时高 4.71× 和 2.44×，同时对网络延迟和带宽的敏感度更低。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2026](../index.md)
