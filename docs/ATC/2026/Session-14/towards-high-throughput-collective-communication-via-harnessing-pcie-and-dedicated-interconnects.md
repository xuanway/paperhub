# Towards High-Throughput Collective Communication via Harnessing PCIe and Dedicated Interconnects

**中文标题**：面向高吞吐集合通信：利用 PCIe 与专用互连

**所属 Session**：[Session 14: Networking I](index.md) · [ATC 2026](../index.md)

**作者**：Yuezheng Liu (Beihang University), Menghao Zhang (Beihang University), Xuebin Song (Beihang University), Juner Shen (Beihang University), Chunming Hu (Beihang University), Xudong Liu (Beihang University)

## 英文摘要
Collective communication libraries (CCLs) for distributed LLM training focus mainly on dedicated high-speed interconnects and leave PCIe bandwidth under-exploited. For PCIe-only machines, they model collectives as GPU-to-GPU communication and create redundant traffic in the CPU-rooted PCIe hierarchy. For machines with dedicated interconnects, they either ignore PCIe or use a static multipath split that cannot react to runtime PCIe interference. This paper presents HyLink, a two-layer collective communication framework that unlocks PCIe bandwidth and aggregates it with dedicated interconnects. PCIe CCL makes this hierarchy explicit and uses host memory as an active routing point. It expresses topology-aware schedules in a CPU-driven DSL and executes them with an auto-pipelined runtime on GPU copy engines. Multipath Orchestrator splits each collective between the dedicated link and PCIe, and uses runtime feedback to rebalance the split under PCIe interference. In our evaluation across different PCIe-only topologies, PCIe CCL improves large-message collective bandwidth by 26.2% on average over NCCL and reduces Megatron-LM iteration time by 6.1%–6.6%. On the Ascend platform with dedicated interconnects, Multipath Orchestrator improves large-message collective bandwidth by 10.4% on average over HCCL and reduces Megatron-LM iteration time by 2.3%–4.6%.

## 中文摘要
面向分布式 LLM 训练的集合通信库（CCL）主要关注专用高速互连，而使 PCIe 带宽未得到充分利用。对于仅有 PCIe 的机器，它们将集合通信建模为 GPU 到 GPU 的通信，在以 CPU 为根的 PCIe 层次结构中产生冗余流量。对于配有专用互连的机器，它们要么忽略 PCIe，要么使用无法对运行时 PCIe 干扰做出反应的静态多路径拆分。本文提出 HyLink，一个两层集合通信框架，释放 PCIe 带宽并将其与专用互连聚合。PCIe CCL 使该层次结构显式化，并将主机内存用作主动路由点。它用 CPU 驱动的 DSL 表达拓扑感知的调度，并在 GPU 拷贝引擎上以自动流水化的运行时执行这些调度。多路径编排器将每个集合通信在专用链路与 PCIe 之间拆分，并利用运行时反馈在 PCIe 干扰下重新平衡拆分比例。在跨不同纯 PCIe 拓扑的评估中，PCIe CCL 相比 NCCL 将大消息集合通信带宽平均提升 26.2%，并将 Megatron-LM 迭代时间缩短 6.1%–6.6%。在配有专用互连的 Ascend 平台上，多路径编排器相比 HCCL 将大消息集合通信带宽平均提升 10.4%，并将 Megatron-LM 迭代时间缩短 2.3%–4.6%。

## 英文关键词
Collective communication, PCIe, Multipath communication, Distributed LLM training

## 中文关键词
集合通信，PCIe，多路径通信，分布式 LLM 训练

[返回 Session 14](index.md) · [返回 ATC 2026](../index.md)
