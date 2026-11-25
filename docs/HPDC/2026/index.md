---
title: "HPDC 2026 论文集"
description: "HPDC 2026 官方主会议程的 Session 与论文索引。"
---

# HPDC 2026

**HPDC 2026** · 2026年7月13日 - 7月16日 · Cleveland, OH, USA

本索引依据 [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html)整理主会 **12 个 Session、40 篇技术论文**，按官方场次顺序编排。论文标题在官方议程中有简写的，以论文页面收录的完整标题显示。Session 9 中的 ACM SRC presentations、Kizashi Talks、Keynotes、workshops 和其他活动不计入这 40 篇技术论文。

论文页面包含作者、摘要、关键词及 DOI、DBLP 资料链接。以下会议获奖信息均链接至官方来源。

## 获奖信息

- **最佳论文奖**：[Pome: Parallelizing I/Os and Computations for Efficient LSM-tree-based Data Storage](Session-8/pome-parallelizing-i-os-and-computations-for-efficient-lsm-tree-based-data-storage.md)（[官方议程](https://hpdc.sci.utah.edu/2026/program.html)标注 Best Paper Winner）
- **HPDC 成就奖**：Carl Kesselman（[官方获奖页面](https://hpdc.sci.utah.edu/2026/award.html)）

## Session 导航 {#session-nav}

点击 Session 可浏览对应论文、作者与出版链接。

| Session | 中文主题 | Session Chair | 论文数 |
| --- | --- | --- | ---: |
| [Session 1: LLM Inference: Scheduling & Serving](Session-1/index.md) | LLM 推理：调度与服务 | Satish Puri | 3 |
| [Session 2: Scaling Generative Inference](Session-2/index.md) | 扩展生成式推理 | Bogdan Nicolae | 3 |
| [Session 3: MoE Systems & Distributed LLM Training](Session-3/index.md) | MoE 系统与分布式 LLM 训练 | Peter Dinda | 3 |
| [Session 4: Programming Models, Frameworks & Compilers](Session-4/index.md) | 编程模型、框架与编译器 | Dhabaleswar K (DK) Panda | 4 |
| [Session 5: Scientific Applications at Scale](Session-5/index.md) | 大规模科学应用 | Michael Papka | 4 |
| [Session 6: Scientific Data Compression](Session-6/index.md) | 科学数据压缩 | Jay Lofstead | 4 |
| [Session 7: Graph Processing & Community Detection](Session-7/index.md) | 图处理与社区发现 | Dilma Da Silva | 3 |
| [Session 8: Storage & I/O for Data-Intensive Workloads](Session-8/index.md) | 数据密集型负载的存储与 I/O | Sarah Neuwirth | 4 |
| [Session 9: Cloud, Serverless & Microservices](Session-9/index.md) | 云、无服务器与微服务 | Santonu Sarkar | 3 |
| [Session 10: Data Systems for AI & Analytics](Session-10/index.md) | AI 与分析的数据系统 | Xiaoyi Lu | 3 |
| [Session 11: Communication, Workflows & Sustainability](Session-11/index.md) | 通信、工作流与可持续性 | Mehmet Koyuturk | 4 |
| [Session 12: Emerging Generative & Agentic AI Workloads](Session-12/index.md) | 新兴生成式与智能体 AI 负载 | Stefan Andrei | 2 |

## Session 1: LLM Inference: Scheduling & Serving

| English Title | 中文标题 |
| --- | --- |
| [STAR: Decode-Phase Rescheduling for LLM Inference](Session-1/star-decode-phase-rescheduling-for-llm-inference.md) | STAR：面向 LLM 推理的解码阶段重调度 |
| [PKAS: Predictive KVCache-Aware Scheduling for Faster LLM and Transformer Inferences](Session-1/pkas-predictive-kvcache-aware-scheduling-for-faster-llm-and-transformer-inferences.md) | PKAS：预测式 KV Cache 感知调度，加速 LLM 与 Transformer 推理 |
| [Omnia: Efficient RAG Serving through Speculative Scheduling](Session-1/omnia-efficient-rag-serving-through-speculative-scheduling.md) | Omnia：通过推测式调度实现高效 RAG 服务 |

## Session 2: Scaling Generative Inference

| English Title | 中文标题 |
| --- | --- |
| [Scaling Attention Beyond GPUs for LLM Inference](Session-2/scaling-attention-beyond-gpus-for-llm-inference.md) | 超越 GPU 扩展 LLM 推理的注意力计算 |
| [Accelerating Block Low-Rank Foundation Model Inference on Memory-Constrained GPUs](Session-2/accelerating-block-low-rank-foundation-model-inference-on-memory-constrained-gpus.md) | 加速内存受限 GPU 上的分块低秩基础模型推理 |
| [MoE-Lens: Towards the Hardware Limit of High-Throughput MoE LLM Serving Under Resource Constraints](Session-2/moe-lens-towards-the-hardware-limit-of-high-throughput-moe-llm-serving-under-resource-constraints.md) | MoE-Lens：资源受限条件下逼近硬件极限的高吞吐 MoE LLM 服务 |

## Session 3: MoE Systems & Distributed LLM Training

| English Title | 中文标题 |
| --- | --- |
| [UniEP: Unified Expert-Parallel MegaKernel MoE for LLM Training](Session-3/uniep-unified-expert-parallel-megakernel-moe-for-llm-training.md) | UniEP：用于 LLM 训练的统一专家并行 MegaKernel MoE |
| [ResiHP: Taming LLM Training Failures with Dynamic Hybrid Parallelism](Session-3/resihp-taming-llm-training-failures-with-dynamic-hybrid-parallelism.md) | ResiHP：通过动态混合并行应对 LLM 训练故障 |
| [TACO: Efficient Communication Compression of Intermediate Tensors for Scalable Tensor-Parallel LLM Training](Session-3/taco-efficient-communication-compression-of-intermediate-tensors-for-scalable-tensor-parallel-llm-training.md) | TACO：通过高效中间张量通信压缩实现可扩展的张量并行 LLM 训练 |

## Session 4: Programming Models, Frameworks & Compilers

| English Title | 中文标题 |
| --- | --- |
| [SYCL++: A Unified Programming Framework for Heterogeneous Supercomputers at Scale](Session-4/sycl-a-unified-programming-framework-for-heterogeneous-supercomputers-at-scale.md) | SYCL++：面向异构超级计算机的统一编程框架 |
| [Enabling Floating Point Virtualization With Tiny Numbers](Session-4/enabling-floating-point-virtualization-with-tiny-numbers.md) | 使用微小数值实现浮点虚拟化 |
| [FAME: A Framework for Accelerating Independent Multi-Agent Reinforcement Learning on Heterogeneous Platforms](Session-4/fame-a-framework-for-accelerating-independent-multi-agent-reinforcement-learning-on-heterogeneous-platforms.md) | FAME：加速异构平台上独立多智能体强化学习的框架 |
| [CARBS: Compiler Autotuning via Randomized Biased Search](Session-4/carbs-compiler-autotuning-via-randomized-biased-search.md) | CARBS：基于随机偏置搜索的编译器自动调优 |

## Session 5: Scientific Applications at Scale

| English Title | 中文标题 |
| --- | --- |
| [POLAR-PIC: A Holistic Framework for Matrixized PIC with Co-Designed Compute, Layout, and Communication](Session-5/polar-pic-a-holistic-framework-for-matrixized-pic-with-co-designed-compute-layout-and-communication.md) | POLAR-PIC：协同设计计算、数据布局与通信的矩阵化 PIC 整体框架 |
| [A Fully GPU-Accelerated Framework for High-Performance Configuration Interaction Selection with Neural Network Quantum States](Session-5/a-fully-gpu-accelerated-framework-for-high-performance-configuration-interaction-selection-with-neural-network-quantum-states.md) | 基于神经网络量子态的高性能组态相互作用选择 GPU 加速框架 |
| [Full-Core Fluid-Structure-Interaction Simulation of Nuclear Reactor on CPU+GPU Hybrid Clusters](Session-5/full-core-fluid-structure-interaction-simulation-of-nuclear-reactor-on-cpu-gpu-hybrid-clusters.md) | CPU+GPU 混合集群上的核反应堆全堆芯流固耦合模拟 |
| [Endeavor: Efficient PairHMM for Detection of DNA Variants in Genome-Scale Datasets](Session-5/endeavor-efficient-pairhmm-for-detection-of-dna-variants-in-genome-scale-datasets.md) | Endeavor：面向基因组规模 DNA 变异检测的高效 PairHMM |

## Session 6: Scientific Data Compression

| English Title | 中文标题 |
| --- | --- |
| [OPAL: On-demand Progressive Accelerated Scientific Lossy Compression](Session-6/opal-on-demand-progressive-accelerated-scientific-lossy-compression.md) | OPAL：按需渐进式加速科学有损压缩 |
| [TZ: Achieving High-Ratio Scientific Data Compression on GPUs with Global Data Decomposition](Session-6/tz-achieving-high-ratio-scientific-data-compression-on-gpus-with-global-data-decomposition.md) | TZ：通过全局数据分解实现 GPU 上的高压缩比科学数据压缩 |
| [QProR: An Efficient Framework for Quantity-of-Interest Based Progressive Retrieval with Guaranteed Error Control](Session-6/qpror-an-efficient-framework-for-quantity-of-interest-based-progressive-retrieval-with-guaranteed-error-control.md) | QProR：具备误差保证的兴趣量渐进式检索高效框架 |
| [Bridging Information Theory and Practice for Scientific Lossy Compression](Session-6/bridging-information-theory-and-practice-for-scientific-lossy-compression.md) | 打通科学有损压缩的信息论与实践 |

## Session 7: Graph Processing & Community Detection

| English Title | 中文标题 |
| --- | --- |
| [SAGA: State-Aware Graph Analytics for Combinatorial Optimization on Dynamic Graphs](Session-7/saga-state-aware-graph-analytics-for-combinatorial-optimization-on-dynamic-graphs.md) | SAGA：面向动态图组合优化的状态感知图分析 |
| [Efficient Tracking of Communities on Evolving Graphs with Leiden Algorithm](Session-7/efficient-tracking-of-communities-on-evolving-graphs-with-leiden-algorithm.md) | 使用 Leiden 算法高效追踪演化图中的社区 |
| [νMG-LPA and νBM-LPA: Memory Efficient GPU-based Label Propagation Algorithms (LPA) for Community Detection](Session-7/mg-lpa-and-bm-lpa-memory-efficient-gpu-based-label-propagation-algorithms-lpa-for-community-detection.md) | νMG-LPA 与 νBM-LPA：面向社区发现的高内存效率 GPU 标签传播算法 |

## Session 8: Storage & I/O for Data-Intensive Workloads

| English Title | 中文标题 |
| --- | --- |
| [A High-Performance Persistent Transactional Memory System via Cooperative Concurrency Control](Session-8/a-high-performance-persistent-transactional-memory-system-via-cooperative-concurrency-control.md) | 通过协同并发控制实现高性能持久化事务内存系统 |
| [GLANCED-IO: Taming I/O Optimization for Deep Learning at Scale](Session-8/glanced-io-taming-i-o-optimization-for-deep-learning-at-scale.md) | GLANCED-IO：驾驭大规模深度学习中的 I/O 优化 |
| [Merkle-Tree Weight Snapshot Deduplication for Provenance-Aware Auditing of Neural Network Training](Session-8/merkle-tree-weight-snapshot-deduplication-for-provenance-aware-auditing-of-neural-network-training.md) | 面向神经网络训练溯源审计的 Merkle 树权重快照去重 |
| [Pome: Parallelizing I/Os and Computations for Efficient LSM-tree-based Data Storage](Session-8/pome-parallelizing-i-os-and-computations-for-efficient-lsm-tree-based-data-storage.md) | Pome：并行化 I/O 与计算以实现高效的 LSM 树数据存储 |

## Session 9: Cloud, Serverless & Microservices

| English Title | 中文标题 |
| --- | --- |
| [Enabling High-Utilization and Low-Contention FaaS: A Request-Level Resource Provisioning Approach](Session-9/enabling-high-utilization-and-low-contention-faas-a-request-level-resource-provisioning-approach.md) | 实现高利用率与低争用的 FaaS：基于请求级资源配置的方法 |
| [Cremes: Cost-Efficient and Reliable Microservice Execution on Spot Instances](Session-9/cremes-cost-efficient-and-reliable-microservice-execution-on-spot-instances.md) | Cremes：在竞价实例上实现经济高效且可靠的微服务执行 |
| [Krysha: Cost-Efficient Resource Orchestration for Geo-Distributed Serverless Microservices](Session-9/krysha-cost-efficient-resource-orchestration-for-geo-distributed-serverless-microservices.md) | Krysha：面向地理分布式无服务器微服务的经济高效资源编排 |

## Session 10: Data Systems for AI & Analytics

| English Title | 中文标题 |
| --- | --- |
| [SIVF: GPU-Resident IVF Index for Streaming Vector Analytics](Session-10/sivf-gpu-resident-ivf-index-for-streaming-vector-analytics.md) | SIVF：面向流式向量分析的 GPU 驻留式 IVF 索引 |
| [BCCE: Block-Centric GPU Co-Design for Real-Time Range-Top-K Query at Scale](Session-10/bcce-block-centric-gpu-co-design-for-real-time-range-top-k-query-at-scale.md) | BCCE：面向大规模实时 Range-Top-K 查询的块中心 GPU 协同设计 |
| [ATLAS: Efficient Out-of-Core Inference for Billion-Scale Graph Neural Networks](Session-10/atlas-efficient-out-of-core-inference-for-billion-scale-graph-neural-networks.md) | ATLAS：面向十亿级图神经网络的高效外存推理 |

## Session 11: Communication, Workflows & Sustainability

| English Title | 中文标题 |
| --- | --- |
| [GICC: A High-Performance Runtime for GPU-Initiated Communication and Coordination in Modern HPC Systems](Session-11/gicc-a-high-performance-runtime-for-gpu-initiated-communication-and-coordination-in-modern-hpc-systems.md) | GICC：面向现代 HPC 系统的 GPU 发起式通信与协调高性能运行时 |
| [When RDMA Goes Long-Haul: Characterization, Modeling, and Verbs-Level Emulation with Implications for Federated Learning](Session-11/when-rdma-goes-long-haul-characterization-modeling-and-verbs-level-emulation-with-implications-for-federated-learning.md) | RDMA 远距离传输：特征分析、建模与 Verbs 级仿真及其对联邦学习的启示 |
| [JANUS: Resilient and Adaptive Data Transmission for Enabling Timely and Efficient Cross-Facility Scientific Workflows](Session-11/janus-resilient-and-adaptive-data-transmission-for-enabling-timely-and-efficient-cross-facility-scientific-workflows.md) | JANUS：通过弹性自适应数据传输实现及时高效的跨设施科学工作流 |
| [PowerQuant: Architecture-Agnostic GPU Power Estimation via Quantile Regression](Session-11/powerquant-architecture-agnostic-gpu-power-estimation-via-quantile-regression.md) | PowerQuant：基于分位数回归的架构无关 GPU 功耗估算 |

## Session 12: Emerging Generative & Agentic AI Workloads

| English Title | 中文标题 |
| --- | --- |
| [DiTango: Cost-Effective Parallel Diffusion Generation with Selective Attention State Reuse](Session-12/ditango-cost-effective-parallel-diffusion-generation-with-selective-attention-state-reuse.md) | DiTango：通过选择性复用注意力状态实现经济高效的并行扩散生成 |
| [Dynamo-MoE: Accelerating Sparse Large Model Inference with Dynamic Parallelization](Session-12/dynamo-moe-accelerating-sparse-large-model-inference-with-dynamic-parallelization.md) | Dynamo-MoE：通过动态并行加速稀疏大模型推理 |
