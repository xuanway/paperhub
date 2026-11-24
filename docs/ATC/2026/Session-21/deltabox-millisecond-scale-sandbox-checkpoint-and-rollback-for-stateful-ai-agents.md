# DeltaBox: Millisecond-Scale Sandbox Checkpoint and Rollback for Stateful AI Agents

**中文标题**：DeltaBox：面向有状态 AI 智能体的毫秒级沙箱检查点与回滚

**所属 Session**：[Session 21: New: Verification and Recovery of AI Systems](index.md) · [ATC 2026](../index.md)

**作者**：Yunpeng Dong (Shanghai Jiao Tong University), Jingkai He (Shanghai Jiao Tong University), Shiqi Liu (Shanghai Jiao Tong University), Yuze Hou (Shanghai Jiao Tong University), Dong Du (Shanghai Jiao Tong University), Zhonghu Xu (Huawei Technologies Co., Ltd.), Si Yu (Huawei Technologies Co., Ltd.), Baochuan Yang (Huawei Technologies Co., Ltd.), Yubin Xia (Shanghai Jiao Tong University), Haibo Chen (Shanghai Jiao Tong University)

## 英文摘要
Emerging LLM-powered AI agent workloads, such as test-time tree search and reinforcement learning (RL), require high-frequency state exploration, relying on rapid checkpoint/restore (C/R) of the complete sandbox state, including files and process state. Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R, which severely bottlenecks deep search and large-scale fan-outs. We observe that consecutive sandbox states between checkpoints differ only marginally. Therefore, instead of full duplication, a sandbox should only duplicate the changes between consecutive checkpoints (Key Insight), yet the lack of OS support makes this hard to realize. We propose a new OS-level abstraction, DeltaState, that delivers change-based C/R for agents through co-designed OS mechanisms. First, DeltaFS checkpoints file state by freezing the writable layer and inserting a new one, turning updates into copy-on-write and rollback into a layer switch. Second, DeltaCR quickly restores process state by forking from a frozen template process. A coordinator pairs the two so each checkpoint is one consistent (filesystem, memory) state. Building on these mechanisms, we present DeltaBox, an agent sandbox with millisecond-level C/R. On SWE-bench, DeltaBox hides its checkpoint work (10.83 ms) under inference and rolls back in a mean 1.86 ms, with the same warm-template fork driving low-cost RL rollout fan-out. DeltaBox is open-sourced at https://github.com/delta-box.

## 中文摘要
新兴的由 LLM 驱动的 AI 智能体负载，例如测试时树搜索和强化学习（RL），需要高频的状态探索，依赖对完整沙箱状态（包括文件和进程状态）的快速检查点/恢复（C/R）。现有机制会复制整个状态，导致每次 C/R 产生数百毫秒到数秒的延迟，严重制约深度搜索和大规模扇出。我们观察到，检查点之间相邻的沙箱状态只有极小的差异。因此，沙箱不应做全量复制，而只应复制相邻检查点之间的变化（核心洞见），但缺少操作系统支持使这一点难以实现。我们提出一种新的 OS 级抽象 DeltaState，通过协同设计的 OS 机制为智能体提供基于变化的 C/R。首先，DeltaFS 通过冻结可写层并插入一个新层来对文件状态做检查点，把更新转化为写时复制，把回滚转化为层切换。其次，DeltaCR 通过从冻结的模板进程 fork 来快速恢复进程状态。一个协调器将两者配对，使每个检查点都是一个一致的（文件系统、内存）状态。在这些机制之上，我们提出 DeltaBox，一个具备毫秒级 C/R 的智能体沙箱。在 SWE-bench 上，DeltaBox 将其检查点工作（10.83 ms）隐藏在推理之下，并以平均 1.86 ms 完成回滚，同一套热模板 fork 还驱动了低成本的 RL rollout 扇出。DeltaBox 已在 https://github.com/delta-box 开源。

## 英文关键词
AI agents, sandbox, checkpoint/restore, OverlayFS, copy-on-write

## 中文关键词
AI 智能体，沙箱，检查点/恢复，OverlayFS，写时复制

## 代码与研究制品

- [项目主页](https://github.com/delta-box)

[返回 Session 21](index.md) · [返回 ATC 2026](../index.md)
