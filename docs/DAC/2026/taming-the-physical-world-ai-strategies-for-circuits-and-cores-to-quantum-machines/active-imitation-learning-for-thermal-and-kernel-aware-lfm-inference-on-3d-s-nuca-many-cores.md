Active Imitation Learning for Thermal- and Kernel-Aware LFM Inference on 3D S-NUCA Many-Cores
Authors：
[Yixian Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=38464155909917029471)，[Chaoyao Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=3074370865382965621)，[Jan Deen](https://63dac.conference-program.com/?post_type=page&p=15&uid=96961631669233857621)，[George Floros](https://63dac.conference-program.com/?post_type=page&p=15&uid=9672463920549143928)，[Andy Pimentel](https://63dac.conference-program.com/?post_type=page&p=15&uid=7837915741825332279)，[Anuj Pathania](https://63dac.conference-program.com/?post_type=page&p=15&uid=626143)

## 中文标题

面向 3D S-NUCA 众核的热感知与内核感知 LFM 推理主动模仿学习

## 英文摘要

Large Foundation Model (LFM) inference is both memory-and compute-intensive, traditionally relying on GPUs. However, the limited availability and high cost have motivated the adoption of high-performance general-purpose CPUs, especially emerging 3D-stacked Static Non-Uniform Cache Architecture (3D S-NUCA) systems. These architectures offer enhanced bandwidth and locality but suffer from severe thermal challenges and uneven cache latencies due to 3D Networks-on-Chip (NoC). Optimal management of thread migration and V/f scaling is non-trivial due to LFM kernel diversity and system heterogeneity. Existing thermal management approaches often rely on oversimplified analytical models and lack adaptability. We propose AILFM, an Active Imitation Learning (AIL)-based scheduling framework that learns near-optimal thermal-aware scheduling policies from Oracle demonstrations with minimal run-time overhead. AILFM accounts for both core-level performance heterogeneity and kernel-specific behavior in LFMs to maintain thermal safety while maximizing performance. Extensive experiments show that AILFM outperforms state-of-the-art baselines and generalizes well across diverse LFM workloads.

## 中文摘要

大基础模型（LFM）推理兼具存储密集与计算密集的特性，传统上依赖 GPU。然而，GPU 资源有限且成本高昂，促使人们转而采用高性能通用 CPU，尤其是新兴的三维堆叠静态非一致缓存架构（3D S-NUCA）系统。此类架构提供更高的带宽与局部性，但由于三维片上网络（NoC），也面临严峻的热挑战与不均衡的缓存延迟。受 LFM 内核多样性与系统异构性影响，线程迁移与 V/f 调节的最优管理并非易事。现有热管理方法往往依赖过度简化的解析模型，且缺乏适应性。我们提出 AILFM，一种基于主动模仿学习（AIL）的调度框架，能够以极小的运行时开销从 Oracle 示范中学习近最优的热感知调度策略。AILFM 同时考虑核级性能异构性与 LFM 中内核特有的行为，在保持热安全的同时最大化性能。大量实验表明，AILFM 优于现有最先进基线，并能在多样的 LFM 工作负载上良好泛化。
