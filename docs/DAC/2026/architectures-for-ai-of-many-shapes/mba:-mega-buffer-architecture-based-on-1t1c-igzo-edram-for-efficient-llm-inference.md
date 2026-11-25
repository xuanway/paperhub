MBA: Mega-Buffer Architecture Based on 1T1C IGZO eDRAM for Efficient LLM Inference
Authors：
[Siyuan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=52883720653599178311)，[Ruiqi Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=6302397042949834046)，[Jiaqi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=39785628780630534141)，[Shiyang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=5603868839812269506)，[Ao Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=66137284560213521161)，[Yiyang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=66366451799535334701)，[Yi Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5235345834510493071)，[Zhuohua Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8152976359211832939)，[Lifeng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4903035384379741554)，[Peng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7044907344583043329)

## 中文标题

MBA：基于 1T1C IGZO eDRAM 的超大缓冲区架构，实现高效 LLM 推理

## 英文摘要

Substantial weight and KV cache transfers between the GPU and HBM severely constrain Large Language Model (LLM) inference system performance. While LLM compression techniques can reduce memory footprint and transfer volume, existing methods are often task-specific and compromise model accuracy. This work proposes a mega-buffer architecture (MBA) that integrates gigabyte-scale on-chip buffers utilizing the embedded DRAM (eDRAM) technology recently introduced by TSMC. To fully leverage this large on-chip memory, we introduce a KV cache prioritized mapping (KVP) scheme that minimizes inefficient KV cache traffic between the HBM and the chip. Furthermore, a highly efficient pipeline integrating double buffering mechanism (DB) is co-designed with an iteration-aware eviction strategy (IA) to enhance data reuse and sustain high compute utilization. Evaluation results show that MBA attains 5.99x and 3.63x end-to-end speedup, and 8.86x and 4.93x energy efficiency improvement against GPU and LLM accelerator baselines, demonstrating a highly efficient architectural solution for LLM inference.

## 中文摘要

GPU 与 HBM 之间大量的权重与 KV 缓存传输严重制约了大型语言模型（LLM）推理系统的性能。尽管 LLM 压缩技术能够降低内存占用与传输量，但现有方法往往针对特定任务，且会损害模型精度。本工作提出一种巨型缓存架构（MBA），利用台积电近期引入的嵌入式 DRAM（eDRAM）技术集成吉字节量级的片上缓存。为充分利用这一大容量片上存储，我们引入 KV 缓存优先映射（KVP）方案，最大限度减少 HBM 与芯片之间低效的 KV 缓存传输。此外，我们将集成双缓冲机制（DB）的高效流水线与迭代感知驱逐策略（IA）协同设计，以提升数据复用并维持高计算利用率。评估结果表明，相较于 GPU 与 LLM 加速器基线，MBA 分别取得 5.99× 与 3.63× 的端到端加速比，以及 8.86× 与 4.93× 的能效提升，展示了面向 LLM 推理的高效架构方案。

## 英文关键词

Large Language Models, Embedded DRAM, AI Accelerators

## 中文关键词

大型语言模型、嵌入式 DRAM、AI 加速器
