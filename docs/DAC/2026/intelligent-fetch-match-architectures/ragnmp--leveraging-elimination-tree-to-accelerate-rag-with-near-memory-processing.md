RAGNMP: Leveraging Elimination Tree to Accelerate RAG with Near-Memory Processing
Authors：
[Dan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7081508471090800104)，[Huize Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=5335695194768397579)，[Zhaoying Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=96579215574630725841)，[Huiying Lan](https://63dac.conference-program.com/?post_type=page&p=15&uid=39008092908971335031)，[Xiang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4242767014324850101)，[Zerui Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=2099010589845800104)，[Dan Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1159461271599472599)，[Bin Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=40138255384532296961)，[Tulika Mitra](https://63dac.conference-program.com/?post_type=page&p=15&uid=187343)

## 中文标题

RAGNMP：利用消去树以近存处理加速 RAG

## 英文摘要

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by integrating information retrieval from knowledge databases, significantly improving the generated results’ accuracy, relevance, and contextual richness. An in-depth analysis of RAG reveals that its diverse operations are primarily constrained by memory bottlenecks. The diversity and continual evolution of RAG algorithms further increase system design complexity. In this paper, we introduce RAGNMP, a general-purpose Near-Memory Processing (NMP) accelerator designed for RAG. Specifically, we first propose an enhanced and quantified elimination tree variant that simultaneously explores data placement, task parallelism, and pipelining to better support RAG workloads on NMP architectures. It also remains adaptable to algorithm changes in RAG. We further propose a general-purpose NMP architecture with a flexible processing unit that efficiently supports diverse memory-bound operations in RAG. Experimental results show that RAGNMP outperforms the state-of-the-art RAG system and accelerator.

## 中文摘要

检索增强生成（RAG）通过整合来自知识库的信息检索来增强大语言模型（LLM），显著提升生成结果的准确性、相关性与上下文丰富度。对 RAG 的深入分析表明，其多样化的操作主要受内存瓶颈制约。RAG 算法的多样性与持续演进进一步增加了系统设计复杂度。本文提出 RAGNMP，一种为 RAG 设计的通用近存处理（NMP）加速器。具体而言，我们首先提出一种增强且可量化的消去树变体，它同时探索数据放置、任务并行与流水化，以更好地在 NMP 架构上支撑 RAG 负载，并且能够适应 RAG 算法的变化。我们进一步提出一种通用 NMP 架构，其灵活的处理单元可高效支持 RAG 中多样的内存受限操作。实验结果表明，RAGNMP 优于最先进的 RAG 系统与加速器。
