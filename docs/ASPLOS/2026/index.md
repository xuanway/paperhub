---
title: "ASPLOS 2026 论文集"
description: "ASPLOS 2026 Detailed Program 全部 36 个论文 Session、168 条论文日程记录的中英文索引与摘要。"
tags:
  - "ASPLOS2026"
  - "Computer Architecture"
  - "Programming Languages"
  - "Operating Systems"
---

# ASPLOS 2026

本页按 [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html) 整理全部 **36 个论文 Session、168 条论文日程记录**。每篇论文页包含中英文题名、摘要、关键词、作者与单位、论文 DOI 和出版卷号，并收录已核实的代码或研究制品链接。

会议于 **2026 年 3 月 22–26 日**在美国宾夕法尼亚州匹兹堡举行，论文宣讲安排在 **3 月 24–26 日**。各 Session 页保留具体时间、地点、主持人与作者单位统计。

> **统计口径：** 官方 Program Overview 标注 “167 unique papers”，而 Detailed Program 对应 168 条论文日程记录，两处数量存在差异。本目录按 Detailed Program 逐条整理；文中的 168 指日程条目/页面数，不代表官方确认的唯一论文数。

## Session 导航

| Session | 中文主题 | 论文数 |
| --- | --- | ---: |
| [Session 1A: LLM Serving: Throughput Optimization](Session-1A/index.md) | 大语言模型服务：吞吐量优化 | 5 |
| [Session 1B: LLM Serving: Latency & Scheduling](Session-1B/index.md) | 大语言模型服务：延迟与调度 | 5 |
| [Session 1C: Quantum Computing: Compilation](Session-1C/index.md) | 量子计算：编译 | 5 |
| [Session 1D: CXL & Memory Fabric](Session-1D/index.md) | CXL 与内存互连 | 5 |
| [Session 2A: LLM Training Systems](Session-2A/index.md) | 大语言模型训练系统 | 5 |
| [Session 2B: Speculative Decoding](Session-2B/index.md) | 推测解码 | 5 |
| [Session 2C: GPU Systems & Scheduling](Session-2C/index.md) | GPU 系统与调度 | 5 |
| [Session 2D: DRAM Reliability & Security](Session-2D/index.md) | DRAM 可靠性与安全 | 5 |
| [Session 3A: LLM Attention & KV Cache](Session-3A/index.md) | 大语言模型注意力与 KV 缓存 | 5 |
| [Session 3B: Mixture-of-Experts & Efficient Inference](Session-3B/index.md) | 混合专家与高效推理 | 5 |
| [Session 3C: 3D Gaussian Splatting & Rendering](Session-3C/index.md) | 三维高斯泼溅与渲染 | 5 |
| [Session 3D: Trusted Execution Environments](Session-3D/index.md) | 可信执行环境 | 5 |
| [Session 4A: ML Training & Monitoring](Session-4A/index.md) | 机器学习训练与监测 | 5 |
| [Session 4B: ML Compilers & Tensor Programs](Session-4B/index.md) | 机器学习编译器与张量程序 | 5 |
| [Session 4C: Quantum Error Correction](Session-4C/index.md) | 量子纠错 | 5 |
| [Session 4D: Processing-in-Memory](Session-4D/index.md) | 存内处理 | 5 |
| [Session 5A: Generative Model Serving](Session-5A/index.md) | 生成式模型服务 | 5 |
| [Session 5B: On-Device & Edge AI](Session-5B/index.md) | 端侧与边缘人工智能 | 5 |
| [Session 5C: Formal Verification](Session-5C/index.md) | 形式化验证 | 5 |
| [Session 5D: Storage & Caching](Session-5D/index.md) | 存储与缓存 | 5 |
| [Session 6A: Neural Network Acceleration](Session-6A/index.md) | 神经网络加速 | 5 |
| [Session 6B: Hardware Design Languages](Session-6B/index.md) | 硬件设计语言 | 5 |
| [Session 6C: Graph & Sparse Computing](Session-6C/index.md) | 图计算与稀疏计算 | 5 |
| [Session 6D: Disaggregated Memory Systems](Session-6D/index.md) | 解耦内存系统 | 5 |
| [Session 7A: Fully Homomorphic Encryption](Session-7A/index.md) | 全同态加密 | 4 |
| [Session 7B: Compilers & Code Generation](Session-7B/index.md) | 编译器与代码生成 | 4 |
| [Session 7C: Testing & Fuzzing](Session-7C/index.md) | 测试与模糊测试 | 4 |
| [Session 7D: Processor Microarchitecture](Session-7D/index.md) | 处理器微架构 | 4 |
| [Session 8A: GPU Programming](Session-8A/index.md) | GPU 编程 | 4 |
| [Session 8B: Serverless & Cloud Networking](Session-8B/index.md) | 无服务器计算与云网络 | 4 |
| [Session 8C: Memory Hierarchy & Performance](Session-8C/index.md) | 内存层次结构与性能 | 4 |
| [Session 8D: Reconfigurable Architectures](Session-8D/index.md) | 可重构架构 | 4 |
| [Session 9A: Systems Profiling & Optimization](Session-9A/index.md) | 系统性能剖析与优化 | 4 |
| [Session 9B: Quantum & Emerging Computing](Session-9B/index.md) | 量子计算与新型计算 | 4 |
| [Session 9C: Reliability & Fault Tolerance](Session-9C/index.md) | 可靠性与容错 | 4 |
| [Session 9D: Network & Cloud Infrastructure](Session-9D/index.md) | 网络与云基础设施 | 4 |

## Session 1A: LLM Serving: Throughput Optimization

**中文主题：** 大语言模型服务：吞吐量优化

| 英文标题 | 中文标题 |
| --- | --- |
| [Towards High-Goodput LLM Serving with Prefill-decode Multiplexing](Session-1A/towards-high-goodput-llm-serving-with-prefill-decode-multiplexing.md) | 面向预填充-解码多路复用的高有效吞吐 LLM 服务 |
| [Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration](Session-1A/bullet-boosting-gpu-utilization-for-llm-serving-via-dynamic-spatial-temporal-orchestration.md) ([code](https://github.com/zejia-lin/BulletServe)) | Bullet：通过动态时空编排提升 LLM 服务中的 GPU 利用率 |
| [QoServe: Breaking the Silos of LLM Inference Serving](Session-1A/qoserve-breaking-the-silos-of-llm-inference-serving.md) | QoServe：打破 LLM 推理服务的孤岛 |
| [Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads](Session-1A/shift-parallelism-low-latency-high-throughput-llm-inference-for-dynamic-workloads.md) | Shift Parallelism：面向动态工作负载的低延迟、高吞吐 LLM 推理 |
| [XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads](Session-1A/xy-serve-end-to-end-versatile-production-serving-for-dynamic-llm-workloads.md) | XY-Serve：面向动态 LLM 工作负载的端到端通用型生产服务系统 |

## Session 1B: LLM Serving: Latency & Scheduling

**中文主题：** 大语言模型服务：延迟与调度

| 英文标题 | 中文标题 |
| --- | --- |
| [PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel](Session-1B/pat-accelerating-llm-decoding-via-prefix-aware-attention-with-resource-efficient-multi-tile-kernel.md) | PAT：通过前缀感知注意力与资源高效的多 Tile 内核加速 LLM 解码 |
| [ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression](Session-1B/zipserv-fast-and-memory-efficient-llm-inference-with-hardware-aware-lossless-compression.md) | ZipServ：基于硬件感知无损压缩的快速、内存高效的 LLM 推理 |
| [BlendServe: Optimizing Offline Inference with Resource-Aware Batching](Session-1B/blendserve-optimizing-offline-inference-with-resource-aware-batching.md) | BlendServe：以资源感知批处理优化离线推理 |
| [BAT: Efficient Generative Recommender Serving with Bipartite Attention](Session-1B/bat-efficient-generative-recommender-serving-with-bipartite-attention.md) | BAT：基于二分注意力的高效生成式推荐服务 |
| [MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading](Session-1B/moe-apex-an-efficient-moe-inference-system-with-adaptive-precision-expert-offloading.md) | MoE-APEX：一种采用自适应精度专家卸载的高效 MoE 推理系统 |

## Session 1C: Quantum Computing: Compilation

**中文主题：** 量子计算：编译

| 英文标题 | 中文标题 |
| --- | --- |
| [PowerMove: Optimizing Compilation for Neutral Atom Quantum Computers with Zoned Architecture](Session-1C/powermove-optimizing-compilation-for-neutral-atom-quantum-computers-with-zoned-architecture.md) | PowerMove：面向分区架构中性原子量子计算机的优化编译 |
| [Reconfigurable Quantum Instruction Set Computers for High Performance Attainable on Hardware](Session-1C/reconfigurable-quantum-instruction-set-computers-for-high-performance-attainable-on-hardware.md) | 面向硬件上可达成高性能的可重构量子指令集计算机 |
| [QTurbo: A Robust and Efficient Compiler for Analog Quantum Simulation](Session-1C/qturbo-a-robust-and-efficient-compiler-for-analog-quantum-simulation.md) | QTurbo：面向模拟量子模拟的鲁棒且高效的编译器 |
| [Reducing T Gates with Unitary Synthesis](Session-1C/reducing-t-gates-with-unitary-synthesis.md) | 利用酉综合减少 T 门 |
| [Borrowing Dirty Qubits in Quantum Programs](Session-1C/borrowing-dirty-qubits-in-quantum-programs.md) | 在量子程序中借用脏量子比特 |

## Session 1D: CXL & Memory Fabric

**中文主题：** CXL 与内存互连

| 英文标题 | 中文标题 |
| --- | --- |
| [HybridTier: An Adaptive and Lightweight CXL-Memory Tiering System](Session-1D/hybridtier-an-adaptive-and-lightweight-cxl-memory-tiering-system.md) | HybridTier：一种自适应且轻量级的 CXL 内存分层系统 |
| [vCXLGen: Automated Synthesis and Verification of CXL Bridges for Heterogeneous Architectures](Session-1D/vcxlgen-automated-synthesis-and-verification-of-cxl-bridges-for-heterogeneous-architectures.md) | vCXLGen：面向异构架构的 CXL 桥自动综合与验证 |
| [CXLMC: Model Checking CXL Shared Memory Programs](Session-1D/cxlmc-model-checking-cxl-shared-memory-programs.md) | CXLMC：CXL 共享内存程序的模型检测 |
| [A Programming Model for Disaggregated Memory over CXL](Session-1D/a-programming-model-for-disaggregated-memory-over-cxl.md) | 面向 CXL 分离式内存的编程模型 |
| [Cxlalloc: Safe and Efficient Memory Allocation for a CXL Pod](Session-1D/cxlalloc-safe-and-efficient-memory-allocation-for-a-cxl-pod.md) | Cxlalloc：面向 CXL Pod 的安全高效内存分配 |

## Session 2A: LLM Training Systems

**中文主题：** 大语言模型训练系统

| 英文标题 | 中文标题 |
| --- | --- |
| [SNIP: An Adaptive Mixed Precision Framework for Subbyte Large Language Model Training](Session-2A/snip-an-adaptive-mixed-precision-framework-for-subbyte-large-language-model-training.md) | SNIP：面向亚字节大语言模型训练的自适应混合精度框架 |
| [Fine-grained and Non-intrusive LLM Training Monitoring via Microsecond-level Traffic Measurement](Session-2A/fine-grained-and-non-intrusive-llm-training-monitoring-via-microsecond-level-traffic-measurement.md) | 基于微秒级流量测量的细粒度且非侵入式 LLM 训练监控 |
| [SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips](Session-2A/superoffload-unleashing-the-power-of-large-scale-llm-training-on-superchips.md) | SuperOffload：在超级芯片上释放大规模 LLM 训练的能力 |
| [DIP: Efficient Large Multimodal Model Training with Dynamic Interleaved Pipeline](Session-2A/dip-efficient-large-multimodal-model-training-with-dynamic-interleaved-pipeline.md) | DIP：基于动态交错流水线的高效大型多模态模型训练 |
| [Dynamic Sparsity in Large-Scale Video DiT Training](Session-2A/dynamic-sparsity-in-large-scale-video-dit-training.md) | 大规模视频 DiT 训练中的动态稀疏性 |

## Session 2B: Speculative Decoding

**中文主题：** 推测解码

| 英文标题 | 中文标题 |
| --- | --- |
| [DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU](Session-2B/dfvg-a-heterogeneous-architecture-for-speculative-decoding-with-draft-on-fpga-and-verify-on-gpu.md) | DFVG：一种采用 FPGA 起草与 GPU 验证的投机解码异构架构 |
| [SwiftSpec: Disaggregated Speculative Decoding and Fused Kernels for Low-Latency LLM Inference](Session-2B/swiftspec-disaggregated-speculative-decoding-and-fused-kernels-for-low-latency-llm-inference.md) | SwiftSpec：面向低延迟 LLM 推理的解聚式投机解码与融合内核 |
| [SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs](Session-2B/specontext-enabling-efficient-long-context-reasoning-with-speculative-context-sparsity-in-llms.md) | SpeContext：在 LLM 中以投机式上下文稀疏性实现高效长上下文推理 |
| [SpecProto: A Parallelizing Compiler for Speculative Decoding of Large Protocol Buffers Data](Session-2B/specproto-a-parallelizing-compiler-for-speculative-decoding-of-large-protocol-buffers-data.md) | SpecProto：一种面向大规模 Protocol Buffers 数据投机解码的并行化编译器 |
| [EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse](Session-2B/earth-an-efficient-moe-accelerator-with-entropy-aware-speculative-prefetch-and-result-reuse.md) | EARTH：一种具有熵感知投机预取与结果复用的高效 MoE 加速器 |

## Session 2C: GPU Systems & Scheduling

**中文主题：** GPU 系统与调度

| 英文标题 | 中文标题 |
| --- | --- |
| [gShare: Efficient GPU Sharing with Aggressive Scheduling in Multi-tenant FaaS platform](Session-2C/gshare-efficient-gpu-sharing-with-aggressive-scheduling-in-multi-tenant-faas-platform.md) | gShare：多租户 FaaS 平台中采用激进调度的高效 GPU 共享 |
| [GFS: A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management](Session-2C/gfs-a-preemption-aware-scheduling-framework-for-gpu-clusters-with-predictive-spot-instance-management.md) | GFS：面向 GPU 集群的抢占感知调度框架，具备预测性竞价实例管理 |
| [Asynchrony and GPUs: Bridging this Dichotomy for I/O with AGIO](Session-2C/asynchrony-and-gpus-bridging-this-dichotomy-for-i-o-with-agio.md) | 异步与 GPU：以 AGIO 弥合 I/O 中的这一二分对立 |
| [MSCCL++: Rethinking GPU Communication Abstractions for AI Inference](Session-2C/msccl-rethinking-gpu-communication-abstractions-for-ai-inference.md) ([code](https://github.com/microsoft/mscclpp)) | MSCCL++：为 AI 推理重新思考 GPU 通信抽象 |
| [Insum: Sparse GPU Kernels Simplified and Optimized with Indirect Einsums](Session-2C/insum-sparse-gpu-kernels-simplified-and-optimized-with-indirect-einsums.md) | Insum：用间接 Einsum 简化并优化稀疏 GPU 内核 |

## Session 2D: DRAM Reliability & Security

**中文主题：** DRAM 可靠性与安全

| 英文标题 | 中文标题 |
| --- | --- |
| [RowArmor: Efficient and Comprehensive Protection Against DRAM Disturbance Errors](Session-2D/rowarmor-efficient-and-comprehensive-protection-against-dram-disturbance-errors.md) | RowArmor：高效且全面的 DRAM 干扰错误防护 |
| [APT: Securing Against DRAM Read Disturbance via Adaptive Probabilistic In-DRAM Trackers](Session-2D/apt-securing-against-dram-read-disturbance-via-adaptive-probabilistic-in-dram-trackers.md) | APT：通过自适应概率式 DRAM 内跟踪器防御 DRAM 读干扰 |
| [STRAW: Stress-Aware WL-Based Read Disturbance Management for High-Density NAND Flash Memory](Session-2D/straw-stress-aware-wl-based-read-disturbance-management-for-high-density-nand-flash-memory.md) | STRAW：面向高密度 NAND 闪存的压力感知、基于字线的读干扰管理 |
| [Trust-V: Toward Secure and Reliable Storage for Trusted Execution Environments](Session-2D/trust-v-toward-secure-and-reliable-storage-for-trusted-execution-environments.md) | Trust-V：面向可信执行环境的安全可靠存储 |
| [Optimizer-Friendly Instrumentation for Event Quantification with PRUE Algorithm](Session-2D/optimizer-friendly-instrumentation-for-event-quantification-with-prue-algorithm.md) | 基于 PRUE 算法的事件量化优化器友好插桩 |

## Session 3A: LLM Attention & KV Cache

**中文主题：** 大语言模型注意力与 KV 缓存

| 英文标题 | 中文标题 |
| --- | --- |
| [I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention](Session-3A/i-o-analysis-is-all-you-need-an-i-o-analysis-for-long-sequence-attention.md) | I/O 分析即所需：面向长序列注意力机制的 I/O 分析 |
| [REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing](Session-3A/repa-reconfigurable-pim-for-the-joint-acceleration-of-kv-cache-offloading-and-processing.md) | REPA：面向 KV 缓存卸载与处理联合加速的可重构 PIM |
| [STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems](Session-3A/starc-selective-token-access-with-remapping-and-clustering-for-efficient-llm-decoding-on-pim-systems.md) | STARC：面向 PIM 系统上高效 LLM 解码的带重映射与聚类的选择性 token 访问 |
| [Mugi: Value Level Parallelism For Efficient LLMs](Session-3A/mugi-value-level-parallelism-for-efficient-llms.md) | Mugi：面向高效 LLM 的值级并行 |
| [TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference](Session-3A/tpla-tensor-parallel-latent-attention-for-efficient-disaggregated-prefill-decode-inference.md) | TPLA：面向高效分离式 Prefill 与 Decode 推理的张量并行潜在注意力 |

## Session 3B: Mixture-of-Experts & Efficient Inference

**中文主题：** 混合专家与高效推理

| 英文标题 | 中文标题 |
| --- | --- |
| [LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training](Session-3B/laer-moe-load-adaptive-expert-re-layout-for-efficient-mixture-of-experts-training.md) | LAER-MoE：面向高效混合专家训练的自适应负载专家重布局 |
| [oFFN: Outlier and Neuron-aware Structured FFN for Fast yet Accurate LLM Inference](Session-3B/offn-outlier-and-neuron-aware-structured-ffn-for-fast-yet-accurate-llm-inference.md) | oFFN：面向快速且准确的 LLM 推理的离群值与神经元感知结构化 FFN |
| [MoDM: Efficient Serving for Image Generation via Mixture-of-Diffusion Models](Session-3B/modm-efficient-serving-for-image-generation-via-mixture-of-diffusion-models.md) | MoDM：基于扩散模型混合的高效图像生成服务 |
| [Taming the Long-Tail: Efficient Reasoning RL Training with Adaptive Drafter](Session-3B/taming-the-long-tail-efficient-reasoning-rl-training-with-adaptive-drafter.md) | 驯服长尾：基于自适应草稿模型的高效推理强化学习训练 |
| [FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning](Session-3B/fasttts-accelerating-test-time-scaling-for-edge-llm-reasoning.md) | FastTTS：加速边缘 LLM 推理的测试时扩展 |

## Session 3C: 3D Gaussian Splatting & Rendering

**中文主题：** 三维高斯泼溅与渲染

| 英文标题 | 中文标题 |
| --- | --- |
| [GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading](Session-3C/gs-scale-unlocking-large-scale-3d-gaussian-splatting-training-via-host-offloading.md) | GS-Scale：通过主机卸载释放大规模 3D 高斯泼溅训练 |
| [Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration](Session-3C/neo-real-time-on-device-3d-gaussian-splatting-with-reuse-and-update-sorting-acceleration.md) | Neo：基于复用与更新排序加速的实时端侧 3D 高斯泼溅 |
| [CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](Session-3C/clm-removing-the-gpu-memory-barrier-for-3d-gaussian-splatting.md) | CLM：消除 3D 高斯泼溅的 GPU 内存壁垒 |
| [Nebula: Infinite-Scale 3D Gaussian Splatting in VR via Collaborative Rendering and Accelerated Stereo Rasterization](Session-3C/nebula-infinite-scale-3d-gaussian-splatting-in-vr-via-collaborative-rendering-and-accelerated-stereo-rasterization.md) ([code](https://github.com/SJTU-MVCLab/Nebula)) ([website](https://stonesix16.github.io/Nebula/)) | Nebula：通过协同渲染与加速立体光栅化在 VR 中实现无限规模 3D 高斯泼溅 |
| [AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame Covisibility Detection](Session-3C/ags-accelerating-3d-gaussian-splatting-slam-via-codec-assisted-frame-covisibility-detection.md) | AGS：通过 CODEC 辅助的帧共视检测加速 3D 高斯泼溅 SLAM |

## Session 3D: Trusted Execution Environments

**中文主题：** 可信执行环境

| 英文标题 | 中文标题 |
| --- | --- |
| [Detecting Inconsistencies in ARM CCA’s Formally Verified Specification](Session-3D/detecting-inconsistencies-in-arm-cca-s-formally-verified-specification.md) | 检测 ARM CCA 形式化验证规范中的不一致性 |
| [WorksetEnclave: Towards Optimizing Cold Starts in Confidential Serverless with Workset-Based Enclave Restore](Session-3D/worksetenclave-towards-optimizing-cold-starts-in-confidential-serverless-with-workset-based-enclave-restore.md) | WorksetEnclave：面向基于工作集的 enclave 恢复优化机密无服务器中的冷启动 |
| [TEEM³: Core-Independent and Cooperating Trusted Execution Environments](Session-3D/teem3-core-independent-and-cooperating-trusted-execution-environments.md) | TEEM³：核无关且可协作的可信执行环境 |
| [WAVE: Leveraging Architecture Observation for Privacy-Preserving Model Oversight](Session-3D/wave-leveraging-architecture-observation-for-privacy-preserving-model-oversight.md) | WAVE：利用架构观测实现隐私保护下的模型监管 |
| [Compass: Navigating the Design Space of Taint Schemes for RTL Security Verification](Session-3D/compass-navigating-the-design-space-of-taint-schemes-for-rtl-security-verification.md) | Compass：导航 RTL 安全验证的污点方案设计空间 |

## Session 4A: ML Training & Monitoring

**中文主题：** 机器学习训练与监测

| 英文标题 | 中文标题 |
| --- | --- |
| [T-Control: An Efficient Dynamic Tensor Rematerialization System for DNN Training](Session-4A/t-control-an-efficient-dynamic-tensor-rematerialization-system-for-dnn-training.md) | T-Control：一个面向 DNN 训练的高效动态张量重计算系统 |
| [NotebookOS: A Replicated Notebook Platform for Interactive Training with On-Demand GPUs](Session-4A/notebookos-a-replicated-notebook-platform-for-interactive-training-with-on-demand-gpus.md) | NotebookOS：一个面向按需 GPU 交互式训练的复制笔记本平台 |
| [DeepContext: A Context-aware, Cross-platform, and Cross-framework Tool for Performance Profiling and Analysis of Deep Learning Workloads](Session-4A/deepcontext-a-context-aware-cross-platform-and-cross-framework-tool-for-performance-profiling-and-analysis-of-deep-learning-workloads.md) | DeepContext：一个面向深度学习工作负载性能剖析与分析的上下文感知、跨平台、跨框架工具 |
| [Triton-Sanitizer: A Fast and Device-Agnostic Memory Sanitizer for Triton with Rich Diagnostic Context](Session-4A/triton-sanitizer-a-fast-and-device-agnostic-memory-sanitizer-for-triton-with-rich-diagnostic-context.md) ([code](https://doi.org/10.5281/zenodo.17925531)) | Triton-Sanitizer：一个面向 Triton 的快速、设备无关且具备丰富诊断上下文的内存检查器 |
| [LAIKA: Machine Learning-Assisted In-Kernel APU Acceleration](Session-4A/laika-machine-learning-assisted-in-kernel-apu-acceleration.md) | LAIKA：机器学习辅助的内核内 APU 加速 |

## Session 4B: ML Compilers & Tensor Programs

**中文主题：** 机器学习编译器与张量程序

| 英文标题 | 中文标题 |
| --- | --- |
| [FuseFlow: A Fusion-Centric Compilation Framework for Sparse Deep Learning on Streaming Dataflow](Session-4B/fuseflow-a-fusion-centric-compilation-framework-for-sparse-deep-learning-on-streaming-dataflow.md) | FuseFlow：面向流式数据流的稀疏深度学习融合式编译框架 |
| [Trinity: Three-Dimensional Tensor Program Optimization via Tile-level Equality Saturation](Session-4B/trinity-three-dimensional-tensor-program-optimization-via-tile-level-equality-saturation.md) | Trinity：通过 Tile 级等式饱和实现的三维张量程序优化 |
| [RedFuser: An Automatic Operator Fusion Framework for Cascaded Reductions on AI Accelerators](Session-4B/redfuser-an-automatic-operator-fusion-framework-for-cascaded-reductions-on-ai-accelerators.md) | RedFuser：面向 AI 加速器上级联归约的自动算子融合框架 |
| [Linear Layouts: Robust Code Generation of Efficient Tensor Computation Using F2](Session-4B/linear-layouts-robust-code-generation-of-efficient-tensor-computation-using-f2.md) | Linear Layouts：使用 F2 实现高效张量计算的健壮代码生成 |
| [Streaming Tensor Program: A streaming abstraction for dynamic parallelism](Session-4B/streaming-tensor-program-a-streaming-abstraction-for-dynamic-parallelism.md) | Streaming Tensor Program：面向动态并行的流式抽象 |

## Session 4C: Quantum Error Correction

**中文主题：** 量子纠错

| 英文标题 | 中文标题 |
| --- | --- |
| [AlphaSyndrome: Tackling the Syndrome Measurement Circuit Scheduling Problem for QEC Codes](Session-4C/alphasyndrome-tackling-the-syndrome-measurement-circuit-scheduling-problem-for-qec-codes.md) | AlphaSyndrome：应对 QEC 码的校验子测量电路调度问题 |
| [PropHunt: Automated Optimization of Quantum Syndrome Measurement Circuits](Session-4C/prophunt-automated-optimization-of-quantum-syndrome-measurement-circuits.md) | PropHunt：量子校验子测量电路的自动化优化 |
| [iSwitch: QEC on Demand via In-Situ Encoding of Bare Qubits for Ion Trap Architectures](Session-4C/iswitch-qec-on-demand-via-in-situ-encoding-of-bare-qubits-for-ion-trap-architectures.md) | iSwitch：面向离子阱架构、通过裸量子比特原位编码实现按需 QEC |
| [Architecting Scalable Trapped Ion Quantum Computers using Surface Codes](Session-4C/architecting-scalable-trapped-ion-quantum-computers-using-surface-codes.md) | 使用表面码架构可扩展的囚禁离子量子计算机 |
| [Accelerating Computation in Quantum LDPC Code](Session-4C/accelerating-computation-in-quantum-ldpc-code.md) | 加速量子 LDPC 码中的计算 |

## Session 4D: Processing-in-Memory

**中文主题：** 存内处理

| 英文标题 | 中文标题 |
| --- | --- |
| [DARTH-PUM: A Hybrid Processing-Using-Memory Architecture](Session-4D/darth-pum-a-hybrid-processing-using-memory-architecture.md) | DARTH-PUM：一种混合的存内处理架构 |
| [PUSHtap: PIM-based In-Memory HTAP with Unified Data Storage Format](Session-4D/pushtap-pim-based-in-memory-htap-with-unified-data-storage-format.md) | PUSHtap：基于 PIM 的统一数据存储格式内存 HTAP 系统 |
| [CoGraf: Fully Accelerating Graph Applications with Fine-Grained PIM](Session-4D/cograf-fully-accelerating-graph-applications-with-fine-grained-pim.md) | CoGraf：以细粒度 PIM 全面加速图应用 |
| [Ouroboros: Wafer-Scale SRAM CIM with Token-Grained Pipelining for Large Language Model Inference](Session-4D/ouroboros-wafer-scale-sram-cim-with-token-grained-pipelining-for-large-language-model-inference.md) | Ouroboros：用于大语言模型推理的晶圆级 SRAM CIM 与令牌粒度流水线 |
| [A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs](Session-4D/a-cost-effective-near-storage-processing-solution-for-offline-inference-of-long-context-llms.md) | 面向长上下文 LLM 离线推理的高性价比近存储处理方案 |

## Session 5A: Generative Model Serving

**中文主题：** 生成式模型服务

| 英文标题 | 中文标题 |
| --- | --- |
| [TetriServe: Efficiently Serving Mixed DiT Workloads](Session-5A/tetriserve-efficiently-serving-mixed-dit-workloads.md) | TetriServe：高效服务混合 DiT 工作负载 |
| [Segment Only Where You Look: Leveraging Human Gaze Behavior for Efficient Computer Vision Applications in Augmented Reality](Session-5A/segment-only-where-you-look-leveraging-human-gaze-behavior-for-efficient-computer-vision-applications-in-augmented-reality.md) | 只在你注视之处分割：利用人类注视行为实现增强现实中高效的计算机视觉应用 |
| [Compositional AI Beyond LLMs: System Implications of Neuro-Symbolic-Probabilistic Architectures](Session-5A/compositional-ai-beyond-llms-system-implications-of-neuro-symbolic-probabilistic-architectures.md) | 超越 LLM 的组合式 AI：神经-符号-概率架构的系统影响 |
| [It Takes Two to Entangle](Session-5A/it-takes-two-to-entangle.md) | 纠缠需要双方 |
| [Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation](Session-5A/tilus-a-tile-level-gpgpu-programming-language-for-low-precision-computation.md) ([code](https://github.com/NVIDIA/tilus)) | Tilus：面向低精度计算的 Tile 级 GPGPU 编程语言 |

## Session 5B: On-Device & Edge AI

**中文主题：** 端侧与边缘人工智能

| 英文标题 | 中文标题 |
| --- | --- |
| [Neuralink: Fast on-Device LLM Inference with Neuron Co-Activation Linking](Session-5B/neuralink-fast-on-device-llm-inference-with-neuron-co-activation-linking.md) | Neuralink：利用神经元共激活链接实现快速的端侧 LLM 推理 |
| [Lifetime-Aware Design for Item-Level Intelligence at the Extreme Edge](Session-5B/lifetime-aware-design-for-item-level-intelligence-at-the-extreme-edge.md) | 面向极致边缘物品级智能的生命周期感知设计 |
| [FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations](Session-5B/flashmem-supporting-modern-dnn-workloads-on-mobile-with-gpu-memory-hierarchy-optimizations.md) | FlashMem：通过 GPU 内存层次优化在移动端支持现代 DNN 工作负载 |
| [ASDR: Exploiting Adaptive Sampling and Data Reuse for CIM-based Instant Neural Rendering](Session-5B/asdr-exploiting-adaptive-sampling-and-data-reuse-for-cim-based-instant-neural-rendering.md) | ASDR：利用自适应采样与数据复用实现基于 CIM 的即时神经渲染 |
| [BitRed: Taming Non-Uniform Bit-Level Sparsity with a Programmable RISC-V ISA for DNN Acceleration](Session-5B/bitred-taming-non-uniform-bit-level-sparsity-with-a-programmable-risc-v-isa-for-dnn-acceleration.md) | BitRed：以可编程 RISC-V ISA 驾驭非均匀位级稀疏性实现 DNN 加速 |

## Session 5C: Formal Verification

**中文主题：** 形式化验证

| 英文标题 | 中文标题 |
| --- | --- |
| [Graphiti: Formally Verified Out-of-Order Execution in Dataflow Circuits](Session-5C/graphiti-formally-verified-out-of-order-execution-in-dataflow-circuits.md) | Graphiti：数据流电路中经形式化验证的乱序执行 |
| [Highly Automated Verification of Security Properties for Unmodified System Software](Session-5C/highly-automated-verification-of-security-properties-for-unmodified-system-software.md) | 面向未经修改的系统软件的安全属性高度自动化验证 |
| [SylQ-SV: Scaling Symbolic Execution of Hardware Designs with Query Caching](Session-5C/sylq-sv-scaling-symbolic-execution-of-hardware-designs-with-query-caching.md) | SylQ-SV：利用查询缓存扩展硬件设计的符号执行 |
| [Once-for-All: Skeleton-Guided SMT Solver Fuzzing with LLM-Synthesized Generators](Session-5C/once-for-all-skeleton-guided-smt-solver-fuzzing-with-llm-synthesized-generators.md) | Once-for-All：基于骨架引导、以 LLM 合成生成器驱动的 SMT 求解器模糊测试 |
| [LPO: Discovering Missed Peephole Optimizations with Large Language Models](Session-5C/lpo-discovering-missed-peephole-optimizations-with-large-language-models.md) | LPO：用大语言模型发现被遗漏的窥孔优化 |

## Session 5D: Storage & Caching

**中文主题：** 存储与缓存

| 英文标题 | 中文标题 |
| --- | --- |
| [Nemo: A Low-Write-Amplification Cache for Tiny Objects on Log-Structured Flash Devices](Session-5D/nemo-a-low-write-amplification-cache-for-tiny-objects-on-log-structured-flash-devices.md) | Nemo：面向日志结构闪存设备上小对象的低写放大缓存 |
| [ICARUS: Criticality and Reuse based Instruction Caching for Datacenter Applications](Session-5D/icarus-criticality-and-reuse-based-instruction-caching-for-datacenter-applications.md) | ICARUS：面向数据中心应用的基于关键性与重用的指令缓存 |
| [CacheMind: From Miss Rates to Why – Natural-Language, Trace-Grounded Reasoning for Cache Replacement](Session-5D/cachemind-from-miss-rates-to-why-natural-language-trace-grounded-reasoning-for-cache-replacement.md) | CacheMind：从缺失率到原因——面向缓存替换的自然语言、基于轨迹的推理 |
| [Toasty: Speeding up network I/O with cache-warm buffers](Session-5D/toasty-speeding-up-network-i-o-with-cache-warm-buffers.md) | Toasty：使用缓存预热缓冲区加速网络 I/O |
| [Hitchhike: Efficient Request Submission via Deferred Enforcement of Address Contiguity](Session-5D/hitchhike-efficient-request-submission-via-deferred-enforcement-of-address-contiguity.md) | Hitchhike：通过延迟执行地址连续性校验实现高效请求提交 |

## Session 6A: Neural Network Acceleration

**中文主题：** 神经网络加速

| 英文标题 | 中文标题 |
| --- | --- |
| [History Doesn’t Repeat Itself but Rollouts Rhyme: Accelerating Reinforcement Learning with HistoRL](Session-6A/history-doesn-t-repeat-itself-but-rollouts-rhyme-accelerating-reinforcement-learning-with-historl.md) | 历史不会重演，但 Rollout 会押韵：用 HistoRL 加速强化学习 |
| [Hardwired-Neuron Language Processing Units as General-Purpose Cognitive Substrates](Session-6A/hardwired-neuron-language-processing-units-as-general-purpose-cognitive-substrates.md) | 硬连线神经元语言处理单元作为通用认知基底 |
| [Voyager: Input-Adaptive Algebraic Transformations for High-Performance Graph Neural Networks](Session-6A/voyager-input-adaptive-algebraic-transformations-for-high-performance-graph-neural-networks.md) | Voyager：面向高性能图神经网络的输入自适应代数变换 |
| [CREATE: Cross-Layer Resilience Characterization and Optimization for Efficient yet Reliable Embodied AI Systems](Session-6A/create-cross-layer-resilience-characterization-and-optimization-for-efficient-yet-reliable-embodied-ai-systems.md) | CREATE：面向高效且可靠的具身智能系统的跨层韧性刻画与优化 |
| [Syno: Structured Synthesis for Neural Operators](Session-6A/syno-structured-synthesis-for-neural-operators.md) ([code](https://github.com/tsinghua-ideal/Syno)) | Syno：神经算子的结构化合成 |

## Session 6B: Hardware Design Languages

**中文主题：** 硬件设计语言

| 英文标题 | 中文标题 |
| --- | --- |
| [Parameterized Hardware Design with Latency-Abstract Interfaces](Session-6B/parameterized-hardware-design-with-latency-abstract-interfaces.md) | 带延迟抽象接口的参数化硬件设计 |
| [Anvil: A General-Purpose Timing-Safe Hardware Description Language](Session-6B/anvil-a-general-purpose-timing-safe-hardware-description-language.md) | Anvil：一种通用的定时安全硬件描述语言 |
| [Rage Against the State Machine: Type-Stated Hardware Peripherals for Increased Driver Correctness](Session-6B/rage-against-the-state-machine-type-stated-hardware-peripherals-for-increased-driver-correctness.md) | 怒斥状态机：以类型陈述的硬件外设提升驱动程序正确性 |
| [RTeAAL Sim: Using Tensor Algebra to Represent and Accelerate RTL Simulation](Session-6B/rteaal-sim-using-tensor-algebra-to-represent-and-accelerate-rtl-simulation.md) | RTeAAL Sim：使用张量代数表示并加速 RTL 仿真 |
| [Sequential Specifications for Precise Hardware Exceptions](Session-6B/sequential-specifications-for-precise-hardware-exceptions.md) | 精确硬件异常的串行规范 |

## Session 6C: Graph & Sparse Computing

**中文主题：** 图计算与稀疏计算

| 英文标题 | 中文标题 |
| --- | --- |
| [TempGraph: An Efficient Chain-driven Temporal Graph Computing Framework on the GPU](Session-6C/tempgraph-an-efficient-chain-driven-temporal-graph-computing-framework-on-the-gpu.md) | TempGraph：一种高效的基于 GPU 的链驱动时序图计算框架 |
| [Leveraging Sparsity to Accelerate Automata Processing](Session-6C/leveraging-sparsity-to-accelerate-automata-processing.md) | 利用稀疏性加速自动机处理 |
| [SLAWS: Spatial Locality Analysis and Workload Orchestration for Sparse Matrix Multiplication](Session-6C/slaws-spatial-locality-analysis-and-workload-orchestration-for-sparse-matrix-multiplication.md) | SLAWS：面向稀疏矩阵乘法的空间局部性分析与工作负载编排 |
| [Efficient Temporal Graph Network Training via Unified Redundancy Elimination](Session-6C/efficient-temporal-graph-network-training-via-unified-redundancy-elimination.md) | 通过统一冗余消除实现高效的时序图网络训练 |
| [Understanding Query Optimization Bugs in Graph Database Systems](Session-6C/understanding-query-optimization-bugs-in-graph-database-systems.md) | 理解图数据库系统中的查询优化缺陷 |

## Session 6D: Disaggregated Memory Systems

**中文主题：** 解耦内存系统

| 英文标题 | 中文标题 |
| --- | --- |
| [Efficient Remote Memory Ordering for Non-Coherent Systems](Session-6D/efficient-remote-memory-ordering-for-non-coherent-systems.md) | 面向非一致性系统的高效远程内存排序 |
| [CPU-Oblivious Offloading of Failure-Atomic Transactions for Disaggregated Memory](Session-6D/cpu-oblivious-offloading-of-failure-atomic-transactions-for-disaggregated-memory.md) | 面向分离式内存的 CPU 无关的失败原子事务卸载 |
| [PIPM: Partial and Incremental Page Migration for Multi-host CXL Disaggregated Shared Memory](Session-6D/pipm-partial-and-incremental-page-migration-for-multi-host-cxl-disaggregated-shared-memory.md) | PIPM：面向多主机 CXL 分离式共享内存的部分与增量页迁移 |
| [CREST: High-Performance Contention Resolution for Disaggregated Transactions](Session-6D/crest-high-performance-contention-resolution-for-disaggregated-transactions.md) | CREST：面向分离式事务的高性能争用消解 |
| [Understanding and Optimizing Database Pushdown on Disaggregated Storage](Session-6D/understanding-and-optimizing-database-pushdown-on-disaggregated-storage.md) | 理解并优化分离式存储上的数据库下推 |

## Session 7A: Fully Homomorphic Encryption

**中文主题：** 全同态加密

| 英文标题 | 中文标题 |
| --- | --- |
| [A Framework for Developing and Optimizing Fully Homomorphic Encryption Programs on GPUs](Session-7A/a-framework-for-developing-and-optimizing-fully-homomorphic-encryption-programs-on-gpus.md) | 面向GPU的全同态加密程序开发与优化框架 |
| [HEPIC: Private Inference over Homomorphic Encryption with Client Intervention](Session-7A/hepic-private-inference-over-homomorphic-encryption-with-client-intervention.md) | HEPIC：基于同态加密并引入客户端介入的隐私推理 |
| [Falcon: Algorithm-Hardware Co-Design for Efficient Fully Homomorphic Encryption Accelerator](Session-7A/falcon-algorithm-hardware-co-design-for-efficient-fully-homomorphic-encryption-accelerator.md) | Falcon：面向高效全同态加密加速器的算法-硬件协同设计 |
| [Maverick: Rethinking TFHE Bootstrapping on GPUs via Algorithm-Hardware Co-Design](Session-7A/maverick-rethinking-tfhe-bootstrapping-on-gpus-via-algorithm-hardware-co-design.md) | Maverick：借助算法-硬件协同设计重新思考GPU上的TFHE自举 |

## Session 7B: Compilers & Code Generation

**中文主题：** 编译器与代码生成

| 英文标题 | 中文标题 |
| --- | --- |
| [COGENT: Adaptable Compiler Toolchain for Tagging RISC-V Binaries](Session-7B/cogent-adaptable-compiler-toolchain-for-tagging-risc-v-binaries.md) | COGENT：面向 RISC-V 二进制标记的可适配编译器工具链 |
| [Finding Reusable Instructions via E-Graph Anti-Unification](Session-7B/finding-reusable-instructions-via-e-graph-anti-unification.md) | 通过 E-Graph 反合一发现可复用指令 |
| [LOOPRAG: Enhancing Loop Transformation Optimization with Retrieval-Augmented Large Language Models](Session-7B/looprag-enhancing-loop-transformation-optimization-with-retrieval-augmented-large-language-models.md) | LOOPRAG：利用检索增强大语言模型增强循环变换优化 |
| [Evaluating Compiler Optimization Impacts on zkVM Performance](Session-7B/evaluating-compiler-optimization-impacts-on-zkvm-performance.md) | 评估编译器优化对 zkVM 性能的影响 |

## Session 7C: Testing & Fuzzing

**中文主题：** 测试与模糊测试

| 英文标题 | 中文标题 |
| --- | --- |
| [DejaVuzz: Disclosing Transient Execution Bugs with Dynamic Swappable Memory and Differential Information Flow Tracking assisted Processor Fuzzing](Session-7C/dejavuzz-disclosing-transient-execution-bugs-with-dynamic-swappable-memory-and-differential-information-flow-tracking-assisted-processor-fuzzing.md) | DejaVuzz：借助动态可交换内存与差分信息流追踪的处理器模糊测试揭示瞬态执行缺陷 |
| [Signal Breaker: Fuzzing Digital Signal Processors](Session-7C/signal-breaker-fuzzing-digital-signal-processors.md) | Signal Breaker：数字信号处理器的模糊测试 |
| [Scaling Automated Database System Testing](Session-7C/scaling-automated-database-system-testing.md) | 扩展自动化数据库系统测试 |
| [SEVI: Silent Data Corruption of Vector Instructions in Hyper-Scale Datacenters](Session-7C/sevi-silent-data-corruption-of-vector-instructions-in-hyper-scale-datacenters.md) | SEVI：超大规模数据中心中向量指令的静默数据损坏 |

## Session 7D: Processor Microarchitecture

**中文主题：** 处理器微架构

| 英文标题 | 中文标题 |
| --- | --- |
| [Co-Exploration of RISC-V Processor Microarchitectures and FreeRTOS Extensions for Lower Context Switch Latency](Session-7D/co-exploration-of-risc-v-processor-microarchitectures-and-freertos-extensions-for-lower-context-switch-latency.md) | 面向更低上下文切换延迟的 RISC-V 处理器微架构与 FreeRTOS 扩展协同探索 |
| [Chips Need DIP: Time-Proportional Per-Instruction Cycle Stacks at Dispatch](Session-7D/chips-need-dip-time-proportional-per-instruction-cycle-stacks-at-dispatch.md) | 芯片需要 DIP：分发阶段按时间比例的逐指令周期栈 |
| [Arm Weak Memory Consistency on Apple Silicon: What Is It Good For?](Session-7D/arm-weak-memory-consistency-on-apple-silicon-what-is-it-good-for.md) | Apple Silicon 上的 Arm 弱内存一致性：它有什么用？ |
| [A Data-Driven Dynamic Execution Orchestration Architecture](Session-7D/a-data-driven-dynamic-execution-orchestration-architecture.md) | 一种数据驱动的动态执行编排架构 |

## Session 8A: GPU Programming

**中文主题：** GPU 编程

| 英文标题 | 中文标题 |
| --- | --- |
| [cuJSON: A Highly Parallel JSON Parser for GPUs](Session-8A/cujson-a-highly-parallel-json-parser-for-gpus.md) | cuJSON：面向 GPU 的高度并行 JSON 解析器 |
| [CHERI-SIMT: Implementing Capability Memory Protection in GPGPUs](Session-8A/cheri-simt-implementing-capability-memory-protection-in-gpgpus.md) | CHERI-SIMT：在 GPGPU 中实现能力内存保护 |
| [Lobster: A GPU-Accelerated Framework for Neurosymbolic Programming](Session-8A/lobster-a-gpu-accelerated-framework-for-neurosymbolic-programming.md) | Lobster：面向神经符号编程的 GPU 加速框架 |
| [ReliaFHE: Resilient Design for Fully Homomorphic Encryption Accelerators](Session-8A/reliafhe-resilient-design-for-fully-homomorphic-encryption-accelerators.md) | ReliaFHE：面向全同态加密加速器的弹性设计 |

## Session 8B: Serverless & Cloud Networking

**中文主题：** 无服务器计算与云网络

| 英文标题 | 中文标题 |
| --- | --- |
| [Lambda-trim: Reducing Monetary and Performance Cost of Serverless Cold Starts with Cost-driven Application Debloating](Session-8B/lambda-trim-reducing-monetary-and-performance-cost-of-serverless-cold-starts-with-cost-driven-application-debloating.md) | Lambda-trim：通过成本驱动的应用去膨胀降低无服务器冷启动的金钱成本与性能代价 |
| [Skyler: Static Analysis for Predicting API-Driven Costs in Serverless Applications](Session-8B/skyler-static-analysis-for-predicting-api-driven-costs-in-serverless-applications.md) | Skyler：预测无服务器应用中 API 驱动成本的静态分析 |
| [Enabling fast networking in the public cloud](Session-8B/enabling-fast-networking-in-the-public-cloud.md) | 在公有云中实现快速网络 |
| [SG-IOV: Socket-Granular I/O Virtualization for SmartNIC-Based Container Networks](Session-8B/sg-iov-socket-granular-i-o-virtualization-for-smartnic-based-container-networks.md) | SG-IOV：面向基于 SmartNIC 的容器网络的套接字粒度 I/O 虚拟化 |

## Session 8C: Memory Hierarchy & Performance

**中文主题：** 内存层次结构与性能

| 英文标题 | 中文标题 |
| --- | --- |
| [PACT: A Criticality-First Design for Tiered Memory](Session-8C/pact-a-criticality-first-design-for-tiered-memory.md) | PACT：一种面向分层内存的关键性优先设计 |
| [CounterPoint: Using Hardware Event Counters to Refute and Refine Microarchitectural Assumptions](Session-8C/counterpoint-using-hardware-event-counters-to-refute-and-refine-microarchitectural-assumptions.md) | CounterPoint：利用硬件事件计数器反驳并修正微架构假设 |
| [Performance Predictability in Heterogeneous Memory](Session-8C/performance-predictability-in-heterogeneous-memory.md) | 异构内存中的性能可预测性 |
| [PF-LLM: Large Language Model Hinted Hardware Prefetching](Session-8C/pf-llm-large-language-model-hinted-hardware-prefetching.md) | PF-LLM：大语言模型提示的硬件预取 |

## Session 8D: Reconfigurable Architectures

**中文主题：** 可重构架构

| 英文标题 | 中文标题 |
| --- | --- |
| [Neura: A Unified Framework for Hierarchical and Adaptive CGRAs](Session-8D/neura-a-unified-framework-for-hierarchical-and-adaptive-cgras.md) | Neura：面向层次化与自适应 CGRA 的统一框架 |
| [Transforming Torus Fabrics for Efficient Multi-tenant ML](Session-8D/transforming-torus-fabrics-for-efficient-multi-tenant-ml.md) | 为高效多租户机器学习改造 Torus 互连网络 |
| [The Configuration Wall: Characterization and Elimination of Accelerator Configuration Overhead](Session-8D/the-configuration-wall-characterization-and-elimination-of-accelerator-configuration-overhead.md) | 配置墙：加速器配置开销的表征与消除 |
| [Static Analysis for Efficient Streaming Tokenization](Session-8D/static-analysis-for-efficient-streaming-tokenization.md) | 面向高效流式分词的静态分析 |

## Session 9A: Systems Profiling & Optimization

**中文主题：** 系统性能剖析与优化

| 英文标题 | 中文标题 |
| --- | --- |
| [Arancini: A Hybrid Binary Translator for Weak Memory Model Architectures](Session-9A/arancini-a-hybrid-binary-translator-for-weak-memory-model-architectures.md) | Arancini：面向弱内存模型架构的混合二进制翻译器 |
| [Wax: Optimizing Data Center Applications With Stale Profile](Session-9A/wax-optimizing-data-center-applications-with-stale-profile.md) | Wax：利用陈旧 Profile 优化数据中心应用 |
| [M2XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization](Session-9A/m2xfp-a-metadata-augmented-microscaling-data-format-for-efficient-low-bit-quantization.md) | M2XFP：一种面向高效低比特量化的元数据增强微缩放数据格式 |
| [Cheddar: A Swift Fully Homomorphic Encryption Library Designed for GPU Architectures](Session-9A/cheddar-a-swift-fully-homomorphic-encryption-library-designed-for-gpu-architectures.md) | Cheddar：一个为 GPU 架构设计的 Swift 全同态加密库 |

## Session 9B: Quantum & Emerging Computing

**中文主题：** 量子计算与新型计算

| 英文标题 | 中文标题 |
| --- | --- |
| [COMPAS: A Distributed Multi-Party SWAP Test for Parallel Quantum Algorithms](Session-9B/compas-a-distributed-multi-party-swap-test-for-parallel-quantum-algorithms.md) | COMPAS：一种用于并行量子算法的分布式多方 SWAP 测试 |
| [TreeVQA: A Tree-Structured Execution Framework for Shot Reduction in Variational Quantum Algorithms](Session-9B/treevqa-a-tree-structured-execution-framework-for-shot-reduction-in-variational-quantum-algorithms.md) | TreeVQA：一种用于减少变分量子算法采样次数的树状执行框架 |
| [CHEHAB RL: Learning to Optimize Fully Homomorphic Encryption Computations](Session-9B/chehab-rl-learning-to-optimize-fully-homomorphic-encryption-computations.md) | CHEHAB RL：学习优化全同态加密计算 |
| [CEMU: Enabling Full-System Emulation of Computational Storage beyond Hardware Limits](Session-9B/cemu-enabling-full-system-emulation-of-computational-storage-beyond-hardware-limits.md) | CEMU：实现超越硬件限制的计算型存储全系统仿真 |

## Session 9C: Reliability & Fault Tolerance

**中文主题：** 可靠性与容错

| 英文标题 | 中文标题 |
| --- | --- |
| [Fault Escaping: Improving Robustness of DPU Enhanced Platform with Mutual Assisted VM Recovery](Session-9C/fault-escaping-improving-robustness-of-dpu-enhanced-platform-with-mutual-assisted-vm-recovery.md) | Fault Escaping：借助互助式虚拟机恢复提升 DPU 增强平台的鲁棒性 |
| [Radshield: Software Radiation Protection for Commodity Hardware in Space](Session-9C/radshield-software-radiation-protection-for-commodity-hardware-in-space.md) | Radshield：面向太空商用硬件的软件辐射防护 |
| [TierX: A Simulation Framework for Multi-tier BCI System Design Evaluation and Exploration](Session-9C/tierx-a-simulation-framework-for-multi-tier-bci-system-design-evaluation-and-exploration.md) | TierX：面向多层次 BCI 系统设计评估与探索的仿真框架 |
| [PrioriFI: More Informed Fault Injection for Edge Neural Networks](Session-9C/priorifi-more-informed-fault-injection-for-edge-neural-networks.md) | PrioriFI：面向边缘神经网络的更知情故障注入 |

## Session 9D: Network & Cloud Infrastructure

**中文主题：** 网络与云基础设施

| 英文标题 | 中文标题 |
| --- | --- |
| [TiNA: Tiered Network Buffer Architecture for Fast Networking in Chiplet-based CPU](Session-9D/tina-tiered-network-buffer-architecture-for-fast-networking-in-chiplet-based-cpu.md) | TiNA：面向基于 Chiplet 的 CPU 中快速网络的分层网络缓冲区架构 |
| [An MLIR Lowering Pipeline for Stencils at Wafer-Scale](Session-9D/an-mlir-lowering-pipeline-for-stencils-at-wafer-scale.md) | 面向晶圆级 Stencil 计算的 MLIR 降级流水线 |
| [JOSer: Just-In-Time Object Serialization for Heavy Java Serialization Workloads](Session-9D/joser-just-in-time-object-serialization-for-heavy-java-serialization-workloads.md) | JOSer：面向重度 Java 序列化负载的即时对象序列化 |
| [Wave: Offloading Resource Management to SmartNIC Cores](Session-9D/wave-offloading-resource-management-to-smartnic-cores.md) | Wave：将资源管理卸载到 SmartNIC 核心 |

## 收录范围与来源

| 出版来源 | 收录论文条目数 | 说明 |
| --- | ---: | --- |
| [ASPLOS 2026 · Volume 1](https://doi.org/10.1145/3760250) | 20 | ASPLOS 2026 论文集 |
| [ASPLOS 2026 · Volume 2](https://doi.org/10.1145/3779212) | 132 | ASPLOS 2026 论文集 |
| [ASPLOS 2025 · Volume 3](https://doi.org/10.1145/3676642) | 16 | 发表于 2025 年论文集、在 ASPLOS 2026 宣讲 |
| **合计** | **168** | 与 Detailed Program 逐条对应 |

- 本目录按 **宣讲会议与 Session** 组织；论文 DOI 和出版卷号按出版记录标注。16 篇跨年论文在各自页面单独说明。
- 英文标题以官方日程为导航入口；与出版记录不同的题名在论文页注明“出版标题”。“Transforming Torus Fabrics…” 已纠正归属为 ASPLOS 2026 Volume 2。
- 中英文摘要与关键词沿用现有整理稿；“原文无 Keywords”表示原文未列出关键词，不按主题补造。原始 PDF 文件名仅作为来源记录，不表示本仓库提供 PDF 下载。
- 代码与研究制品仅列出已能确认与论文对应的链接；未列出链接不代表论文没有公开制品。
- DOI 与卷号核对来源：[Crossref](https://www.crossref.org/) 的 ACM 出版书目；日程、作者与单位核对来源：[会议官方 Program](https://www.asplos-conference.org/asplos2026/program/index.html)。核对日期：2026-11-24。
