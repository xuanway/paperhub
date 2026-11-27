PRICE: An Operator Recomputation and Fission Framework for Computation Graphs via Attainable Arithmetic Intensity
Authors：
[Minghua Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=942343)，[Fuyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7726526395623280415)，[Zhaoyun Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=23997776231558027831)

## 中文标题

PRICE：基于可达算术强度的计算图算子重计算与算子分裂框架

## 英文摘要

Computation graphs are fundamental for GPUs to efficiently deploy workloads. They also bring a challenge of growing memory demands. Operator recomputation and operator fission are promising directions to mitigate peak memory usage. However, existing work relies on offline decisions in recomputation and fission, leading to an increase in computation latency for only a marginal reduction in memory usage. In this paper, we propose PRICE, which is a novel operator recomputation and fission framework for computation graphs. Central to this framework is the attainable arithmetic intensity that can effectively trade off between memory usage and computation latency. We design a compile-time modeling approach to parameterize arithmetic intensity with GPU workload characteristics. Then we develop a runtime instantiation approach to attain the arithmetic intensity for online decision-making. Experiments on NVIDIA RTX 4090 and A100 demonstrate that PRICE achieves 1.08× to 1.31× speedup while delivering a comparable reduction in peak memory usage, compared to the state-of-the-art works.

## 中文摘要

计算图是 GPU 高效部署工作负载的基础，但也带来内存需求不断增长的挑战。算子重计算与算子分裂是缓解峰值内存占用的有前景方向。然而，已有工作依赖离线的重计算与分裂决策，导致在仅带来内存占用边际下降的同时反而增加了计算延迟。本文提出 PRICE，一种面向计算图的新型算子重计算与分裂框架。该框架的核心是可达算术强度（attainable arithmetic intensity），它能够有效权衡内存占用与计算延迟。我们设计了一种编译期建模方法，以 GPU 工作负载特征对算术强度进行参数化；进而提出一种运行时实例化方法，为在线决策获取算术强度。在 NVIDIA RTX 4090 与 A100 上的实验表明，与最先进工作相比，PRICE 在实现相当的峰值内存占用降低的同时，取得 1.08× 至 1.31× 的加速。
