# Beyond Target Placement: Unified Multi-Objective Path-Aware Offline VM Scheduling at Scale

**中文标题**：超越目标放置：大规模下统一的多目标路径感知离线虚拟机调度

**所属 Session**：[Session 17: Scheduling and Serverless](index.md) · [ATC 2026](../index.md)

**作者**：Zihan Xu (Alibaba Cloud Computing), Zhidong Hu (Alibaba Cloud Computing), Zhengtong Zhang (Alibaba Cloud Computing), Fei Peng (Alibaba Cloud Computing), Kaiyuan Shen (Alibaba Cloud Computing), Feng Wang (Alibaba Cloud Computing), Xiangyun Kong (Alibaba Cloud Computing), Binda Ma (Alibaba Cloud Computing), Jian Zhou (Alibaba Cloud Computing)

## 英文摘要
Offline scheduling of virtual machines (VMs) in large-scale cloud clusters faces three core challenges: uniformly modeling heterogeneous business objectives, efficiently solving NP-hard problems at industrial scale, and producing feasible migration paths rather than merely computing target placements. This paper presents PAMOS (Path-Aware Multi-objective Offline Scheduling), an offline scheduling system built around a unified modeling framework that abstracts diverse constraints and objectives into a single additive cost minimization problem through several composable cost forms. A domain-specific language (DSL) enables nonexpert users to define rules in fewer than ten lines of code. At the solving level, a heuristic algorithm combining active and passive migration mechanisms directly produces feasible migration-path sequences. SVD-accelerated Tag-based Cost computation and a level-cache mechanism meet the minute-scale planning-time service-level objective (SLO). Evaluation on 631 production problems shows that, after path construction, three placement-based baselines realize only 14.7–20.3% of PAMOS’s optimization effectiveness and retain only 10.3–13.6% of their proposed migrations. At the scale where exact comparison is feasible, PAMOS achieves 97.0% of the path-aware mixed-integer programming (MIP) solver’s optimum with four orders of magnitude speedup. PAMOS has run stably at Alibaba Cloud for over eight years, processing thousands of tasks daily, achieving substantial cost reductions and stability improvements.

## 中文摘要
大规模云集群中的虚拟机离线调度面临三个核心挑战：统一建模异构的业务目标、在工业规模上高效求解 NP-hard 问题，以及产出可行的迁移路径而不仅仅是算出目标放置方案。本文提出 PAMOS（路径感知多目标离线调度），这是一个围绕统一建模框架构建的离线调度系统，该框架通过若干可组合的代价形式，把多样的约束与目标抽象为单一的加性代价最小化问题。领域特定语言（DSL）使非专家用户能在十行代码以内定义规则。在求解层面，一种结合主动与被动迁移机制的启发式算法直接产出可行的迁移路径序列。SVD 加速的基于标签的代价计算与层级缓存机制满足了分钟级规划时间的服务等级目标（SLO）。在 631 个生产问题上的评估表明，在构建路径之后，三个基于放置的基线仅实现 PAMOS 优化效果的 14.7%–20.3%，并且只保留其提出的迁移中的 10.3%–13.6%。在可进行精确比较的规模上，PAMOS 达到路径感知混合整数规划（MIP）求解器最优解的 97.0%，同时快四个数量级。PAMOS 已在阿里云稳定运行超过八年，每天处理数千个任务，实现了显著的成本下降与稳定性提升。

## 英文关键词
cloud computing, virtual machine, offline scheduling, live migration

## 中文关键词
云计算，虚拟机，离线调度，热迁移

[返回 Session 17](index.md) · [返回 ATC 2026](../index.md)
