An Efficient Heterogeneous Co-Design for Fine-Tuning on a Single GPU
Authors：
[Ruijia Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=60817391858073231141)，[Zeyi Wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=0090789329129344965)

## 中文标题

面向单 GPU 微调的高效异构协同设计

## 英文摘要

Fine-tuning Large Language Models (LLMs) has become essential for domain adaptation, but its memory-intensive property exceeds the capabilities of most GPUs. To address this challenge and democratize LLM fine-tuning, we present SlideFormer, a novel system designed for single-GPU environments. Our innovations are: (1) A lightweight asynchronous engine that treats the GPU as a sliding window and overlaps GPU computation with CPU updates and multi-tier I/O. (2) A highly efficient heterogeneous memory management scheme significantly reduces peak memory usage. (3) Optimized Triton kernels to solve key bottlenecks and integrated advanced I/O. This collaborative design enables fine-tuning of the latest 123B+ models on a single RTX 4090, supporting up to 8× larger batch sizes and 6× larger models. In evaluations, SlideFormer achieves 1.40× to 6.27× higher throughput while roughly halving CPU/GPU memory usage compared to baselines, sustaining >95% peak performance on both NVIDIA and AMD GPUs.

## 中文摘要

大语言模型（LLM）的微调已成为领域适配的关键手段，但其内存密集型特性超出了大多数 GPU 的能力。为应对这一挑战并推动 LLM 微调的普及，我们提出 SlideFormer，一种面向单 GPU 环境设计的新系统。其创新点包括：(1) 轻量级异步引擎，将 GPU 视为一个滑动窗口，使 GPU 计算与 CPU 更新及多级 I/O 相互重叠；(2) 高效的异构内存管理方案，显著降低峰值内存占用；(3) 优化的 Triton 内核以解决关键瓶颈，并集成先进的 I/O 机制。这种协同设计使得在单块 RTX 4090 上微调最新的 123B+模型成为可能，支持最多 8×更大的批尺寸和 6×更大的模型。在评测中，相较基线，SlideFormer 的吞吐率高出 1.40×至 6.27×，同时 CPU/GPU 内存占用约减半，并在 NVIDIA 与 AMD GPU 上均保持>95%的峰值性能。

## 英文关键词

MLSys, LLM fine-tuning, Heterogeneous memory management

## 中文关键词

MLSys、LLM 微调、异构内存管理
