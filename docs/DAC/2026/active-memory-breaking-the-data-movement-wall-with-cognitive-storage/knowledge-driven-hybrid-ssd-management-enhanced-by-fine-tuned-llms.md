Knowledge-Driven Hybrid SSD Management Enhanced by Fine-Tuned LLMs
Authors：
[Qian Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=02460108310512940031)，[Yi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=68212183459467932711)，[Zehao Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=382536017723056371)，[Tianren Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=7322820901763596142)，[Zhaoyan Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=010443)，[Dongxiao Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=00234952750427492331)，[Bingzhe Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=6510234104195560688)

## 中文标题

基于微调大语言模型的知识驱动混合 SSD 管理

## 英文摘要

A hybrid Solid-State Drives (SSDs) integrates different modes of flash cells (e.g., single-level cell (SLC) and Quad-Level Cell (QLC)) and enables them to convert between each other, achieving both high performance and storage capacity. However, this hybrid design introduces a significantly larger design space than traditional SSDs with additional design factors such as flash conversion and data migration across different flash modes, leading to higher optimization complexity. Efficient management of such complexity requires deep hybrid SSD knowledge and dynamic adjustment mechanisms. Large language models (LLMs) offer a promising solution through their contextual reasoning and adaptive coordination capabilities. In this work, we explore the potential of using LLMs in understanding and efficiently managing hybrid SSD design space. We find that leveraging LLMs for knowledge-guided optimization of management parameters enables substantial performance gains. Building on these insights, we propose LLM-hybridSSD, an integrated optimization framework that formulates hybrid SSD management as a parameter-tuning problem, employs an LLM-based tuner for adaptive configuration, and applies reinforcement learning-based fine-tuning to align local lightweight models with domain-specific knowledge. Experimental results show an average 58.92% increase in throughput and a 28.56% reduction in write amplification (WA) compared with state-of-the-art schemes under different real-world workloads.

## 中文摘要

混合固态硬盘（SSD）集成了不同模式的闪存单元（例如单层单元（SLC）和四层单元（QLC）），并使它们能够相互转换，从而同时实现高性能和大容量。然而，这种混合设计引入了比传统 SSD 大得多的设计空间，并增加了闪存模式转换和跨模式数据迁移等设计因素，导致优化复杂度更高。高效管理这种复杂性需要深入的混合 SSD 知识和动态调整机制。大语言模型（LLM）凭借其上下文推理和自适应协调能力，提供了一种有前景的解决方案。在本工作中，我们探索了利用 LLM 理解和高效管理混合 SSD 设计空间的潜力。我们发现，利用 LLM 对管理参数进行知识引导的优化能够带来显著的性能提升。基于这些见解，我们提出了 LLM-hybridSSD，一个集成优化框架；它将混合 SSD 管理建模为参数调优问题，采用基于 LLM 的调优器进行自适应配置，并应用基于强化学习的微调，使本地轻量级模型与领域知识对齐。实验结果表明，在不同的真实工作负载下，与当前最优方案相比，该框架平均将吞吐量提高 58.92%，并将写放大（WA）降低 28.56%。

## 英文关键词

Hybrid SSD Management, LLM, Fine-tuning

## 中文关键词

混合 SSD 管理、LLM、微调
