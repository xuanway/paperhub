Accelerating GPU Inference of Large Language Models with Moderately Unstructured Sparse Weight Matrices
Authors：
[Tao Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5433059659926980939)，[Haoyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=30317506339830652701)，[Zonghui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=57439189886637361811)，[Keshen Xiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5075093829239872253)，[Jiaheng Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=95323744779511511321)，[Wenzhi Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=6140109398167150292)

## 中文标题

利用中等非结构化稀疏权重矩阵加速大语言模型的 GPU 推理

## 英文摘要

With the growing deployment of large language models (LLMs), LLM inference cost has become a key challenge. Pruning techniques that introduce sparsity into weight matrices can accelerate inference. However, maintaining model quality typically limits pruning to moderate unstructured sparsity (around 50%). At these sparsity levels, none of the existing GPU kernels for sparse matrix multiplication (SpMM) can outperform their dense counterparts. This paper proposes an efficient GPU inference method for LLMs with moderate sparsity. We propose a three-layer matrix storage format comprising: (i) a Sparse-TC layer enabling sparse tensor cores to accelerate SpMM; (ii) a Slot-Filling layer using parallel differential distance for matrix compression while supporting low-cost on-chip decoding; (iii) a lightweight Residual Layer ensuring correct SpMM computation. Building on this format, we design a SpMM kernel that jointly utilizes sparse tensor cores and CUDA cores. This design enables an efficient execution pipeline and overlaps on-chip computation with memory access. Evaluations show that our work is the first to outperform dense matrix multiplication on modern GPUs equipped with high-bandwidth memory (HBM). It achieves up to 1.64× kernel-level speedup over SpInfer (EuroSys’25, Best paper) and up to 1.41× end-to-end speedups over FlashLLM (VLDB’24). Our source code: https://github.com/moui0/cudac.

## 中文摘要

随着大语言模型（LLM）的部署范围不断扩大，LLM 的推理成本已成为一项关键挑战。在权重矩阵中引入稀疏性的剪枝技术能够加速推理。然而，保持模型质量通常将剪枝限制在中等程度的非结构化稀疏（约 50%）。在这一稀疏度下，现有用于稀疏矩阵乘法（SpMM）的 GPU kernel 均无法超越与之对应的稠密实现。本文提出一种面向中等稀疏度 LLM 的高效 GPU 推理方法。我们提出一种三层矩阵存储格式，包括：(i) Sparse-TC 层，使稀疏张量核能够加速 SpMM；(ii) Slot-Filling 层，利用并行差分距离进行矩阵压缩，同时支持低成本的片上解码；(iii) 轻量的 Residual 层，确保 SpMM 计算正确。基于该格式，我们设计了一个同时利用稀疏张量核与 CUDA 核的 SpMM kernel。该设计实现了高效的执行流水线，并将片上计算与访存相互重叠。评估表明，我们的工作是首个在配备高带宽内存（HBM）的现代 GPU 上超越稠密矩阵乘法的方法。相较于 SpInfer（EuroSys'25 最佳论文），实现了最高 1.64× 的 kernel 级加速；相较于 FlashLLM（VLDB'24），实现了最高 1.41× 的端到端加速。源代码：https://github.com/moui0/cudac。
