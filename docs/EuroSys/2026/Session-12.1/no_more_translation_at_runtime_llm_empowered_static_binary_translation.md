---
title: "No More Translation at Runtime: LLM-Empowered Static Binary Translation"
description: "EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning · Zhibo Liu (The Hong Kong University of Science and Technology), Huaijin Wang (Th"
tags:
  - "EuroSys2026"
  - "ML Model Optimization: Compilers, Quantization & Fine-Tuning"
---

# No More Translation at Runtime: LLM-Empowered Static Binary Translation

**中文标题：** 无需运行时翻译：LLM 赋能的静态二进制翻译

**所属 Session：** [Session 12.1: ML Model Optimization: Compilers, Quantization & Fine-Tuning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：ML Model Optimization: Compilers, Quantization & Fine-Tuning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning</p>
</div>

**作者**：Zhibo Liu (The Hong Kong University of Science and Technology), Huaijin Wang (The Hong Kong University of Science and Technology), Wai Kin Wong (The Hong Kong University of Science and Technology), Daoyuan Wu (Lingnan University), Shuai Wang (The Hong Kong University of Science and Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803600)

## 英文摘要

While AArch64 CPUs are becoming strong market contenders, their software ecosystem lags behind the mature x86-64 environment, hindering the adoption of the new architectures and impacting user experience. Binary translation bridges this divide by converting binary code from one architecture (e.g., x86-64) to run on another (e.g., AArch64), allowing legacy software to benefit from modern hardware’s performance and energy efficiency advantages.

Current translation methods are typically either dynamic, which adds significant runtime overhead, or static, which struggles with reliability due to the inherent complexities of binary analysis. This paper introduces a new static, assembly-to-assembly translation paradigm that transforms binary code ahead of execution, generating portable, efficient native-like binaries that run on AArch64 devices without runtime frameworks. Benefiting from recent breakthroughs in large language models (LLMs), we provide a practical and automated translation engine that produces high-quality code with minimal human intervention. To ensure correctness, we introduce a crucial verification step, where we split the assembly code into simplified snippets, enabling efficient and scalable semantic verification.

Our evaluation shows that this approach significantly outperforms existing open-source solutions with a large margin, producing binaries with near-native performance. Furthermore, it shows substantial improvements over the leading industrial translator, ExaGear, illuminating a promising new direction for cross-architecture binary translation research.

## 中文摘要

随着 AArch64 CPU 成为强有力的市场竞争者，其软件生态却落后于成熟的 x86-64 环境，阻碍了新架构的采用并影响用户体验。二进制翻译通过将二进制代码从一种架构（如 x86-64）转换到另一种架构（如 AArch64）上运行来弥合这一鸿沟，使遗留软件能够受益于现代硬件的性能和能效优势。

当前的翻译方法通常要么是动态的——会带来显著的运行时开销，要么是静态的——由于二进制分析固有的复杂性而难以保证可靠性。本文引入一种新的静态、汇编到汇编的翻译范式，在执行前转换二进制代码，生成可移植、高效、类原生的二进制文件，无需运行时框架即可在 AArch64 设备上运行。受益于大语言模型（LLM）的最新突破，我们提供了一个实用且自动化的翻译引擎，以最少的人工干预生成高质量代码。为确保正确性，我们引入一个关键的验证步骤，将汇编代码拆分为简化的片段，从而实现高效且可扩展的语义验证。

我们的评估表明，该方法以较大幅度显著优于现有开源方案，生成的二进制文件具有接近原生的性能。此外，它还相比领先的工业翻译器 ExaGear 有实质性提升，为跨架构二进制翻译研究指明了一个有前景的新方向。

**英文关键词：** Binary Translation, Cross-Architecture Migration, Large Language Models, Reverse Engineering

**中文关键词：** 二进制翻译、跨架构迁移、大语言模型、逆向工程

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
