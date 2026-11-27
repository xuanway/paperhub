---
title: "DAC 2026: Efficient LLM and MoE Inference on Specialized Hardware"
description: "DAC 2026 session: Efficient LLM and MoE Inference on Specialized Hardware (10 papers)."
tags:
  - "DAC2026"
---

# DAC 2026: Efficient LLM and MoE Inference on Specialized Hardware

**论文数量：** 10 篇

## Session Chairs

[Xiang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=114843)

[Sangyeob Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=404843)

## Session Description

Large language models and mixture-of-experts architectures are creating new demands on specialized hardware, driven by growing model size, irregular execution, tight memory capacity, and increasing pressure on bandwidth and energy efficiency. This session brings together recent advances that address these challenges across multiple layers of the hardware stack, including expert caching, adaptive and mixed-precision computation, activation approximation and compression, reconfigurable dataflow design, and near-memory acceleration. Several papers focus directly on efficient LLM and MoE inference, proposing new architectural support for expert selection, speculative decoding, asymmetric GEMM, and bandwidth-aware execution on emerging memory systems. Others contribute techniques that improve the efficiency of core operators and model components through distribution-aware activation design, binary-coded quantization, adaptive precision, and robust activation compression for training. Taken together, these works reflect the rapid maturation of workload-driven AI hardware design, where performance depends not only on raw compute throughput, but also on how effectively architectures manage sparsity, precision diversity, data movement, and dynamic execution behavior in modern foundation models.

## Papers

| English Title | 中文标题 |
| --- | --- |
| [An Energy-Efficient Dataflow Architecture for Efficient MoE Model Inference](an-energy-efficient-dataflow-architecture-for-efficient-moe-model-inference.md) | 一种面向高效 MoE 模型推理的节能数据流架构 |
| [CAPA: Convertibility-Aware Mixed-Precision Accelerator for Asymmetric GEMM in Weight-Only Quantized LLMs](capa--convertibility-aware-mixed-precision-accelerator-for-asymmetric-gemm-in-weight-only-quantized-llms.md) | CAPA：面向权重量化 LLM 非对称 GEMM 的可转换性感知混合精度加速器 |
| [CORE: Compact, Optimized, and Resource-Efficient Compute Engine for FP-INT GEMM Acceleration with Binary Coding Quantization](core--compact-optimized-and-resource-efficient-compute-engine-for-fp-int-gemm-acceleration-with-binary-coding-quantization.md) | CORE：面向二值编码量化的 FP-INT GEMM 加速的紧凑、优化且资源高效计算引擎 |
| [DAPA: Distribution Aware Piecewise Activation Functions for On-Device Transformer Inference and Training](dapa--distribution-aware-piecewise-activation-functions-for-on-device-transformer-inference-and-training.md) | DAPA：面向端侧 Transformer 推理与训练的分布感知分段激活函数 |
| [HAP: Efficient Quantization Harnessing Adaptive Precision for DNN Hardware Acceleration](hap--efficient-quantization-harnessing-adaptive-precision-for-dnn-hardware-acceleration.md) | HAP：面向 DNN 硬件加速的利用自适应精度的高效量化 |
| [Hbspec: A Hybrid-Bonding-Based Heterogeneous Accelerator for Efficient Tree-Structured Speculative Decoding](hbspec--a-hybrid-bonding-based-heterogeneous-accelerator-for-efficient-tree-structured-speculative-decoding.md) | HBSpec：面向高效树结构推测解码的混合键合异构加速器 |
| [Hiband: A Hierarchical Bandwidth-Aware HB-DRAM Accelerator with Array-Level Co-Execution and Reconfigurable NoC for LLM Inference](hiband--a-hierarchical-bandwidth-aware-hb-dram-accelerator-with-array-level-co-execution-and-reconfigurable-noc-for-llm-inference.md) | HiBand：具备阵列级协同执行与可重构 NoC 的分层带宽感知 HB-DRAM LLM 推理加速器 |
| [REACT: Rapid Error-Tolerant Activation Compressor for Efficient Transformer Training](react--rapid-error-tolerant-activation-compressor-for-efficient-transformer-training.md) | REACT：面向高效 Transformer 训练的低开销容错激活压缩器 |
| [SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning](saem--stage-aware-expert-management-for-memory-efficient-moe-inference-in-chain-of-thought-reasoning.md) | SAEM：面向思维链推理中内存高效 MoE 推理的阶段感知专家管理 |
| [Slicemoe: Bit-Sliced Expert Caching Under Miss-Rate Constraints for Efficient MoE Inference](slicemoe--bit-sliced-expert-caching-under-miss-rate-constraints-for-efficient-moe-inference.md) | SliceMoE：未命中率约束下面向高效 MoE 推理的位切片专家缓存 |

[DAC 2026 总览](../index.md) · [官方会议议程](https://www.dac.com/2026/program)
