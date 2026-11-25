TACo: Training-Free, Hardware-Aware ViT Architecture Search with a Hypervolume-Based Unified Zero-Cost Score
Authors：
[Eunji Kwon](https://63dac.conference-program.com/?post_type=page&p=15&uid=32659762406871007721)

## 中文标题

TACo：基于超体积统一零成本分数的免训练、硬件感知 ViT 架构搜索

## 英文摘要

We propose TACo, a training-free, hardware-aware architecture search framework for Vision Transformers (ViTs) powered by a Hypervolume-based Unified Zero-Cost Score (HV-score) integrating four accuracy-and hardware-related dimensions: a newly proposed zero-cost accuracy score (ZAS), latency, energy, and activation memory. TACo rapidly estimates the potential of candidate ViTs without training: ZAS captures layer-wise gradient stability, weight-gradient coupling, and gradient-modulated activation stability while HV-score guides multi-objective selection with Pareto and hypervolume principles. Experiments on CIFAR-10 and ImageNet-1k show that TACo reduces the search time from GPU-days to GPU-hours while finding a well-balanced ViT architecture in terms of accuracy and computational cost.

## 中文摘要

我们提出 TACo，一个免训练、硬件感知的视觉 Transformer（ViT）架构搜索框架，其核心是基于超体积的统一零成本分数（HV-score），融合了四个与精度和硬件相关的维度：新提出的零成本精度分数（ZAS）、延迟、能耗与激活内存。TACo 无需训练即可快速估计候选 ViT 的潜力：ZAS 刻画逐层梯度稳定性、权重-梯度耦合以及梯度调制的激活稳定性，而 HV-score 以 Pareto 与超体积原则引导多目标选择。在 CIFAR-10 和 ImageNet-1k 上的实验表明，TACo 将搜索时间从 GPU-天缩短至 GPU-小时，同时找到在精度与计算开销方面均衡良好的 ViT 架构。
