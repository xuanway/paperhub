# FlexMARL: Graph-Driven Rollout-Training Co-Design for LLM-Based Multi-Agent Reinforcement Learning

**中文标题**：FlexMARL：面向基于 LLM 的多智能体强化学习的图驱动 rollout 与训练协同设计

**所属 Session**：[Session 19: Model Training](index.md) · [ATC 2026](../index.md)

**作者**：Zhida Jiang (JD.com), Zhaolong Xing (JD.com), Jiawei Lu (JD.com), Yipei Niu (Huawei), Qingyuan Sang (JD.com), Liangxu Zhang (JD.com), Wenquan Dai (Huawei), Junhua Shu (JD.com), Jiaxing Wang (JD.com), Qiangyu Pei (Huawei), Qiong Chen (Huawei), Xinyu Liu (Huawei), Fangming Liu (Huazhong University of Science and Technology), Ai Han (JD.com), Zhen Chen (JD.com), Ke Zhang (JD.com)

## 英文摘要
Despite algorithm-level innovations for multi-agent reinforcement learning (MARL), the underlying infrastructure for large-scale MARL remains underexplored. Existing training frameworks primarily optimize for single-agent scenarios and fail to capture the graph-structured nature of MARL. This fundamental mismatch leads to three MARL-specific challenges: topology-induced rollout skew, critical path synchronization barriers, and dynamic training demand. To bridge this gap, we propose FlexMARL, a graph-driven rollout-training co-designed framework for large-scale LLM-based MARL. FlexMARL introduces the multi-agent execution graph (MEG) and materializes the intermediate representation as the MEG Store, which provides decentralized multi-table storage and serves as the data hub for system components. Built around the MEG Store, the Rollout Engine develops dependency parallel sampling with hierarchical load balancing, which reduces inference latency and balances intra-agent/inter-agent loads. The Joint Orchestrator exploits an agent-level asynchronous pipeline to mitigate the critical path synchronization barriers while maintaining consistency. The Training Engine achieves on-demand resource allocation by collectively managing training processes for individual agents. The training states of different agents are swapped via location-agnostic communication APIs. Empirical results on a production cluster demonstrate that FlexMARL achieves up to 7.3× speedup and improves hardware utilization by up to 5.6× compared to existing frameworks.

## 中文摘要
尽管多智能体强化学习（MARL）在算法层面不断创新，支撑大规模 MARL 的底层基础设施仍研究不足。现有训练框架主要针对单智能体场景优化，未能刻画 MARL 的图结构特性。这种根本性的错配导致三个 MARL 特有的挑战：拓扑引发的 rollout 倾斜、关键路径同步屏障，以及动态的训练需求。为弥合这一缺口，我们提出 FlexMARL，一个面向大规模基于 LLM 的 MARL 的图驱动 rollout 与训练协同设计框架。FlexMARL 引入多智能体执行图（MEG），并将该中间表示物化为 MEG Store，它提供去中心化的多表存储，并作为各系统组件的数据枢纽。围绕 MEG Store，rollout 引擎开发了带分层负载均衡的依赖并行采样，降低了推理延迟并平衡了智能体内与智能体间的负载。联合编排器利用智能体级异步流水线来缓解关键路径同步屏障，同时保持一致性。训练引擎通过统一管理各个智能体的训练进程实现按需资源分配。不同智能体的训练状态通过位置无关的通信 API 进行交换。在生产集群上的实证结果表明，与现有框架相比，FlexMARL 最高取得 7.3× 的加速，并将硬件利用率最高提升 5.6×。

## 英文关键词
Multi-Agent Reinforcement Learning, Large Language Models, Distributed Training

## 中文关键词
多智能体强化学习，大语言模型，分布式训练

[返回 Session 19](index.md) · [返回 ATC 2026](../index.md)
