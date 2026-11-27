Inferweave: Efficient LLM Inference on the MT-3000 Processor
Authors：
[Xinxin Qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=40200745858085342321)，[Jianbin Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0829996901234782826)，[Peng Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0973160083337316758)，[Yonggang Che](https://63dac.conference-program.com/?post_type=page&p=15&uid=88527177459764354641)

## 中文标题

InferWeave：在 MT-3000 处理器上实现高效 LLM 推理

## 英文摘要

The deployment of large language models (LLMs) is increasingly targeting heterogeneous unified-memory architectures (HUMA) for edge and cost-sensitive computing. However, GPU-centric inference systems perform suboptimally on HUMA due to shared DRAM bandwidth contention and inefficient static operator placement. This paper introduces InferWeave, a bandwidth-aware inference framework that co-designs offline planning and runtime scheduling for HUMA. InferWeave’s offline solver formulates operator placement and data staging as a unified optimization problem with DRAM bandwidth as a first-class constraint. At runtime, a bandwidth-aware asynchronous pipeline scheduler enforces these plans by regulating memory access rates, enabling non-blocking execution across host and device. Evaluated on LLaMA and GPT models using the MT-3000 processor, InferWeave achieves up to 2.3× higher throughput than baselines, demonstrating its effectiveness in enabling efficient LLM inference on integrated architectures.

## 中文摘要

大语言模型（LLM）的部署正日益面向异构统一内存架构（HUMA），以服务于边缘与成本敏感型计算。然而，以 GPU 为中心的推理系统在 HUMA 上表现欠佳，原因在于共享 DRAM 带宽争用与低效的静态算子放置。本文提出 InferWeave，这是一个面向 HUMA 的带宽感知推理框架，对离线规划与运行时调度进行协同设计。InferWeave 的离线求解器将算子放置与数据暂存建模为统一优化问题，并把 DRAM 带宽作为一等约束。在运行时，带宽感知的异步流水线调度器通过调节内存访问速率来落实这些规划，从而实现主机与设备之间的非阻塞执行。在 MT-3000 处理器上使用 LLaMA 与 GPT 模型进行评估，InferWeave 相比基线取得最高 2.3× 的吞吐提升，证明了其在集成架构上实现高效 LLM 推理的有效性。

## 英文关键词

Large Language Models, Inference, Heterogeneous Unified-Memory Architecture (HUMA), MT-3000

## 中文关键词

大语言模型、推理、异构统一内存架构（HUMA）、MT-3000
