PIMGRAG: A Heterogeneous PIM Architecture for Graph-Based Retrieval-Augmented Generation
Authors：
[Zhaoyu Zhong](https://63dac.conference-program.com/?post_type=page&p=15&uid=10452314555911753431)，[Yunhao Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=57557561104456963911)，[Yaodong Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=76792985475625473821)，[Jiaxian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=37582528852818661511)，[Tianyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4102639928273142851)，[Chenlin Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=4213970674159892189)，[Rui Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=430343)，[Kecheng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9023677625232671802)，[Yi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=030343)

## 中文标题

PIMGRAG：面向基于图的检索增强生成的异构 PIM 架构

## 英文摘要

Graph-based retrieval-augmented generation (RAG) improves the interpretability and factual consistency of large language models (LLMs) through structured knowledge graphs. Despite these benefits, graph-based RAG suffers from inefficient retrieval. The retrieval stage causes massive movement of vector and graph data between memory and processors. This movement leads to low arithmetic intensity and heavy pressure on memory bandwidth. This work presents PIMGRAG, a heterogeneous architecture that accelerates graph-based RAG through hardware/software codesign. At the hardware level, PIMGRAG designs a PIM architecture for the retrieval stage, which reduces off-chip data transfer by executing bandwidth-intensive operations near memory. At the software level, PIMGRAG applies a lightweight scheduling method that orchestrates PIM and GPU execution and lowers idle time across stages. Evaluation results show improvements in throughput, latency, and energy efficiency over CPU–GPU and existing PIM-based baselines.

## 中文摘要

基于图的检索增强生成（RAG）通过结构化知识图谱提升了大型语言模型（LLM）的可解释性与事实一致性。尽管具有这些优势，基于图的 RAG 仍受制于低效的检索过程。检索阶段需要在内存与处理器之间搬运大量向量与图数据，这种搬运导致算术强度低、内存带宽压力沉重。本文提出 PIMGRAG，一种通过软硬件协同设计加速基于图的 RAG 的异构架构。在硬件层面，PIMGRAG 为检索阶段设计了 PIM 架构，通过在近内存处执行带宽密集型操作来减少片外数据传输。在软件层面，PIMGRAG 采用轻量级调度方法，统筹 PIM 与 GPU 的执行并降低各阶段之间的空闲时间。评估结果表明，相较于 CPU–GPU 方案以及现有的基于 PIM 的基线，PIMGRAG 在吞吐率、延迟和能效方面均有所提升。

## 英文关键词

Graph-based RAG, Processing-in-Memory, HW/SW Co-design

## 中文关键词

基于图的 RAG、存内计算、软硬件协同设计
