---
title: "DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference"
description: "MICRO 2026 · Session 7B · DeepStack：支持分布式 LLM 推理的三维 DRAM 堆叠加速器协同设计探索"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "DRAM"
  - "HW-SW Co-design"
---

# DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference

**中文标题：** DeepStack：支持分布式 LLM 推理的三维 DRAM 堆叠加速器协同设计探索

**所属 Session：** [Session 7B](index.md) · [MICRO 2026](../index.md)

**作者：** Zhiwen Mo, Guoyu Li, Hao Mark Chen, Yu Cheng, Zhengju Tang, Qianzhou Wang, Lei Wang, Shuang Liang, Lingxiao Ma, Yuxiao Guo, Wayne Luk, Jilong Xue, Hongxiang Fan

**来源：** MICRO 2026，pp. 2388–2405；[DOI](https://doi.org/10.1109/MICRO67795.2026.00164)

## 英文摘要

Advances in hybrid bonding and packaging have driven growing interest in 3D DRAM-stacked AI accelerators. As LLMs scale to hundreds of billions or trillions of parameters, distributed inference across multiple 3D chips has become essential for future AI serving. This trend makes cross-stack co-design critical: system-level parallelization and scheduling choices are tightly coupled with low-level hardware characteristics such as memory organization, interconnect, and thermal constraints. To enable early-stage co-design of distributed 3D AI systems, we present DeepStack, an accurate performance model and efficient design space exploration (DSE) framework for distributed 3D-stacked LLM inference. At the hardware level, DeepStack captures fine-grained 3D memory characteristics, such as transaction-aware bandwidth, bank activation constraints, buffering limitations, and thermal–power modeling. At the system level, DeepStack incorporates comprehensive parallelization strategies and execution scheduling for distributed LLM inference. With novel modeling techniques such as dual-stage network abstraction and tile-level compute–communication overlap, we achieve up to 100,000× faster runtime over state-of-the-art simulators at comparable accuracy. We cross-validate the modeling accuracy against our in-house 3D designs, NS-3 backend (2.12% error), and vLLM serving on 8×B200 GPUs (12.92% error). Combining with hierarchical design space search, DeepStack enables efficient exploration over ~2.5 × 10^14 design points spanning across the number of 3D-stacked DRAM layers, DRAM vertical connectivity, interconnect, compute-memory allocation, and distributed scheduling under thermal and area constraints. A search-space ablation shows that restricted DSE baselines can miss up to 9.5× modeled throughput. Beyond modeling and DSE, we demonstrate that DeepStack can be leveraged to derive design implications for distributed 3D AI systems, guiding performance optimization across the stack. Source code and artifacts are available at https://github.com/tile-ai/DeepStack/tree/ae

## 中文摘要

混合键合和封装的进步推动了人们对 3D DRAM 堆叠人工智能加速器的兴趣日益浓厚。随着大语言模型扩展到数千亿或数万亿个参数，跨多个 3D 芯片的分布式推理对于未来的人工智能服务至关重要。这种趋势使得跨堆栈协同设计变得至关重要：系统级并行化和调度选择与内存组织、互连和热约束等低级硬件特性紧密耦合。为了实现分布式 3D AI 系统的早期协同设计，我们推出了 DeepStack，这是一种用于分布式 3D 堆栈 LLM 推理的准确性能模型和高效设计空间探索 (DSE) 框架。在硬件层面，DeepStack 捕获细粒度的 3D 内存特征，例如事务感知带宽、存储体激活约束、缓冲限制和热功率建模。在系统层面，DeepStack结合了全面的并行化策略和分布式LLM推理的执行调度。借助双级网络抽象和分块级计算通信重叠等新颖的建模技术，我们在相当的精度下实现了比最先进的模拟器快 100,000 倍的运行时间。我们针对我们的内部 3D 设计、NS-3 后端（2.12% 错误）和在 8×B200 GPU 上服务的 vLLM（12.92% 错误）交叉验证建模准确性。与分层设计空间搜索相结合，DeepStack 能够在热和面积限制下对约 2.5 × 10^14 设计点进行高效探索，涵盖 3D 堆叠 DRAM 层数、DRAM 垂直连接、互连、计算内存分配和分布式调度。搜索空间消融表明，受限的 DSE 基线可能会错过高达 9.5 倍的建模吞吐量。除了建模和 DSE 之外，我们还证明可以利用 DeepStack 得出分布式 3D AI 系统的设计含义，从而指导整个堆栈的性能优化。源代码和研究制品可在 https://github.com/tile-ai/DeepStack/tree/ae 获取

## 中文关键词

三维 DRAM 堆叠加速器；设计空间探索；分布式大语言模型推理；性能建模

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/tile-ai/DeepStack/tree/ae](https://github.com/tile-ai/DeepStack/tree/ae)
- 研究制品归档：[https://zenodo.org/records/21351389](https://zenodo.org/records/21351389)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7B](index.md) · [MICRO 2026 主页](../index.md)
