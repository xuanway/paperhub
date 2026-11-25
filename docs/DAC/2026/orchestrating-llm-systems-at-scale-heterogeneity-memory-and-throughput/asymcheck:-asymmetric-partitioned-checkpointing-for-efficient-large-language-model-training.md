Asymcheck: Asymmetric Partitioned Checkpointing for Efficient Large Language Model Training
Authors：
[Zhangqiang Ming](https://63dac.conference-program.com/?post_type=page&p=15&uid=7518605749296573392)，[Yuchong Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7589487054955796938)，[Zhiyuan Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=66175325492342061071)，[Patrick P. C. Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=7458903579435810806)，[Yuanhao Shu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5054770536258050206)，[Xinjue Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=8797870214325797666)，[Wenxiang Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=7110651454797517573)，[Dan Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=342343)

## 中文标题

AsymCheck：面向高效大语言模型训练的非对称分区检查点

## 英文摘要

Distributed large language model (LLM) training faces prevalent failures and requires efficient checkpointing. State-of-the-art approaches employ partition-based pipelined checkpointing, splitting checkpoints into partitions for concurrent processing. However, existing solutions rely on a fixed partition size, which our analysis reveals is suboptimal for LLM training: large partitions cause bandwidth stalls during forward passes, while small partitions incur substantial startup overhead during backward passes. We propose AsymCheck, which employs asymmetric partitioning: small partitions for forward passes and large partitions for backward passes, plus selective partition compression and batched flushing optimizations. Evaluation on 64 GPUs shows AsymCheck reduces training time by 20.1%-48.2% over state-of-the-art methods, approaching no-checkpointing efficiency.

## 中文摘要

分布式大语言模型（LLM）训练普遍面临故障，需要高效的检查点机制。最先进的方法采用基于分区的流水线式检查点，将检查点切分为多个分区以并发处理。然而，现有方案依赖固定的分区大小，我们的分析表明这对 LLM 训练而言并非最优：大分区会在前向传播期间造成带宽停顿，小分区则在反向传播期间引入可观的启动开销。我们提出 AsymCheck，采用非对称分区：前向传播使用小分区，反向传播使用大分区，并辅以选择性分区压缩与批量冲刷优化。在 64 个 GPU 上的评估表明，AsymCheck 相较最先进方法将训练时间缩短 20.1%–48.2%，接近无检查点时的效率。
