---
title: "PointShuffler: Accelerating Point Cloud Neural Networks on General-Purpose GPUs"
description: "EuroSys 2026 · GPU Systems, Graph Computing & Applied ML · Yangfan Li (School of Computer Science and Engineering, Central South University"
tags:
  - "EuroSys2026"
  - "GPU Systems, Graph Computing & Applied ML"
---

# PointShuffler: Accelerating Point Cloud Neural Networks on General-Purpose GPUs

**中文标题：** PointShuffler：在通用 GPU 上加速点云神经网络

**所属 Session：** [Session 12.3: GPU Systems, Graph Computing & Applied ML](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：GPU Systems, Graph Computing & Applied ML。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · GPU Systems, Graph Computing & Applied ML</p>
</div>

**作者**：Yangfan Li (School of Computer Science and Engineering, Central South University), Zhengjie Jin (School of Computer Science and Engineering, Central South University), Yue Tian (School of Computer Science and Engineering, Central South University), Mengquan Li (College of Information Science and Engineering, Hunan University), Fengxiao Tang (School of Computer Science and Engineering, Central South University), Ming Zhao (School of Computer Science and Engineering, Central South University), Cen Chen (School of Future Technology, South China University of Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803611)

## 英文摘要

Point Cloud Neural Networks (PCNNs) have emerged as a vital tool for latency-sensitive 3D perception applications, such as autonomous driving and AR/VR. However, their inherent computational redundancy—arising from excessive global sampling/search operations and repeated feature updates/aggregations caused by shared neighbors—severely constrains execution efficiency. More critically, conventional redundancy elimination methods usually introduce operations that are highly GPU-unfriendly, resulting in high memory overhead, increased branch divergence, irregular memory access, and serial dependencies, which together pose a significant challenge to PCNN acceleration.

To this end, we propose PointShuffler, the first-of-its-kind GPU-friendly inference engine that efficiently eliminates PCNN redundancy with preserved accuracy. It consists of three enabling optimizations: (1) Network Architecture Transformation, which can convert a typical PCNN into an architecture variant with well-eliminated redundancy while negligible accuracy losses; (2) Data Orchestration, which arranges the irregular data access inherent in 3D point clouds into deterministic and contiguous data access, to fundamentally alleviate the costs from data access, branch divergence, and data movement; and (3) Operation Parallelization, which enables parallel sampling and neighbor searching by eliminating serial dependencies lie in the core operations of PCNNs. Extensive experimental results demonstrate the effectiveness of PointShuffler, achieving an average of 6.15× speedup and at least 5.30× memory saving without accuracy loss. The codes of PointShuffler are released at https://github.com/Jeff5trick/PointShuffler.

## 中文摘要

点云神经网络（PCNN）已成为自动驾驶和 AR/VR 等延迟敏感的 3D 感知应用的重要工具。然而，其固有的计算冗余——源于过多的全局采样与搜索操作，以及共享邻居导致的重复特征更新与聚合——严重制约了执行效率。更关键的是，传统的冗余消除方法通常会引入对 GPU 极不友好的操作，导致高昂的内存开销、更多的分支发散、不规则的内存访问以及串行依赖，这些共同对 PCNN 加速构成了重大挑战。

为此，我们提出 PointShuffler，这是首个在保持精度的前提下高效消除 PCNN 冗余的 GPU 友好推理引擎。它包含三项关键优化：（1）网络架构变换，可将典型的 PCNN 转换为冗余已被良好消除且精度损失可忽略的架构变体；（2）数据编排，将 3D 点云固有的不规则数据访问安排为确定且连续的数据访问，从根本上缓解数据访问、分支发散与数据移动带来的开销；（3）操作并行化，通过消除 PCNN 核心操作中存在的串行依赖，实现并行采样与邻居搜索。大量实验结果表明了 PointShuffler 的有效性：在无精度损失的情况下平均实现 6.15 倍加速，并至少节省 5.30 倍内存。PointShuffler 的代码已在 https://github.com/Jeff5trick/PointShuffler 发布。

**英文关键词：** Point Cloud Neural Networks, GPU Acceleration, Redundancy Elimination

**中文关键词：** 点云神经网络、GPU 加速、冗余消除

## 代码与研究制品

- [代码](https://github.com/Jeff5trick/PointShuffler)（论文摘要提供）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
