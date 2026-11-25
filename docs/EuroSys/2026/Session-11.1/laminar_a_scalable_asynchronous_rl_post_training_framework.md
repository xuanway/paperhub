---
title: "Laminar: A Scalable Asynchronous RL Post-Training Framework"
description: "EuroSys 2026 · Distributed Training & Collective Communication · Guangming Sheng (The University of Hong Kong), Yuxuan Tong (ByteDance), Borui Wa"
tags:
  - "EuroSys2026"
  - "Distributed Training & Collective Communication"
---

# Laminar: A Scalable Asynchronous RL Post-Training Framework

**中文标题：** Laminar：可扩展的异步强化学习后训练框架

**所属 Session：** [Session 11.1: Distributed Training & Collective Communication](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Training & Collective Communication。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Training & Collective Communication</p>
</div>

**作者**：Guangming Sheng (The University of Hong Kong), Yuxuan Tong (ByteDance), Borui Wan (The University of Hong Kong), Wang Zhang (ByteDance), Chaobo Jia (The Chinese University of Hong Kong), Xibin Wu (Bytedance), Yuqi Wu (Shanghai Jiaotong University), Xiang Li (Bytedance), Chi Zhang (ByteDance), Yanghua Peng (ByteDance), Haibin Lin (ByteDance Inc.), Xin Liu (ByteDance Inc.), Chuan Wu (The University of Hong Kong)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803580)

## 英文摘要

Reinforcement learning (RL) post-training for Large Language Models (LLMs) is now scaling to large clusters and running for extended durations to enhance model reasoning performance. However, the scalability of existing RL frameworks is limited, as extreme long-tail skewness in RL trajectory generation causes severe GPU underutilization. Current asynchronous RL systems attempt to mitigate this, but they rely on global weight synchronization between the actor and all rollouts, which creates a rigid model update schedule. This global synchronization is ill-suited for the highly skewed and evolving distribution of trajectory generation latency in RL training, crippling training efficiency. Our key insight is that efficient scaling requires breaking this lockstep through trajectory-level asynchrony, which generates and consumes each trajectory independently. We propose Laminar, a scalable and robust RL post-training system built on a fully decoupled architecture. First, we replace global updates with a tier of relay workers acting as a distributed parameter service. This enables asynchronous and fine-grained weight synchronization, allowing rollouts to pull the latest weight anytime without stalling the actor’s training loop. Second, a dynamic repack mechanism consolidates long-tail trajectories onto a few dedicated rollouts, maximizing generation throughput. The fully decoupled design also isolates failures, ensuring robustness for long-running jobs. Our evaluation on a 1024-GPU cluster shows that Laminar achieves up to 5.48× training throughput speedup over state-of-the-art systems, while reducing model convergence time.

## 中文摘要

大语言模型（LLM）的强化学习（RL）后训练如今已扩展到大规模集群并长时间运行，以提升模型的推理能力。然而，现有 RL 框架的可扩展性受限，因为 RL 轨迹生成中极端的长尾偏斜导致 GPU 严重利用不足。当前的异步 RL 系统试图缓解这一问题，但它们依赖 actor 与所有 rollout 之间的全局权重同步，形成了僵化的模型更新调度。这种全局同步不适合 RL 训练中高度偏斜且不断演变的轨迹生成延迟分布，严重损害训练效率。我们的关键洞见是：高效扩展需要通过轨迹级异步打破这种锁步，即独立地生成和消费每条轨迹。我们提出 Laminar，一个构建于完全解耦架构之上的可扩展且健壮的 RL 后训练系统。首先，我们用一层中继 worker 作为分布式参数服务来替代全局更新。这实现了异步且细粒度的权重同步，使 rollout 可随时拉取最新权重而不阻塞 actor 的训练循环。其次，一种动态重打包机制将长尾轨迹集中到少数专用 rollout 上，最大化生成吞吐。完全解耦的设计还实现了故障隔离，确保长时间运行作业的健壮性。我们在 1024-GPU 集群上的评估表明，Laminar 相比最先进系统最高实现 5.48× 的训练吞吐加速，同时缩短了模型收敛时间。

**英文关键词：** RL Post-Training, Large-scale training, Asynchronous training

**中文关键词：** RL 后训练、大规模训练、异步训练

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
