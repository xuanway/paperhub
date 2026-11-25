Scalable and Adaptive Parallel Training of Graph Transformer on Large Graphs
Authors：
[Jun-Liang Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=58724578908563154671)，[Kamesh Madduri](https://63dac.conference-program.com/?post_type=page&p=15&uid=76904851215112941101)，[Mahmut Kandemir](https://63dac.conference-program.com/?post_type=page&p=15&uid=384643)

## 中文标题

大图上图 Transformer 的可扩展自适应并行训练

## 英文摘要

Graph foundation models have demonstrated remarkable adaptability across diverse downstream tasks through large-scale pretraining on graphs. However, existing implementations of the backbone model, graph transformers, are typically limited to single-GPU systems, leading to long training times or out-of-memory issues on large graphs. Moreover, parallelizing graph transformer training over the full graph is challenging, as efficiency depends heavily on both the graph structure and system characteristics, such as bandwidth and memory capacity. In this work, we introduce a distributed training framework for graph transformers, which automatically selects and optimizes parallelization strategies based on the graph structure and hardware configuration. With our implementation of distributed sparse operations, we accelerate sparse graph attention by up to 3.8x and reduce memory consumption by 78% compared to state-of-the-art frameworks. On large graph benchmarks, our proposed framework achieves up to 6x speedup with system scaling up to 8 GPUs. These results demonstrate that the proposed framework improves the scalability of graph transformers, bringing them closer to serving as practical graph foundation models.

## 中文摘要

图基础模型通过对图进行大规模预训练，在多种下游任务上展现出卓越的适应性。然而，其骨干模型——图 Transformer——的现有实现通常局限于单 GPU 系统，导致在大图上训练时间过长或出现内存不足问题。此外，在整个图上并行化图 Transformer 训练颇具挑战，因为效率在很大程度上取决于图结构与系统特性（如带宽和内存容量）。在本工作中，我们提出一个图 Transformer 的分布式训练框架，它根据图结构与硬件配置自动选择并优化并行化策略。借助我们实现的分布式稀疏算子，相比最先进框架，我们将稀疏图注意力加速最高 3.8 倍，并将内存消耗降低 78%。在大图基准上，所提框架在系统扩展至 8 块 GPU 时实现最高 6 倍加速。这些结果表明，所提框架提升了图 Transformer 的可扩展性，使其更接近可作为实用的图基础模型。
