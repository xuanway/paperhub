---
title: "DAC 2026: Serving Intelligence at Scale Architectural and Runtime Innovations for Large Models"
description: "DAC 2026 session: Serving Intelligence at Scale Architectural and Runtime Innovations for Large Models (9 papers)."
tags:
  - "DAC2026"
---

# DAC 2026: Serving Intelligence at Scale Architectural and Runtime Innovations for Large Models

**论文数量：** 9 篇

## Session Chairs

[Kartik Prabhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=542543)

[Cong Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=824843)

## Session Description

Rapid large language and diffusion-based model deployment has resulted in major bottlenecks in serving scalable and efficient inference. This session presents architectural and runtime innovations that improve throughput, energy efficiency, and service predictability across modern accelerator platforms. The works span sparsity-aware GPU kernels, metadata-efficient sparse formats, and erasure-coded KV-cache designs to surpass dense execution and reduce load imbalance in distributed serving. Heterogeneous CPU–GPU co-execution and predictive expert caching enable high-throughput Mixture-of-Experts inference, while hardware-aware routing integrates real-time system signals to meet service level objectives. Low-bit adaptive quantization with dedicated microarchitectures further reduces power without sacrificing accuracy. Additional advances accelerate diffusion-based LLMs through phase-aware optimization and speculative decoding and introduce adaptive operator-level tuning frameworks that eliminate redundant compilation overheads for dynamic-shape workloads. Together, these contributions advance scalable, high-efficiency large-model serving through tightly integrated architectural and runtime co-design.

## Papers

| English Title | 中文标题 |
| --- | --- |
| [Accelerating GPU Inference of Large Language Models with Moderately Unstructured Sparse Weight Matrices](accelerating-gpu-inference-of-large-language-models-with-moderately-unstructured-sparse-weight-matrices.md) | 利用中等非结构化稀疏权重矩阵加速大语言模型的 GPU 推理 |
| [Adana: Accelerating Large Language Models via Adaptive Nonuniform Asymmetric Quantization](adana:-accelerating-large-language-models-via-adaptive-nonuniform-asymmetric-quantization.md) | Adana：基于自适应非均匀非对称量化的 LLM 加速 |
| [CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution](cox-moe:-coalesced-expert-execution-for-high-throughput-moe-inference-with-amx-enabled-cpu-gpu-co-execution.md) | CoX-MoE：面向高吞吐 MoE 推理的合并式专家执行与 AMX 使能 CPU-GPU 协同执行 |
| [Ecprefix: Erasure-Coded Prefix KV Cache for Optimizing Load Balancing in Large Language Model Serving](ecprefix:-erasure-coded-prefix-kv-cache-for-optimizing-load-balancing-in-large-language-model-serving.md) | ECPrefix：用于优化大语言模型服务负载均衡的纠删码前缀 KV 缓存 |
| [Expertflow: Efficient Mixture-of-Experts Inference via Predictive Expert Caching and Token Scheduling](expertflow:-efficient-mixture-of-experts-inference-via-predictive-expert-caching-and-token-scheduling.md) | ExpertFlow：基于预测式专家缓存与 token 调度的 MoE 高效推理 |
| [HW-Router: Hardware-Aware Routing for Scalable Multi-LLM Serving](hw-router:-hardware-aware-routing-for-scalable-multi-llm-serving.md) | HW-Router：面向可扩展多 LLM 服务的硬件感知路由 |
| [Optimizing Dynamic-Shape Neural Networks: A Unified Approach to Adaptive Tuning](optimizing-dynamic-shape-neural-networks:-a-unified-approach-to-adaptive-tuning.md) | 优化动态形状神经网络：自适应调优的统一方法 |
| [Orchestrating Dual-Boundaries: An Arithmetic Intensity Inspired Acceleration Framework for Diffusion Language Models](orchestrating-dual-boundaries:-an-arithmetic-intensity-inspired-acceleration-framework-for-diffusion-language-models.md) | 统筹双重边界：一种受运算强度启发的扩散语言模型加速框架 |
| [Pillarsparse: Rethinking Unstructured Sparse Formats for Tensor Cores](pillarsparse:-rethinking-unstructured-sparse-formats-for-tensor-cores.md) | PillarSparse：重新审视面向张量核的非结构化稀疏格式 |

[DAC 2026 总览](../index.md) · [官方会议议程](https://www.dac.com/2026/program)
