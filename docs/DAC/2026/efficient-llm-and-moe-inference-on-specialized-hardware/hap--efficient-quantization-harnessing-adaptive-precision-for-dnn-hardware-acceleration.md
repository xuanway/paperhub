HAP: Efficient Quantization Harnessing Adaptive Precision for DNN Hardware Acceleration
Authors：
[Erjing Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=7708147204566399509)，[Xinkuang Geng](https://63dac.conference-program.com/?post_type=page&p=15&uid=07076846487607270501)，[Honglan Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=91048570719084638371)，[leibo liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=411243)，[Jie Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=273343)

## 中文标题

HAP：面向 DNN 硬件加速的利用自适应精度的高效量化

## 英文摘要

Post-training quantization (PTQ) avoids expensive training processes and is effective in accelerating deep neural networks (DNNs). Since the representation capacity of a quantizer decreases exponentially with precision, PTQ encounters fundamental limitations in the low-precision domain. As an alternative, adaptive-precision quantization (APQ) leverages the coding redundancy in binary representations to reduce precision without sacrificing resolution. This is especially suitable for activations, as they exhibit greater exploitable redundancy and lesser robustness than weights in PTQ. However, existing APQ approaches require data to heavily cluster near zero, which is not guaranteed in asymmetric quantization that is preferred for activations. Moreover, the precision variability in APQ leads to an unbalanced computational workload, making it difficult to effectively harvest the theoretical performance gain. To address these challenges, a novel quantization and accelerator design harnessing adaptive-precision (HAP), leverages a per-group dynamic zero-point to generalize APQ. Its intra-channel grouping strategy further enables balancing workloads through reordering. Leveraging a dual-precision vulnerable channel protection scheme for weights, it achieves superior accuracy compared with existing PTQ solutions at the level of 4 or 5 bits for a variety of DNN families. A novel bit-serial accelerator features a lightweight reorder engine, achieving a 2.65× speedup and a 55% energy reduction on average compared to existing designs.

## 中文摘要

训练后量化（PTQ）无需昂贵的训练过程，是加速深度神经网络（DNN）的有效手段。由于量化器的表示能力随精度呈指数级下降，PTQ 在低精度区间面临根本性限制。作为替代方案，自适应精度量化（APQ）利用二进制表示中的编码冗余，在不牺牲分辨率的前提下降低精度。这尤其适用于激活，因为在 PTQ 中激活比权重具有更多可利用的冗余且鲁棒性更低。然而，现有 APQ 方法要求数据高度聚集在零附近，而激活所偏好的非对称量化并不能保证这一点。此外，APQ 中精度的可变性导致计算负载不均衡，难以有效获取理论上的性能收益。为应对这些挑战，我们提出一种利用自适应精度的全新量化与加速器设计 HAP，它采用逐组动态零点来推广 APQ。其通道内分组策略通过重排序进一步实现负载均衡。针对权重，它采用双精度易损通道保护方案，在 4 比特或 5 比特水平上对多种 DNN 家族取得了优于现有 PTQ 方案的精度。一款全新的位串行加速器配备了轻量重排序引擎，相比现有设计平均取得 2.65× 的加速和 55% 的能耗降低。
