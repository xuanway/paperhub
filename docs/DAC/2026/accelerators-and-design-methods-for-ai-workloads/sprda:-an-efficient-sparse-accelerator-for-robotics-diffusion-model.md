SpRDA: An Efficient Sparse Accelerator for Robotics Diffusion Model
Authors：
[Renda Jian](https://63dac.conference-program.com/?post_type=page&p=15&uid=0476155778749739921)，[Yuzhou Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=5788779660219157624)，[Pan Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=02880383341021246181)，[Yitian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=13127515961650994351)，[Zhican Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=67813818264358358181)，[Xueling Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2620977719502564871)，[Chen Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9659998036895331133)，[Guanghui He](https://63dac.conference-program.com/?post_type=page&p=15&uid=8245643460890121186)

## 中文标题

SpRDA：一种面向机器人扩散模型的高效稀疏加速器

## 英文摘要

Diffusion models have recently demonstrated great performance in robotic manipulation, standing out with their ability to handling multi-modal action distributions and high-dimensional action spaces. However, its iterative computing feature limits realtime control in resource-constrained robot platform. Some of existing diffusion accelerators explored sparsity based on the similarity of adjacent steps, but suffering from low sparsity of full network and hardware inefficiency due to under-utilization of processing element (PE) and ignorance of more significant non-matrix-multiplication operators (NMOs) in sparse model. To address these issues, we propose SpRDA, an algorithm-architecture co-design accelerator that can achieve high-speed and energy-efficient inference of robotics diffusion model. A fine-grained and difference-aware cache algorithm combining differential computing and cache is proposed to identify more redundant computation in robotics diffusion, achieving over 90% sparsity with no distinct accuracy degradation. Furthermore, we apply two-level group sparsity adjusting and design a dynamic sparsity-aware matrix processing array to fully leverage sparsity in hardware. We also propose a graph-based vector unit to process various NMOs in higher throughput and lower area. Compared to the state-of-the-art diffusion accelerators, SpRDA achieves 1.56-2.60× speedup and 6.45-7.85× energy efficiency improvement.

## 中文摘要

扩散模型近来在机器人操作中展现出优异性能，其突出优势在于能够处理多模态动作分布和高维动作空间。然而，其迭代计算特性限制了资源受限机器人平台上的实时控制。现有的一些扩散加速器基于相邻步骤的相似性来挖掘稀疏性，但面临全网稀疏性低、处理单元（PE）利用率不足以及忽略稀疏模型中更重要的非矩阵乘法算子（NMO）等硬件效率问题。为解决这些问题，我们提出了 SpRDA，一种能够实现机器人扩散模型高速、高能效推理的算法-架构协同设计加速器。我们提出一种结合差分计算与缓存的细粒度差分感知缓存算法，以识别机器人扩散中更多的冗余计算，在精度无明显下降的情况下实现超过 90% 的稀疏性。此外，我们采用两级组稀疏调整，并设计动态稀疏感知矩阵处理阵列，以在硬件中充分利用稀疏性。我们还提出一种基于图的向量单元，以更高吞吐量和更小面积处理各种 NMO。与当前最优的扩散加速器相比，SpRDA 实现了 1.56-2.60 倍的加速和 6.45-7.85 倍的能效提升。

## 英文关键词

Embodied Artificial Intelligence, Diffusion Model, Sparsity Exploitation, Algorithm-Architecture Co-Design

## 中文关键词

具身智能、扩散模型、稀疏性挖掘、算法-架构协同设计
