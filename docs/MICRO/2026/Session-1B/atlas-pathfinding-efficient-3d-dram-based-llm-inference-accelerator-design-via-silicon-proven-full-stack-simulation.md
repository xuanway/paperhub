---
title: "ATLAS: Pathfinding Efficient 3D-DRAM-Based LLM Inference Accelerator Design via Silicon-Proven Full-Stack Simulation"
description: "MICRO 2026 · Session 1B · ATLAS：通过经芯片验证的全栈仿真探索高效三维 DRAM 大语言模型推理加速器设计"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "DRAM"
  - "Simulation"
---

# ATLAS: Pathfinding Efficient 3D-DRAM-Based LLM Inference Accelerator Design via Silicon-Proven Full-Stack Simulation

**中文标题：** ATLAS：通过经芯片验证的全栈仿真探索高效三维 DRAM 大语言模型推理加速器设计

**所属 Session：** [Session 1B](index.md) · [MICRO 2026](../index.md)

**作者：** Cong Li, Chenhao Xue, Yi Ren, Xiping Dong, Yu Cheng, Yinbo Hu, Fujun Bai, Yixin Guo, Xiping Jiang, Qiang Wu, Zhi Yang, Zhe Cheng, Yuan Xie, Guangyu Sun

**来源：** MICRO 2026，pp. 112–128；[DOI](https://doi.org/10.1109/MICRO67795.2026.00024)

## 英文摘要

Large language models (LLMs) exhibit memory-intensive behavior during decoding, making it a key bottleneck in LLM inference. To accelerate decoding execution, hybrid-bonding-based 3D-DRAM has been adopted in LLM accelerators. While this emerging technology provides strong performance gains over existing hardware, current 3D-DRAM accelerators (3D-Accelerators) rely on closed-source evaluation tools, limiting access to publicly available performance analysis methods. Moreover, existing designs are highly customized for specific scenarios, lacking a general and reusable full-stack modeling for 3D-Accelerators across diverse usecases. To bridge this fundamental gap, we present ATLAS, the first silicon-proven Architectural Three-dimesional-DRAM-based LLM Accelerator Simulation framework. Built on commercially deployed multi-layer 3D-DRAM technology, ATLAS introduces unified abstractions for both 3D-Accelerator architecture and programming primitives to support arbitrary LLM inference scenarios. Validation against real silicon shows that ATLAS achieves ≤8.57% simulation error and 97.26-99.96% correlation with measured performance. Through design space exploration with ATLAS, we demonstrate its ability to guide architecture design and distill key takeaways for both 3D-DRAM memory system and 3D-Accelerator microarchitecture across scenarios. ATLAS is open-sourced at https://github.com/pku-gsun/ATLAS-MICRO-2026, enabling further research on 3D-Accelerators.

## 中文摘要

大语言模型 (LLM) 在解码过程中表现出内存密集型行为，使其成为 LLM 推理的关键瓶颈。为了加速解码执行，LLM 加速器采用了基于混合键合的 3D-DRAM。虽然这种新兴技术比现有硬件提供了强大的性能提升，但当前的 3D-DRAM 加速器 (3D-Accelerators) 依赖于闭源评估工具，限制了对公开可用的性能分析方法的访问。此外，现有的设计是针对特定场景进行高度定制的，缺乏针对不同用例的 3D 加速器的通用且可重用的全栈建模。为了弥补这一根本差距，我们推出了 ATLAS，这是第一个经过硅验证的基于三维 DRAM 的架构 LLM 加速器模拟框架。 ATLAS 基于商业部署的多层 3D-DRAM 技术构建，为 3D 加速器架构和编程原语引入了统一抽象，以支持任意 LLM 推理场景。针对真实芯片的验证表明，ATLAS 的模拟误差≤8.57%，与测量性能的相关性为 97.26-99.96%。通过使用 ATLAS 进行设计空间探索，我们展示了其指导架构设计并提取跨场景 3D-DRAM 内存系统和 3D 加速器微架构关键要点的能力。 ATLAS 已在 https://github.com/pku-gsun/ATLAS-MICRO-2026 上开源，支持对 3D 加速器的进一步研究。

## 中文关键词

大语言模型；三维堆叠 DRAM；推理加速器；全栈仿真；芯片验证

## 代码与研究制品

- 代码仓库：[https://github.com/pku-gsun/ATLAS-MICRO-2026](https://github.com/pku-gsun/ATLAS-MICRO-2026)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21439810](https://doi.org/10.5281/zenodo.21439810)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 1B](index.md) · [MICRO 2026 主页](../index.md)
