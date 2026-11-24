# Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs

**中文标题**：共享 GPU 上无服务器 LLM 服务的能耗感知调度

**所属 Session**：[Session 4: Serverless and Elastic LLM Inference](index.md) · [ATC 2026](../index.md)

**作者**：Tianyu Wang (University of Pittsburgh), Gourav Rattihalli (HPE Labs), Aditya Dhakal (HPE Labs), Longfei Shangguan (University of Pittsburgh & Google), Dejan Milojicic (HPE Labs)

## 英文摘要
As LLM inference becomes a major cloud workload, its growing energy footprint makes cluster-wide energy optimization increasingly important. Serverless LLM serving helps platforms absorb traffic volatility by elastically sharing GPU resources across models, but this sharing also makes energy optimization difficult. Multiple co-resident models run under one device-wide operating point, while their resource demands and latency slack change across execution phases and load conditions. As a result, minimizing energy requires coordinated scheduling across request placement, runtime resource adaptation, and workload consolidation. We present Festina, a profiling-guided, power-aware control plane to minimize cluster-wide energy for serverless LLM serving. Unlike common global–local schedulers that focus on throughput or tail latency, Festina makes energy-first decisions by jointly coordinating request placement, SM partitioning, and GPU operating points under TTFT/TBT SLOs. In our system, a lightweight global scheduler performs fast, SLO-safe, energy-aware placement using constant-time lookups from offline profiles and GPU state summaries. On each GPU, a phase-aware local scheduler continuously adapts task batching and compute resources to minimize power consumption. Festina further performs energy-aware workload consolidation to reduce GPUs’ static power consumption via SLO-aware migration. Comparison with four SOTA LLM serving systems and one DVFS-augmented system demonstrates that Festina reduces energy consumption by up to 56% while maintaining parity in SLO attainment.

## 中文摘要
随着 LLM 推理成为主要的云负载，其不断增长的能耗足迹使得集群级能耗优化愈发重要。无服务器 LLM 服务通过跨模型弹性共享 GPU 资源，帮助平台吸收流量的波动，但这种共享也使能耗优化变得困难。多个共置模型运行在同一个设备级工作点上，而它们的资源需求与延迟余量会在不同执行阶段和负载条件下发生变化。因此，最小化能耗需要在请求放置、运行时资源适配与负载整合之间进行协同调度。我们提出 Festina，一个由性能剖析引导的功耗感知控制平面，用于最小化无服务器 LLM 服务的集群级能耗。与关注吞吐或尾延迟的常见全局-局部调度器不同，Festina 在 TTFT/TBT SLO 约束下联合协调请求放置、SM 划分与 GPU 工作点，从而做出能耗优先的决策。在我们的系统中，轻量级全局调度器利用离线剖析数据和 GPU 状态摘要的常数时间查找，执行快速、SLO 安全且能耗感知的放置。在每个 GPU 上，阶段感知的局部调度器持续调整任务批处理与计算资源，以最小化功耗。Festina 还执行能耗感知的负载整合，通过 SLO 感知的迁移降低 GPU 的静态功耗。与四个 SOTA LLM 服务系统以及一个增强 DVFS 的系统相比，Festina 在保持 SLO 达成率持平的同时将能耗最多降低 56%。

## 英文关键词
energy efficiency, frequency-aware scheduling, LLM inference, GPU multiplexing

## 中文关键词
能效，频率感知调度，LLM 推理，GPU 多路复用

[返回 Session 4](index.md) · [返回 ATC 2026](../index.md)
