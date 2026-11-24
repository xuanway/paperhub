---
title: "Sharpen the Spec, Cut the Code: A Case for Generative File System with SYSSPEC"
description: "FAST 2026 · AI and LLMs II · 第 291–312 页"
tags:
  - "FAST2026"
  - "AI and LLMs II"
---

# Sharpen the Spec, Cut the Code: A Case for Generative File System with SYSSPEC

**中文标题**：磨利规范，精简代码：论基于 SYSSPEC 的生成式文件系统

**Session**：AI and LLMs II · 2026-02-25 10:50–12:30 · Chair：Jian Zhang（The Hong Kong University of Science and Technology）

**作者**：Qingyuan Liu, Mo Zou, Hengbin Zhang, Dong Du, Yubin Xia, and Haibo Chen, Shanghai Jiao Tong University

**会议**：FAST 2026 · Santa Clara, CA · 第 291–312 页

**获奖**：Best Paper、Distinguished Artifact Award

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/liu-qingyuan](https://www.usenix.org/conference/fast26/presentation/liu-qingyuan)

**论文 PDF**：[fast26-liu-qingyuan.pdf](https://www.usenix.org/system/files/fast26-liu-qingyuan.pdf)

---

## 英文摘要

File systems are critical OS components that require constant evolution to support new hardware and emerging application needs. However, the traditional paradigm of developing features, fixing bugs, and maintaining the system incurs significant overhead, especially as systems grow in complexity. This paper proposes a new paradigm, *generative file systems*, which leverages Large Language Models (LLMs) to generate and evolve a file system from prompts, effectively addressing the need for robust evolution. Despite the widespread success of LLMs in code generation, attempts to create a functional file system have thus far been unsuccessful, mainly due to the ambiguity of natural language prompts.

This paper introduces SYSSPEC, a framework for developing generative file systems. Its key insight is to *replace ambiguous natural language with principles adapted from formal methods*. Instead of imprecise prompts, SYSSPEC employs a multi-part specification that accurately describes a file system's functionality, modularity, and concurrency. The specification acts as an unambiguous blueprint, guiding LLMs to generate expected code flexibly. To manage evolution, we develop a *DAG-structured patch* that operates on the specification itself, enabling new features to be added without violating existing invariants. Moreover, the SYSSPEC toolchain features a set of LLM-based agents with mechanisms to mitigate hallucination during construction and evolution. We demonstrate our approach by generating SPECFS, a concurrent file system. SPECFS demonstrates equivalent level of correctness to that of a manually-coded baseline across hundreds of regression tests. We further confirm its evolvability by seamlessly integrating 10 real-world features from Ext4. Our work shows that a specification-guided approach makes generating and evolving complex systems not only feasible but also highly effective.

## 中文摘要

文件系统是操作系统中的关键组件，需要不断演进以支持新硬件和新兴应用需求。然而，传统范式——开发功能、修复缺陷和维护系统——会带来显著开销，尤其当系统复杂性增长时。本文提出一种新范式——生成式文件系统，它利用大语言模型（LLM）根据提示生成并演进文件系统，从而有效满足稳健演进的需求。尽管 LLM 在代码生成方面取得了广泛成功，但创建可运行文件系统的尝试迄今尚未成功，主要原因是自然语言提示存在歧义。

本文介绍 SYSSPEC，一个用于开发生成式文件系统的框架。其核心洞见是：用源自形式化方法的原则替代有歧义的自然语言。SYSSPEC 不使用不精确的提示，而是采用由多个部分组成的规范，准确描述文件系统的功能、模块化和并发性。该规范充当无歧义的蓝图，引导 LLM 灵活地生成预期代码。为管理演进，我们开发了一种作用于规范本身的 DAG 结构补丁，使新功能能够在不违反现有不变式的情况下加入。此外，SYSSPEC 工具链包含一组基于 LLM 的智能体，并带有在构建和演进过程中缓解幻觉的机制。我们通过生成并发文件系统 SPECFS 来演示该方法。在数百项回归测试中，SPECFS 表现出与手工编码基线相当的正确性水平。我们进一步通过无缝集成来自 Ext4 的 10 项真实世界功能来确认其可演进性。我们的工作表明，规范引导的方法不仅使生成和演进复杂系统变得可行，而且非常有效。
