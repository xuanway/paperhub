---
title: "Lembas: Cost-Efficient Genome Alignment with External Memory and FPGA Acceleration"
description: "ISCA 2026 · Session 4C · Lembas: Cost-Efficient Genome Alignment with External Memory and FPGA Acceleration"
tags:
  - "ISCA2026"
  - "Session 4C"
  - "Domain Specific Accelerators 1"
---

# Lembas: Cost-Efficient Genome Alignment with External Memory and FPGA Acceleration

**中文标题：** Lembas: 基于外存与 FPGA 加速的成本高效基因组比对

**所属 Session：** [Session 4C](index.md) · [ISCA 2026](../index.md)

**作者：** Seongyoung Kang, Se-Min Lim, Sang-Woo Jun

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

We present Lembas, a cost-efficient long-read genome alignment system designed to scale to the escalating memory and computational requirements of future genomic workloads. Conventional long-read aligners face two distinct scalability constraints in different stages of the pipeline: seeding demands large memory capacity, while extension demands high computational throughput, making larger genomes and deeper sequencing increasingly costly to support. Lembas improves scalability by reducing both the memory capacity required for seeding and the compute resources required for extension through a combination of reconfigurable FPGA acceleration and external-memory algorithms over NVMe SSDs. To our knowledge, Lembas is the first long-read genome alignment system to address both limitations in a single end-to-end system using off-the-shelf components, while preserving the algorithmic behavior of Minimap2. Lembas introduces two novel accelerators: The external-memory columnsort-based seeding accelerator to minimize memory requirements without performance loss, and a tiled Smith-Waterman-Gotoh extension accelerator which achieves competitive traceback performance despite the low clock speed of FPGAs. These novel accelerators, in addition to a conventional streaming chaining accelerator, time-shares each FPGA in the system. We built a prototype using an affordable desktop-class host with 16 GB of DRAM and 12 x86 cores, augmented with two mid-range Xilinx U50 FPGAs and M.2 NVMe SSDs. The resulting system performs on par with 3× costlier state-of-the-art A100 GPU-accelerated system and outperforms a 2× costlier state-of-the-art FPGA-accelerated system, resulting in corresponding cost and power efficiency. More importantly, Lembas achieves higher relative performance with larger genomes or deeper sequencing depth, ensuring current and future scalability.


## 中文摘要

我们提出 Lembas，一个成本高效的长读长基因组比对系统，旨在扩展到未来基因组工作负载不断攀升的内存和计算需求。传统长读长比对器在流水线的不同阶段面临两种不同的可扩展性约束：种子生成需要大内存容量，而扩展需要高计算吞吐量，使得更大基因组和更深测序深度的支持成本越来越高。Lembas 通过可重构 FPGA 加速与基于 NVMe SSD 的外存算法相结合，同时降低种子生成所需的内存容量和扩展所需的计算资源，从而提升可扩展性。据我们所知，Lembas 是首个使用商用组件在单一端到端系统中同时解决这两类限制的长读长基因组比对系统，同时保留了 Minimap2 的算法行为。Lembas 引入两个新型加速器：基于外存列排序（columnsort）的种子生成加速器，在不损失性能的前提下最小化内存需求；以及分块 Smith-Waterman-Gotoh 扩展加速器，尽管 FPGA 时钟频率较低，仍实现具有竞争力的回溯（traceback）性能。这些新型加速器与传统的流式链接（chaining）加速器分时复用系统中的每个 FPGA。我们使用一台配备 16 GB DRAM 和 12 个 x86 核心的经济型桌面级主机，加上两块中端 Xilinx U50 FPGA 和 M.2 NVMe SSD 构建了原型。所得系统的性能与成本高 3× 的最先进 A100 GPU 加速系统相当，并优于成本高 2× 的最先进 FPGA 加速系统，从而带来相应的成本和功耗效率。更重要的是，在更大基因组或更深测序深度下，Lembas 实现更高的相对性能，确保当前与未来的可扩展性。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2026](../index.md)
