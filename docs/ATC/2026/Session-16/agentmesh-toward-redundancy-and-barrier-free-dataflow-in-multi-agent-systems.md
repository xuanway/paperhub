# AgentMesh: Toward Redundancy- and Barrier-Free Dataflow in Multi-Agent Systems

**中文标题**：AgentMesh：面向多智能体系统的无冗余、无屏障数据流

**所属 Session**：[Session 16: AI Agents](index.md) · [ATC 2026](../index.md)

**作者**：Yuchen Xu (Peking University), Yang Li (Huawei), Yitao Yuan (Peking University), Nengyuan Zhang (Peking University), Yaojing Wang (Huawei), Haoyu You (Peking University), Xiaohan Hou (Peking University), Shaoke Fang (Peking University), Mingrui Liu (Peking University), Mufeng Liu (Peking University), Chen Sun (Huawei), Xia Zhu (Huawei), Bingyang Liu (Huawei), Wenfei Wu (Peking University)

## 英文摘要
Multi-agent systems (MAS) now power long-running agentic applications like deep research and coding agents, yet their end-to-end latency reaches minutes to hours. The runtime executes each dataflow as an opaque, indivisible block at coarse granularity, wasting end-to-end time on redundancy (acquiring content already held or unnecessary) and barriers (a downstream component idling until its upstream input is entirely ready). We abstract a produce–transfer–consume dataflow as a basic unit in MAS, where the producer is a tool or LLM decoding, and the consumer is an LLM prefill. We present AgentMesh, a MAS runtime that optimizes each dataflow with three mechanisms: Delta Tool Retrieval (DTR) shrinks the produce step by serving a tool result’s cached items and fetching only the semantic delta; Branch-Parallel Prefill (BPP) shrinks the consume step by prefilling independent branches in parallel under dependency-graph-derived attention sparsity; Dynamic-Equilibrium Streaming (DES), a dynamic pipeline, overlaps produce, transfer, and consume by pacing streamed chunks to the runtime rate of producer and consumer. Implemented on AutoGen, OpenCode, and vLLM and evaluated across three GPU generations and six models, AgentMesh reduces end-to-end latency by up to 62% with no statistically significant quality loss, on both deep research and coding agent workloads.

## 中文摘要
多智能体系统（MAS）如今支撑着深度研究和编码智能体等长时间运行的智能体应用，但其端到端延迟可达数分钟乃至数小时。运行时以粗粒度将每个数据流当作一个不透明、不可分割的块来执行，把端到端时间浪费在冗余（获取已持有的或不必要的内容）与屏障（下游组件一直空等到上游输入完全就绪）上。我们将“生产—传输—消费”数据流抽象为 MAS 中的基本单元，其中生产者是工具或 LLM 解码，消费者是 LLM 预填充。我们提出 AgentMesh，一个 MAS 运行时，用三种机制优化每个数据流：增量工具检索（DTR）通过直接提供工具结果的缓存条目、仅获取语义增量来缩短生产步骤；分支并行预填充（BPP）在由依赖图推导出的注意力稀疏性下并行预填充相互独立的分支，以缩短消费步骤；动态均衡流式传输（DES）作为一种动态流水线，按照生产者与消费者的运行时速率调节流式分块的节奏，使生产、传输与消费相互重叠。AgentMesh 在 AutoGen、OpenCode 和 vLLM 上实现，并在三代 GPU 和六个模型上评测，在深度研究与编码智能体两类负载上均将端到端延迟最多降低 62%，且无统计显著的质量损失。

## 英文关键词
Agents, Tools, Large Language Model Inference, Multi-Agent Systems

## 中文关键词
智能体，工具，大语言模型推理，多智能体系统

[返回 Session 16](index.md) · [返回 ATC 2026](../index.md)
