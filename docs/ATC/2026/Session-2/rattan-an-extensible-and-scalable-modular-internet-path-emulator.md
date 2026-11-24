# Rattan: An Extensible and Scalable Modular Internet Path Emulator

**中文标题**：Rattan：一个可扩展、可伸缩的模块化互联网路径模拟器

**所属 Session**：[Session 2: Network Measurement and Simulation](index.md) · [ATC 2026](../index.md)

**作者**：Yixin Shen (Tsinghua University), Minhu Wang (Tsinghua University), Bo Wang (Tsinghua University), Haixuan Tong (Tsinghua University), Chenghao Li (Tsinghua University), Yutong Xie (Tsinghua University), Yixuan Gao (Tsinghua University), Mingwei Xu (Tsinghua University), Jianping Wu (Tsinghua University)

## 英文摘要
Modern transport and application innovations require evaluation over fast, heterogeneous, and dynamic Internet paths. Existing emulators do not simultaneously provide the expressiveness to model complex paths, the efficiency for high-throughput and concurrent experiments, and the scalability for large evaluation campaigns. We present Rattan, a modular Internet path emulator that separates path expression from execution. Users compose cells, each implementing one path effect, into channel graphs. A graph-aware runtime executes these graphs using metadata-oriented packet I/O and graph-aware scheduling, while a manager and orchestrator provision isolated channels across machines. Our evaluation demonstrates significant throughput improvement, efficient execution of complex path compositions, and dense concurrent emulation with stable results. A multipath case study shows that Rattan can reveal changes in performance rankings missed by other emulators. Deployment at a large CDN provider further demonstrates sustained pre-deployment evaluation and production extensibility. After integration into its workflow, the average congestion-control rollout cycle decreased from 24 weeks to 18 days.

## 中文摘要
现代传输层与应用层的创新需要在快速、异构且动态的互联网路径上进行评估。现有模拟器无法同时具备对复杂路径建模的表达能力、面向高吞吐与并发实验的效率，以及支撑大规模评估活动的可伸缩性。我们提出 Rattan，一个将路径表达与执行相分离的模块化互联网路径模拟器。用户把每个实现一种路径效应的 cell 组合成信道图。一个图感知的运行时使用面向元数据的包 I/O 与图感知调度来执行这些图，而管理器与编排器则跨机器供给相互隔离的信道。我们的评估展示了显著的吞吐提升、复杂路径组合的高效执行，以及结果稳定的高密度并发模拟。一个多路径案例研究表明，Rattan 能够揭示其他模拟器所遗漏的性能排名变化。在一家大型 CDN 提供商处的部署进一步证明了持续的部署前评估与生产环境中的可扩展性。在集成到其工作流之后，平均拥塞控制上线周期从 24 周缩短至 18 天。

## 英文关键词
Network emulation, Internet paths, modularity, reproducibility, transport evaluation

## 中文关键词
网络模拟，互联网路径，模块化，可复现性，传输层评估

[返回 Session 2](index.md) · [返回 ATC 2026](../index.md)
