Warp-STAR: High-Performance, Differentiable GPU-Accelerated Static Timing Analysis Through Warp-Oriented Parallel Orchestration
Authors：
[En-Ming Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=55065122110825161901)，[Shih-Hao Hung](https://63dac.conference-program.com/?post_type=page&p=15&uid=9932045343430867095)

## 中文标题

Warp-STAR：通过面向 warp 的并行编排实现高性能、可微的 GPU 加速静态时序分析

## 英文摘要

Static timing analysis (STA) is crucial for Electronic Design Automation (EDA) flows but remains a computational bottleneck. While existing GPU-based STA engines are faster than CPU, they suffer from inefficiencies, particularly intra-warp load imbalance caused by irregular circuit graphs. This paper introduces Warp-STAR, a novel GPU-accelerated STA engine that eliminates this imbalance by orchestrating parallel computations at the warp level. This approach achieves a 2.4X speedup over previous state-of-the-art (SoTA) GPU-based STA. When integrated into a timing-driven global placement framework, Warp-STAR delivers a 1.7X speedup over SoTA frameworks. The method also proves effective for differentiable gradient analysis with minimal overhead.

## 中文摘要

静态时序分析（STA）对电子设计自动化（EDA）流程至关重要，但始终是计算瓶颈。现有基于 GPU 的 STA 引擎虽然快于 CPU，却存在效率问题，尤其是由不规则电路图引起的 warp 内负载不均衡。本文提出 Warp-STAR，一种新颖的 GPU 加速 STA 引擎，通过在 warp 级别编排并行计算来消除该不均衡。该方法相较此前最先进（SoTA）的 GPU STA 取得 2.4 倍加速。当集成到时序驱动的全局布局框架中时，Warp-STAR 相较 SoTA 框架带来 1.7 倍加速。该方法对可微梯度分析同样有效，且额外开销极小。

## 英文关键词

Static Timing Analysis, GPU Acceleration, Irregular Graphs, Intra-Warp Load Imbalance

## 中文关键词

静态时序分析、GPU 加速、不规则图、warp 内负载不均衡
