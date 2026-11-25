Hybrid PIM-Oriented Architecture-Dataflow Co-Design for Heterogeneous LLM Inference
Authors：
[Hai Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=07272036090320156621)，[Feng Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1625520048303651567)，[Xiang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=114843)，[Weisheng Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=061443)，[Chenchen Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1821160613403026339)

## 中文标题

面向混合 PIM 的异构 LLM 推理架构-数据流协同设计

## 英文摘要

Recent studies show that incorporating Processing-in-Memory (PIM) into neural processing units (NPUs) can significantly improve the efficiency of large language model (LLM) inference on edge devices. However, the limited compute capability of DRAM-PIM and the use of fixed dataflow strategies still constrain overall performance gains. To address these limitations, we propose a hybrid PIM architecture that integrates non-volatile spin-orbit torque magnetic random-access memory (SOT-MRAM)-based PIM into existing NPU-PIM systems, fully exploiting the high compute capability and bandwidth of SOT-MRAM together with the large storage capacity of DRAM. On top of this architecture, we further design an adaptive compute scheduling and dataflow optimization framework. Using NSGA-II-based multi-objective dataflow space exploration, our framework identifies Pareto-optimal hardware resource allocations and dataflow configurations under different deployment objectives. Experimental results show that our approach reduces inference latency by up to 8.72× and energy consumption by 11.74× compared to NPUs, and further achieves 6.24× lower latency and 7.76× higher energy efficiency than NPU-PIM baselines.

## 中文摘要

近期研究表明，将存内计算（PIM）引入神经处理单元（NPU）可显著提升边缘设备上大语言模型（LLM）推理的效率。然而，DRAM-PIM 有限的计算能力以及固定的数据流策略仍然制约着整体性能提升。为克服这些局限，我们提出一种混合 PIM 架构，将基于非易失性自旋轨道矩磁随机存储器（SOT-MRAM）的 PIM 集成到现有的 NPU-PIM 系统中，充分利用 SOT-MRAM 的高计算能力与大带宽以及 DRAM 的大容量存储。在此架构之上，我们进一步设计了自适应计算调度与数据流优化框架。借助基于 NSGA-II 的多目标数据流空间探索，该框架能够在不同的部署目标下找出帕累托最优的硬件资源分配与数据流配置。实验结果表明，与 NPU 相比，我们的方法将推理延迟最多降低 8.72 倍、能耗降低 11.74 倍，并且相比 NPU-PIM 基线进一步实现 6.24 倍的更低延迟与 7.76 倍的更高能效。

## 英文关键词

Heterogeneous LLM Inference, Architecture-Dataflow Co-Design, SOT-MRAM-PIM

## 中文关键词

异构 LLM 推理、架构-数据流协同设计、SOT-MRAM-PIM
